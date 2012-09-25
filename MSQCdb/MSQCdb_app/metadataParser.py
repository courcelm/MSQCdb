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

metadata_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\LTQ-Orbitrap_XL_out\Promix_200812_1.RAW.metadata"
#metadata_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\LTQ-Orbitrap_Elite_out-OrbiHCD\FL-promix-1D-01.raw.metadata"
metadata_model_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\metadata.model"
metadata_model_discrepency_filename = r"H:\Mathieu\NIST_MSQC_pipeline_test\metadata_discrepency.ignore"
metadata_current_model_filename = r"C:\Users\Mathieu\Documents\Aptana Studio 3 Workspace\MSQCdb\MSQCdb_app\models.py"



### Read current model
classPattern = re.compile('^class (?P<class>.+)\(models\.Model\)')

fh_in = open(metadata_current_model_filename, "r")

fieldsDict = dict()
section = ""
for line in fh_in:
    
    line = line.rstrip()
    
    match = classPattern.search(line)
    if hasattr(match, 'group'):
        section = match.group('class')
        #print line
        continue
    
    keyVal_list = line.split("=", 1)
    
    if len(keyVal_list) == 2:
        key, value = keyVal_list
        key = key.replace (" ", "")
        value = value.replace (" models.", "")
        fieldsDict[section + '-' + key] = value
        #print (section + '-' + "%s=%s") % (key, value)

fh_in.close()


### Read metadata_discrepency.ignore
fh_in = open(metadata_model_discrepency_filename, "r")

fieldsIgnoreDict = dict()
fieldsIgnoreDict.setdefault('missing', False)
section = ""
for line in fh_in:
    
    line = line.rstrip()
    fieldsIgnoreDict[line] = True

fh_in.close()



### Metafile reading

# Regexp pattern definition for parsing
sectionPattern = re.compile('^------ (?P<section>[\w\s]+) ------')
dateTimePattern = re.compile('^(?P<section>\d+-\d+-\d+ \d+:\d+)')
intPattern = re.compile('^(?P<floatValue>[-]*\d+$)')
floatPattern = re.compile('^(?P<floatValue>[-]*\d+\.\d+$)')
floatPattern2 = re.compile('^(?P<floatValue>[-]*\d+\.\d+E-\d+$)')


maxValue = 0

def fieldType(s):
        
    match = floatPattern.search(s)
    if hasattr(match, 'group'):
        return 'FloatField()'
    
    match = floatPattern2.search(s)
    if hasattr(match, 'group'):
        return 'FloatField()'
        
    match = intPattern.search(s)
    if hasattr(match, 'group'):
        return "IntegerField()"
        

    match = dateTimePattern.search(s)
    if hasattr(match, 'group'):
        return "DateTimeField()"

    if len(s) > 50:
        return "CharField(max_length=100)"
            
    return "CharField(max_length=50)"



# Prepare header of meta output model
fh_out = open(metadata_model_filename, "w")
fh_out.write('from django.db import models\n\n\n\n\n')

fieldsInFileDict = dict()
fieldsIgnoreDict.setdefault('missing', True)
section = "Metadata_Overview"
subsection = ""
subsectionTmp = ""

fh_out.write("class " + section + "(models.Model):\n\n\n")

fh_out.write('    creation_date = models.DateTimeField(auto_now_add=True)\n\n')



fh_in = open(metadata_filename, "r")
for line in fh_in:
    line = line.rstrip()
    #print line
    
    match = sectionPattern.search(line)
    if hasattr(match, 'group'):
        section = match.group('section').replace (" ", "_")
        
        #print "SECTION:" + section
        
        ## Stop reading the file at this point
        ## all required data should be read at this point
        if section == "LTQ_Metadata":
            break
        continue

    if line == "":
        continue
        #print "space line"

    keyVal_list = line.split(":", 1)
    
    fieldTypeValue = ""
    if len(keyVal_list) == 1:
        subsection = line.replace (" ", "_")
        subsectionTmp = "_" + subsection
        #print "SUB-SECTION:" + subsection 
        fh_out.write("\n\n\n\nclass " + section + "_" + subsection + "(models.Model):\n\n\n")
        fh_out.write("    metadata = models.ForeignKey(Metadata_Overview, related_name='metadata')\n\n")
        continue
    else:
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
        
#        maxValue = max(len(value), maxValue)
#        print maxValue
        
        #print ("%s=%s") % (key, value)
        fieldTypeValue = ""
        if re.search("^ft_cal_item", key):
            fieldTypeValue = "FloatField()"
        else:
            fieldTypeValue = fieldType(value)
            
        
    
    
    # Check if field is in current model and no conflict
    fieldsInFileDict[section + subsectionTmp + "-" + key] = False
    if section + subsectionTmp + "-" + key in fieldsDict:
        currentValue = fieldsDict[section + subsectionTmp + "-" + key]
        if fieldTypeValue != currentValue:
            if not fieldsIgnoreDict.get(section + subsectionTmp + "-" + key):
                print "Model discrepency:\t" + fieldTypeValue + " : " + currentValue + "\t\t" + section + subsectionTmp + "-" + key
            else:
                #fh_out.write("    " + key + " = models." + currentValue + "\n\n")
                continue
            
    else:
        print "Model missing value:\t" + fieldTypeValue + "\t\t\t" + section + subsectionTmp + "-" + key
        fieldTypeValue = fieldTypeValue.replace (")", "null=True, blank=True)")
        fh_out.write("    " + key + " = models." + fieldTypeValue + "\n\n")
    
    #fh_out.write("    " + key + " = models." + fieldTypeValue + "\n\n")


# Check that file has all the fields defined in the model
for field in fieldsDict:
    #print field
    #print fieldsInFileDict.get(field)
    if fieldsInFileDict.get(field) == None:
        if not (field.endswith('metadata') or field.endswith('creation_date')):
            if not fieldsDict[field].endswith('null=True, blank=True)'):
                print "File missing value:\t" + field
    
    
fh_out.close()
fh_in.close()



