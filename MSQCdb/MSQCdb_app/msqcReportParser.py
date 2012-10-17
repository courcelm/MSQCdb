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
import modelReader



## Input/Output Files
reportFile = r"H:\Mathieu\NIST_MSQC_pipeline_test\LTQ-Orbitrap_XL_out\NIST_MSQC_pipeline_test_report.msqc"
modelFile = r"H:\Mathieu\NIST_MSQC_pipeline_test\report.model"



### Read current model
fieldsModelDict = dict()

### Read metadata_discrepency.ignore
fieldsIgnoreDict = dict() #modelReader.readIgnoreList(metadata_model_discrepency_filename)


# Prepare header of meta output model
fh_out = open(modelFile, "w")
fh_out.write('from django.db import models\n\n\n\n\n')



# Open and read metadata file

storeFlag = True
values = dict()

fh_in = open(reportFile, "r")




## Jump to the needed section of the file
for line in fh_in:
    if line == "Run Number\t1\t\n":
        break
line = fh_in

for line in fh_in:
    line = line.rstrip()
    #print line
    
    # Skip blank line        
    if line == "":
        continue
    
    keyVal_list = line.split("\t", 1)
    
    
    if len(keyVal_list) == 1:
        # This is a subsection
        section = line.title().replace (" ", "").rstrip("s")
        section = section.replace('/','')
        
        print section
        
        
        if not values.has_key(section):
            values[section] = dict()
                
        # Write new subsection to the new model file
        fh_out.write("\n\n\n\nclass %s(models.Model):\n\n\n" % (section))
        #fh_out.write("    metadata = models.ForeignKey(MetadataOverview, related_name='%(class)s_metadata')\n\n")
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
        
        
        fieldTypeValue = ""

        fieldTypeValue = modelReader.fieldType(value)
            
        
    
        # Check if field is in current model and no field type conflict
        longKey = "%s-%s" % (section, key)
        
        if longKey in fieldsModelDict:
            currentValue = fieldsModelDict[longKey]
            
            if re.sub(r'\(.*\)', '', fieldTypeValue) != re.sub(r'\(.*\)', '', currentValue):
                if fieldsIgnoreDict.get(longKey) == None:
                    print "Model discrepency:\t%s : %s\t\t%s-%s" % (fieldTypeValue, currentValue, section, key)
                    storeFlag = False
                
            if fieldTypeValue != currentValue:
                fh_out.write("    %s = models.%s\n\n" % (key, currentValue))
                values[section][key] = value
                continue
                
        else:
            print "Model missing value:\t%s\t\t\t%s-%s" % (fieldTypeValue, section, key)
            storeFlag = False
        
        fh_out.write("    %s = models.%s\n\n" % (key, fieldTypeValue))
        values[section][key] = value
        
        
fh_out.close()
fh_in.close()   