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

from config import *
import modelReader
import re
import sys
from django.db.utils import IntegrityError
from MSQCdb.MSQCdb_app.models import *
import MSQCdb.settings
from django.utils.dateparse import parse_datetime
import pytz


## Input/Output Files
modelFile = r"%s\tmpModels.py" % (config['TMPMODEL_DIR'])
modelDiscrepencyFile = r"%s\modelDiscrepency.ignore" % (config['TMPMODEL_DIR'])
currentModelFile = r"%s\models.py" % (config['MODEL_DIR'])



def createSample(rawFile, raw_file_fullPath, instrumentName):
    sample_obj = Sample(raw_file=rawFile, raw_file_fullPath=raw_file_fullPath, instrument_name=instrumentName)
    sample_obj.save()
    return sample_obj


def writeClassHeader(fh_out, section, vname, tablePrefix):
    fh_out.write("\n\n\n\nclass %s(models.Model):\n\n\n" % (section))
    fh_out.write("    class Meta:\n")
    fh_out.write("        verbose_name = \"%s\"\n\n\n" % (vname))
    fh_out.write("    sample = models.ForeignKey(Sample, related_name='%(class)s_" + tablePrefix + "')\n\n")


def parse(fh_out, fileName, tablePrefix, separator, fieldsModelDict, fieldsIgnoreDict):


    # Pattern definition
    beginNumberpattern = re.compile('^\d')


    # Initialize return dictionnary
    values = dict()
    values['storeFlag'] = True
    
    section = ''
    if tablePrefix == 'Meta':
        section = "MetadataOverview"
        vname = tablePrefix + ": Metadata Overview"
        writeClassHeader(fh_out, section, vname, tablePrefix)
        values[section] = dict()


    # Open file 
    fh_in = open(fileName, "r")

    # Jump to the needed section of the file
    if(tablePrefix == 'Report'):
        for line in fh_in:
            if line == "Run Number\t1\t\n":
                break
            line = fh_in
            
    #Read each line and search for section and fields
    for line in fh_in:
        line = line.rstrip()
        #print line
        
        # Skip blank line        
        if line == "":
            continue
        
        keyVal_list = line.split(separator, 1)

        
        # Check for section
        if len(keyVal_list) == 1:
            
            # Stop reading the file at this point
            # all required data should be read at this point
            if tablePrefix == 'Report':
                if line == "End Series=1":
                    break
                
            if tablePrefix == 'Meta':
                if line == "------ LTQ Metadata ------":
                    break
                
            # This is a section
            vname = tablePrefix + ": " + line.title().rstrip("s")
            section = line.title().rstrip("s")
            section = modelReader.sanitizeName(section)
            section = tablePrefix + section
            #print section
            
            if line == '------ Metadata Overview ------':
                section = "MetadataOverview"
                vname = tablePrefix + ": MetadataOverview"
            
            # Prepare values dictionary for the section
            if not values.has_key(section):
                values[section] = dict()
                    
            # Write new subsection to the new model file
            writeClassHeader(fh_out, section, vname, tablePrefix)
            continue
        
        else:
            # If we reach here, we read key value pair
            key, value = keyVal_list;
            text = key
            text = text.rstrip(" ")
            key = key.replace (" ", "_")
            key = modelReader.sanitizeName(key)
            key = key.lower()
            
            # Add a prefix to field starting with a number
            match = beginNumberpattern.search(key)
            if hasattr(match, 'group'):
                key = 'n' + key
            
            value = value.lstrip()


            if tablePrefix == 'Meta':
                ## Split CalibrationFileValue into multiple section
                kv = dict()
                kv['mass_'] = tablePrefix + 'CalibrationFileValueMass'
                kv['ft_cal'] = tablePrefix + 'CalibrationFileValueFtCal'
                kv['res_eject'] = tablePrefix + 'CalibrationFileValueResEject'
                
                
                if section.startswith(tablePrefix + 'Calibration') and not section.endswith('Value'):
                    
                    flag = True
                    for k, v in kv.iteritems():
                        if key.startswith(k):
                            flag = False
                    
                    if flag:
                        section = tablePrefix + 'CalibrationFileValue'
                                    
                        # Write new subsection to the new model file
                        writeClassHeader(fh_out, section, vname, tablePrefix)
        
                
                
                for k, v in kv.iteritems():
                    if key.startswith(k) and section != v:
                        section = v
                                    
                        if not values.has_key(section):
                            values[section] = dict()
                        
                        # Write new subsection to the new model file
                        writeClassHeader(fh_out, section, vname, tablePrefix)
                        break

            
            # Get field type for database model
            fieldTypeValue = modelReader.fieldType(value, text)

            if re.search("^ft_caldot_item", key):
                fieldTypeValue = "FloatField(\"%s\", null=True, blank=True)" % (text)
                
            # Check if field is in current model and no field type conflict
            longKey = "%s-%s" % (section, key)
            
            if longKey in fieldsModelDict:
                currentValue = fieldsModelDict[longKey]
                
                if re.sub(r'\(.*\)', '', fieldTypeValue) != re.sub(r'\(.*\)', '', currentValue):
                    if fieldsIgnoreDict.get(longKey) == None:
                        print "Model discrepency:\t%s : %s\t\t%s-%s" % (fieldTypeValue, currentValue, section, key)
                        values['storeFlag'] = False
                    
                if fieldTypeValue != currentValue:
                    fh_out.write("    %s = models.%s\n\n" % (key, currentValue))
                    values[section][key] = value
                    continue
                    
            else:
                print "Model missing value:\t%s\t\t\t%s-%s" % (fieldTypeValue, section, key)
                values['storeFlag'] = False
            
            fh_out.write("    %s = models.%s\n\n" % (key, fieldTypeValue))
            values[section][key] = value

    fh_in.close()
    
    return values
    
    
    
    
