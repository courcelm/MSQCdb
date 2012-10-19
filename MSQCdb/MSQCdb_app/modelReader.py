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


# Regexp pattern definition
dateTimePattern = re.compile('^(?P<section>\d+-\d+-\d+ \d+:\d+)')
intPattern = re.compile('^(?P<floatValue>[-]*\d+$)')
floatPattern = re.compile('^(?P<floatValue>[-]*\d+\.\d+$)')
floatPattern2 = re.compile('^(?P<floatValue>[-]*\d+\.\d+[eE][-+]\d+$)')



def fieldType(s, text):
        
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

    fieldsIgnoreDict = dict() # return value

    # Open ignore list file
    fh_in = open(fileName, "r")


    # Read the list
    for line in fh_in:
    
        line = line.rstrip()
        fieldsIgnoreDict[line] = False

    fh_in.close()
    
    return fieldsIgnoreDict




def readModel(fileName):

    fieldsDict = dict() # return value
    section = ""
    
    classPattern = re.compile('^class (?P<class>.+)\(models\.Model\)')

    # Open model file
    fh_in = open(fileName, "r")


    # Read the model
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
    
    return fieldsDict



