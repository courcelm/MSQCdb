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


"""
This module has some helper functions to generate the data model.
"""

# Import standard libraries
import re


# Regexp pattern definitions
dateTimePattern = re.compile('^(?P<section>\d+-\d+-\d+ \d+:\d+)')
intPattern = re.compile('^(?P<floatValue>[-]*\d+$)')
floatPattern = re.compile('^(?P<floatValue>[-]*\d+\.\d+$)')
floatPattern2 = re.compile('^(?P<floatValue>[-]*\d+\.*\d*[eE][-+]\d+$)')



# Function definitions  ######################################################

def fieldType(s, text):
    """
    This function generates a Django data field based on the value provided.
    """
        
    match = floatPattern.search(s)
    if hasattr(match, 'group'):
        return 'FloatField("%s", null=True, blank=True)' % (text)
    
    match = floatPattern2.search(s)
    if hasattr(match, 'group'):
        return 'FloatField("%s", null=True, blank=True)' % (text)
        
    match = intPattern.search(s)
    if hasattr(match, 'group'):
        return 'IntegerField("%s", null=True, blank=True)' % (text)

    match = dateTimePattern.search(s)
    if hasattr(match, 'group'):
        return 'DateTimeField("%s", null=True, blank=True)' % (text)

    if len(s) > 50:
        return 'CharField("%s", max_length=100, null=True, blank=True)' % (text)
            
    return 'CharField("%s", max_length=50, null=True, blank=True)' % (text)




def readIgnoreList(fileName):
    """
    This function reads a file with the list fields in the sample file to
    ignore and returns a dictionnary. 
    """

    fieldsIgnoreDict = dict() # return value

    # Open ignore list file
    fh_in = open(fileName, 'r')


    # Read the list
    for line in fh_in:
    
        line = line.rstrip()
        fieldsIgnoreDict[line] = False

    fh_in.close()
    
    return fieldsIgnoreDict




def readModel(fileName):
    """
    This function read the fields of the current data model and returns a
    dictionnary of the classes and fields.
    """

    fieldsDict = dict() # return value
    section = ''
    
    classPattern = re.compile('^class (?P<class>.+)\(models\.Model\)')

    # Open model file
    fh_in = open(fileName, 'r')


    # Read the model
    for line in fh_in:
    
        line = line.rstrip()
    
        match = classPattern.search(line)
        if hasattr(match, 'group'):
            section = match.group('class')
            #print line
            continue
    
        keyVal_list = line.split('=', 1)
    
        if len(keyVal_list) == 2:
            key, value = keyVal_list
            key = key.replace (' ', '')
            value = value.replace (' models.', '')
            fieldsDict[section + '-' + key] = value
            #print (section + '-' + "%s=%s") % (key, value)

    fh_in.close()
    
    return fieldsDict




def sanitizeName(tmp_str):
    """
    This function takes a string of a field name and sanitizes it for
    the creation variable name for the field. 
    """
    
    tmp_str = tmp_str.replace (' ', '')
    tmp_str = tmp_str.replace('/','')
    tmp_str = tmp_str.replace('(','_')
    tmp_str = tmp_str.replace(')','_')
    tmp_str = tmp_str.replace ('[', '_')
    tmp_str = tmp_str.replace (']', '_')
    tmp_str = tmp_str.replace('-','')
    tmp_str = tmp_str.replace(':','')
    tmp_str = tmp_str.replace('>','Gt')
    tmp_str = tmp_str.replace('<','Lt')
    tmp_str = tmp_str.replace('+','Plus')
    tmp_str = tmp_str.replace ('=', 'eq')
    tmp_str = tmp_str.replace(',','')
    tmp_str = tmp_str.replace('.','Dot')
    tmp_str = tmp_str.replace('\'','')
    tmp_str = tmp_str.replace('%','Percent')
    tmp_str = tmp_str.replace('#','Nb')
    tmp_str = tmp_str.replace('__','_')
    tmp_str = tmp_str.replace ('@', 'at')
    tmp_str = tmp_str.replace ('__', '_')
    tmp_str = tmp_str.rstrip('_')

    
    # Keep name short
    if len(tmp_str) > 45:
        tmp_str = tmp_str[0:44]


    return tmp_str