def storeCheck(values):
    if values['storeFlag']:
        del(values['storeFlag'])
        return True
    else:
        print 'ERROR: Model discrepency. Processing halted\n'
        sys.exit()




def storeInDB(values, sample_obj):
    try:
        for key in values:    
            data_dict = values[key]
            data_dict['sample'] = sample_obj
            
            # Fix time
            if key == "MetadataOverview":
                mtl = pytz.timezone(MSQCdb.settings.TIME_ZONE)    
                naive = parse_datetime(data_dict['experimentdate'])
                data_dict['experimentdate'] = mtl.localize(naive)

            
            if len(data_dict):
                obj = eval(key + "(**data_dict)")
                obj.save()
    except IntegrityError, Argument:
        print "IntegrityError: " +  str(Argument) + " (file is probably already loaded in database)"
            
    

def parseAndStore(rawFile, raw_file_fullPath):


    ### Read current model
    fieldsModelDict = modelReader.readModel(currentModelFile)


    ### Read modelDiscrepencyFile
    fieldsIgnoreDict = modelReader.readIgnoreList(modelDiscrepencyFile)
    
    
    # Prepare file handle and header for tmp model
    fh_out = open(modelFile, "w")
    fh_out.write('from django.db import models\n\n\n\n\n')

    # Read report
    metaFile = r'%s\%s.metadata' % (config['OUT_DIR'], rawFile)
    reportFile = r'%s\out_report.msqc' % (config['OUT_DIR'])

    metaValues = parse(fh_out, metaFile, 'Meta', ':', fieldsModelDict, fieldsIgnoreDict)
    reportValues = parse(fh_out, reportFile, 'Report', '\t', fieldsModelDict, fieldsIgnoreDict)
    fh_out.close()
    
    ## Store objects in db
    if storeCheck(reportValues) and storeCheck(metaValues):
        instrumentName = metaValues['MetadataOverview']['instrument_name']
        sample_obj = createSample(rawFile, raw_file_fullPath, instrumentName)
        storeInDB(reportValues, sample_obj)
        storeInDB(metaValues, sample_obj)
    
