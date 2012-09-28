## Copyright 2012 Mathieu Courcelles
## Mike Tyers lab / IRIC / Universite de Montreal 

## This file is part of the MSQCdb project
## MSQCdb is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.

## MSQCdb is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.

## You should have received a copy of the GNU Affero General Public
## License along with MSQCdb. If not, see <http://www.gnu.org/licenses/>.

import re
from MSQCdb.MSQCdb_app.models import *
import MSQCdb.settings as S
import modelReader
from django.utils.dateparse import parse_datetime
import pytz
from django.db.utils import IntegrityError
#import sys
#
#instrumentsChoice = [(metadataOverviewObject.instrument_name, metadataOverviewObject.instrument_name) for metadataOverviewObject in MetadataOverview.objects.all().distinct().order_by('instrument_name')]
#instrumentsChoice.append((u'--------',  None))
#print instrumentsChoice
#
#sys.exit(0)

## Input/Output Files
metadata_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\LTQ-Orbitrap_XL_out\Promix_200812_1.RAW.metadata"
#metadata_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\LTQ-Orbitrap_Elite_out-OrbiHCD\FL-promix-1D-01.raw.metadata"
metadata_model_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\metadata.model"
metadata_model_discrepency_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\metadata_discrepency.ignore"
metadata_current_model_filename = r"C:\Users\Mathieu\Documents\Aptana Studio 3 Workspace\MSQCdb\MSQCdb\MSQCdb_app\models.py"



### Read current model
fieldsModelDict = modelReader.readModel(metadata_current_model_filename)


### Read metadata_discrepency.ignore
fieldsIgnoreDict = modelReader.readIgnoreList(metadata_model_discrepency_filename)




### Metafile reading #####################################################################

fieldsInFileDict = dict()
sectionPattern = re.compile('^------ (?P<section>[\w\s]+) ------')
section = "MetadataOverview"
subsection = ""
storeFlag = True
values = dict()
values[section] = dict()


# Prepare header of meta output model
fh_out = open(metadata_model_filename, "w")
fh_out.write('from django.db import models\n\n\n\n\n')
fh_out.write("class %s(models.Model):\n\n\n" % (section))
fh_out.write('    creation_date = models.DateTimeField(auto_now_add=True)\n\n')


# Open and read metadata file
fh_in = open(metadata_filename, "r")
for line in fh_in:
    line = line.rstrip()
    #print line
    
    
    # Check for section
    match = sectionPattern.search(line)
    if hasattr(match, 'group'):
        section = match.group('section').title().replace(" ", "")
        if not values.has_key(section):
            values[section] = dict()
        #print "SECTION:" + section
        
        ## Stop reading the file at this point
        ## all required data should be read at this point
        if section == "LtqMetadata":
            break
        continue
    
        
    # Skip blank line        
    if line == "":
        continue
        #print "space line"


    
    keyVal_list = line.split(":", 1)
    
    
    if len(keyVal_list) == 1:
        # This is a subsection
        subsection = line.title().replace (" ", "").rstrip("s")
        
        if not values.has_key(section + subsection):
            values[section + subsection] = dict()
                
        # Write new subsection to the new model file
        fh_out.write("\n\n\n\nclass %s%s(models.Model):\n\n\n" % (section, subsection))
        fh_out.write("    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')\n\n")
        continue

    else:
        # If we reach here, we read key value pair
        key, value = keyVal_list;
        key = key.replace (" ", "_")
        key = key.replace (".", "")
        key = key.replace ("(", "")
        key = key.replace (")", "")
        key = key.replace ("[", "_")
        key = key.replace ("]", "_")
        key = key.replace ("-", "")
        key = key.replace ("__", "_")
        key = key.replace ("%", "percent")
        key = key.rstrip("_")
        key = key.lower()
        value = value.lstrip()
        

        ## Split CalibrationFileValue into multiple section
        kv = dict()
        kv['mass_'] = 'CalibrationFileValueMass'
        kv['ft_cal'] = 'CalibrationFileValueFtCal'
        kv['res_eject'] = 'CalibrationFileValueResEject'
        
        
        if subsection.startswith('Calibration') and not subsection.endswith('Value'):
            
            flag = True
            for k, v in kv.iteritems():
                if key.startswith(k):
                    flag = False
            
            if flag:
                subsection = 'CalibrationFileValue'
                            
                # Write new subsection to the new model file
                fh_out.write("\n\n\n\nclass %s%s(models.Model):\n\n\n" % (section, subsection))
                fh_out.write("    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')\n\n")

        
        
        for k, v in kv.iteritems():
            if key.startswith(k) and subsection != v:
                subsection = v
                            
                if not values.has_key(section + subsection):
                    values[section + subsection] = dict()
                
                # Write new subsection to the new model file
                fh_out.write("\n\n\n\nclass %s%s(models.Model):\n\n\n" % (section, subsection))
                fh_out.write("    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')\n\n")
                break
            
                        

        
        fieldTypeValue = ""

        if re.search("^ft_cal_item", key):
            fieldTypeValue = "FloatField(null=True, blank=True)"
        else:
            fieldTypeValue = modelReader.fieldType(value)
            
        
    
        # Check if field is in current model and no field type conflict
        longKey = "%s%s-%s" % (section, subsection, key)
        
        if longKey in fieldsModelDict:
            currentValue = fieldsModelDict[longKey]
            
            if re.sub(r'\(.*\)', '', fieldTypeValue) != re.sub(r'\(.*\)', '', currentValue):
                if fieldsIgnoreDict.get(longKey) == None:
                    print "Model discrepency:\t%s : %s\t\t%s%s-%s" % (fieldTypeValue, currentValue, section, subsection, key)
                    storeFlag = False
                
            if fieldTypeValue != currentValue:
                fh_out.write("    %s = models.%s\n\n" % (key, currentValue))
                values[section + subsection][key] = value
                continue
                
        else:
            print "Model missing value:\t%s\t\t\t%s%s-%s" % (fieldTypeValue, section, subsection, key)
            storeFlag = False
        
        fh_out.write("    %s = models.%s\n\n" % (key, fieldTypeValue))
        values[section + subsection][key] = value

fh_out.close()
fh_in.close()    






## Store objects in db
if storeFlag:
    MetadataOverview_dic = values['MetadataOverview']
    mtl = pytz.timezone(S.TIME_ZONE)    
    naive = parse_datetime(MetadataOverview_dic['experimentdate'])
    MetadataOverview_dic['experimentdate'] = mtl.localize(naive)
        
    mo_obj = MetadataOverview(**MetadataOverview_dic)
    
    try:
        mo_obj.save()
        
        del(values['MetadataOverview'])
        del(values['LtqMetadata'])
        
        for key in values:    
            d = values[key]
            d['metadata'] = mo_obj
            
            if len(d):
                obj = eval(key + "(**d)")
                obj.save()
    except IntegrityError, Argument:
        print "IntegrityError: " +  str(Argument) + " (file is probably already loaded in database)"
            
