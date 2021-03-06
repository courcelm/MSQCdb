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
This module parses and stores metadata and report results from the NISTMSQC
processing pipeline.
"""


# Import standard libraries
import pytz
import re
import sys

# Import Django related libraries
from django.db.utils import IntegrityError
from django.utils.dateparse import parse_datetime
from MSQCdb.MSQCdb_app.models import *
import MSQCdb.settings

# Import project libraries
from config import *
import modelReader




# Function definitions  ######################################################

def convert2LocalDateTime(datetime):
    """
    Converts a naive datetime to a localized datetime and returns it.
    """
    
    local = pytz.timezone(MSQCdb.settings.TIME_ZONE)    
    naive = parse_datetime(datetime)
    
    return local.localize(naive)




def createInstrumentObject(instrumentName):
    """
    Creates and returns an Instrument object.
    """
    
    instrumentObject = Instrument(instrument_name=instrumentName)
    instrumentObject.save()
    
    return instrumentObject




def createSample(rawFile, raw_file_fullPath, instrumentName, experimentdate):
    """
    Creates and returns a Sample object using the supplied parameters.
    """
    
    # Get the Instrument object
    instrumentObject = getInstrumentObject(instrumentName)
    
    if instrumentObject is None:
        instrumentObject = createInstrumentObject(instrumentName)
    
    # Create the Sample object
    sample_obj = Sample(raw_file=rawFile, raw_file_fullPath=raw_file_fullPath,
                        instrument_name=instrumentObject,
                        experimentdate=convert2LocalDateTime(experimentdate))
    sample_obj.save()
    
    return sample_obj




def getInstrumentObject(instrumentName):
    """
    Get and returns the Instrument object with the supplied name. 
    """
    
    try:
        return Instrument.objects.get(instrument_name=instrumentName)
    
    except Instrument.DoesNotExist:
        return None




def writeClassHeader(fh_out, section, vname, tablePrefix):
    """
    Writes a header for a new class in the data model file.
    """
    
    fh_out.write('\n\n\n\nclass %s(models.Model):\n\n\n' % (section))
    fh_out.write('    class Meta:\n')
    fh_out.write('        verbose_name = "%s"\n\n\n' % (vname))
    fh_out.write('    sample = models.ForeignKey(Sample, related_name=\'\
                    %(class)s_' + tablePrefix + '\')\n\n')




def parse(fh_out, fileName, tablePrefix, separator, fieldsModelDict, 
          fieldsIgnoreDict):
    """
    This function parses either the metadata or report the file generated by
    the NISTMSQC pipeline. It returns a dictionary with the parsed values. 
    """


    # Pattern definition
    beginNumberpattern = re.compile('^\d')


    # Initialize return dictionnary
    values = dict()
    values['storeFlag'] = True
    
    section = ''
    if tablePrefix == 'Meta':
        section = 'MetadataOverview'
        vname = tablePrefix + ': Metadata Overview'
        writeClassHeader(fh_out, section, vname, tablePrefix)
        values[section] = dict()


    # Open file 
    fh_in = open(fileName, 'r')

    # Jump to the needed section of the file
    if(tablePrefix == 'Report'):
        for line in fh_in:
            if line == 'Run Number\t1\t\n':
                break
            line = fh_in

            
    #Read each line and search for section and fields
    for line in fh_in:
        line = line.rstrip()
        #print line
        
        # Skip blank line        
        if line == '':
            continue
        
        keyVal_list = line.split(separator, 1)

        
        # Check for section
        if len(keyVal_list) == 1 or line.startswith('='):
            
            # Stop reading the file at this point
            # all required data should be read at this point
            if tablePrefix == 'Report':
                if line == 'End Series=1':
                    break
                
            if tablePrefix == 'Meta':
                if line == '------ LTQ Metadata ------':
                    break
                if line.startswith('=== Identification: ==='):
                    break
            
        
                
                
                
            # This is a section
            vname = tablePrefix + ': ' + line.replace('=', '').replace(':', '').title().rstrip('s').rstrip(' ')
            section = line.replace('=', '').replace(':', '').title().rstrip('s').rstrip(' ')
            section = modelReader.sanitizeName(section)
            section = tablePrefix + section
            #print section
            
            if line == '------ Metadata Overview ------':
                section = 'MetadataOverview'
                vname = tablePrefix + ': MetadataOverview'
            
            # Prepare values dictionary for the section
            if not values.has_key(section):
                values[section] = dict()
                    
            # Write new subsection to the new model file
            writeClassHeader(fh_out, section, vname, tablePrefix)
            continue
        
        # Skip Orbitrap Fusion, to much to store in metadata
        elif line.startswith('EvTuneCommonDevicesandHCDInjectPos'):
            break
        else:
            # If we reach here, we read key value pair
            key, value = keyVal_list;
            text = key
            text = text.rstrip(' ')
            key = key.replace (' ', '_')
            key = modelReader.sanitizeName(key)
            key = key.lower()
            
            # Add a prefix to field starting with a number
            match = beginNumberpattern.search(key)
            if hasattr(match, 'group'):
                key = 'n' + key
            
            value = value.lstrip()
            
            # Fix value for div by 0 or infinite value string representation
            if value == '1.#J' or value == '-1.#J' or value == '1.#IO' or \
                value == '1.$' or value == '-1.$' or value == '-1.#IO' or \
                value == '-1.$e+0' or value == '1.$e+0':
                value = '0.0'


            ## Split CalibrationFileValue into multiple class
            if tablePrefix == 'Meta':
                kv = dict()
                kv['mass_'] = tablePrefix + 'CalibrationFileValueMass'
                kv['ft_cal'] = tablePrefix + 'CalibrationFileValueFtCal'
                kv['resdot_eject'] = tablePrefix + 'CalibrationFileValueResEject'
                
                
                if section.startswith(tablePrefix + 'Calibration') and \
                    not section.endswith('Value'):
                    
                    flag = True
                    for k, v in kv.iteritems():
                        if key.startswith(k):
                            flag = False
                    
                    if section.endswith('Data'):
                        flag = False
                    
                    if flag:
                        section = tablePrefix + 'CalibrationFileValue'
                                    
                        # Write new subsection to the new model file
                        writeClassHeader(fh_out, section, vname, tablePrefix)
        
                
                
                for k, v in kv.iteritems():
                    if key.startswith(k) and section != v and not section.endswith('Data'):
                        section = v
                                    
                        if not values.has_key(section):
                            values[section] = dict()
                        
                        # Write new subsection to the new model file
                        writeClassHeader(fh_out, section, vname, tablePrefix)
                        break

            
            # Get field type for database model
            fieldTypeValue = modelReader.fieldType(value, text)

            if re.search('^ft_caldot_item', key):
                fieldTypeValue = 'FloatField("%s", null=True, blank=True)' % (text)
                
            # Check if field is in current model and no field type conflict
            longKey = '%s-%s' % (section, key)
            
            if longKey in fieldsModelDict:
                currentValue = fieldsModelDict[longKey]
                
                if re.sub(r'\(.*\)', '', fieldTypeValue) != \
                    re.sub(r'\(.*\)', '', currentValue):
                    
                    if fieldsIgnoreDict.get(longKey) is None and \
                        not (fieldTypeValue.startswith('Integer') and \
                              currentValue.startswith('Float')):
                        
                        print 'Model discrepency:\t%s : %s\t\t%s-%s' % \
                            (fieldTypeValue, currentValue, section, key)
                            
                        values['storeFlag'] = False
                    
                if fieldTypeValue != currentValue:
                    fh_out.write('    %s = models.%s\n\n' % (key, currentValue))
                    values[section][key] = value
                    continue
                    
            else:
                print 'Model missing value:\t%s\t\t\t%s-%s' % \
                    (fieldTypeValue, section, key)
                values['storeFlag'] = False
            
            fh_out.write('    %s = models.%s\n\n' % (key, fieldTypeValue))
            values[section][key] = value

    fh_in.close()
    
    return values
    
    
    
    
def storeCheck(values):
    """
    This function inspects the values dictionnary return by the parse function
    and checks the storeFlag to see if the current model is compatible with
    the files parsed. The processing including the daemon is stopped if the
    model is not compatible. Check the log file in order to fix the model.
    """
    
    if values['storeFlag']:
        del(values['storeFlag'])
        return True
    else:
        print 'ERROR: Model discrepency. Processing halted\n'
        sys.exit()




def storeInDB(values, sample_obj):
    """
    This function stores the values from the dictionnary into the database.
    """
    
    try:
        for key in values:    
            data_dict = values[key]
            data_dict['sample'] = sample_obj
            
            # Fix time
            if key == "MetadataOverview":
                data_dict['experimentdate'] = \
                    convert2LocalDateTime(data_dict['experimentdate'])

            
            if len(data_dict):
                obj = eval(key + "(**data_dict)")
                obj.save()
                
    except IntegrityError, Argument:
        print 'IntegrityError:  %s (file is probably already loaded in \
            database)' % (Argument)
            

    

# Script Main section ########################################################

def parseAndStore(rawFile, raw_file_fullPath, logFile_fh):
    """
    This function do all the processing for parsing and storing files
    generated by the NISTMSQC pipeline.
    """


    ### Read current model
    fieldsModelDict = modelReader.readModel(r'%s\models.py'
                                            % (config['MODEL_DIR']))


    ### Read modelDiscrepencyFile
    fieldsIgnoreDict = modelReader.readIgnoreList(r'%s\modelDiscrepency.ignore'
                                                   % (config['TMPMODEL_DIR']))
    
    
    # Prepare file handle and header for tmp model
    fh_out = open(r'%s\tmpModels.py' % (config['TMPMODEL_DIR']), 'w')
    fh_out.write('from django.db import models\n\n\n\n\n')

    # Read and parse metadata and report files
    metaFile = r'%s\%s.metadata' % (config['OUT_DIR'], rawFile)
    reportFile = r'%s\out%s_report.msqc' % (config['OUT_DIR'], config['SUFFIX'])

    metaValues = parse(fh_out, metaFile, 'Meta', ':', fieldsModelDict, 
                       fieldsIgnoreDict)
    
    # Fix Q Exactive Plus name
    #print '-%s-' % metaValues['MetadataOverview']['instrument_name']
    
    if metaValues['MetadataOverview']['instrument_name'] == 'Q Exactive Plus Orbitrap':
        
        slot_id = metaValues['MetadataOverview']['instrument_serial_number'].split('#')[1]
        metaValues['MetadataOverview']['instrument_name'] += ' slot #' + slot_id
        
    #print metaValues['MetadataOverview']['instrument_name']
    
    reportValues = parse(fh_out, reportFile, 'Report', '\t', fieldsModelDict, 
                         fieldsIgnoreDict)
    fh_out.close()
    
    
    ## Check that file has MS1 spectrum
    ms1 = 0
    if reportValues.has_key('ReportSpectrumCount'):
        ms1 = reportValues['ReportSpectrumCount']['ms1_scansfull']
        
    if ms1 == '0':
        # Add file to ignore list
        fh_out = open(config['ARCHIVE_DIR'] + r'\ignoreFiles.txt', 'a')
        fh_out.write('%s***\n' % (raw_file_fullPath))
        fh_out.close()
            
        print '%s has no MS1 (NISTMSQC). File was added to ignore list\n' \
            % (raw_file_fullPath)
        logFile_fh.flush()
        
    else:
        # Store objects in db
        if storeCheck(reportValues) and storeCheck(metaValues):
        
            # Create the sample object
            instrumentName = metaValues['MetadataOverview']['instrument_name']
            experimentdate = metaValues['MetadataOverview']['experimentdate']
            
            
            sample_obj = createSample(rawFile, raw_file_fullPath, 
                                      instrumentName, experimentdate)
            
#             import sys
#             sys.exit()
            
            # Save to database
            storeInDB(reportValues, sample_obj)
            storeInDB(metaValues, sample_obj)
    
