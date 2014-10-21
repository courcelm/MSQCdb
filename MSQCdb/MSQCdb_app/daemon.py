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
This is the daemon module for processing pipeline of MSQCdb.

It reads parameters from the config.py. It inspects folder for new files, 
launches the processing with NISTMSQC and store results to database.

The daemon stores STDOUT, STDERR to a log file.
"""


# Import standard librariesdjang
import scandir
import os
import sys
import time
from time import  localtime, strftime

# Import Django related libraries
from django.db.utils import OperationalError

# Import project libraries
from MSQCdb.MSQCdb_app.models import (Instrument, Sample)
from config import *
import processing


# Fix for Django 1.7
# http://stackoverflow.com/questions/25244631/models-arent-loaded-yet-error-while-populating-in-django1-8-and-python2-7-8
import django
django.setup()

# Function definitions  ######################################################

def diff(a, b):
    """
    This function computes and returns the difference between two lists. 
    """
    
    b = set(b)
    
    return [aa for aa in a if aa not in b]




def getIgnoreFiles():
    """
    This function reads the list of files that the daemon should ignore
    for processing and returns the list. 
    """
    
    fh_in = open(config['ARCHIVE_DIR'] + r'\ignoreFiles.txt', 'r')
    
    ignoreFiles = []
    
    for line in fh_in:
        ignoreFiles.append(line.rstrip('\n').rstrip('*'))
    
    fh_in.close()
    
    return ignoreFiles




def getRawFiles(fileDir):
    """
    This function inspects the folder defined by config['SEARCH_DIR'],
    searches for Promix raw files and return a list of files.
    """
    
    # Inspect folder for Promix files
    rawFiles = [os.path.join(root, name)
                 for root, dirs, files in scandir.walk(fileDir)
                 for name in files
                 if 'promix' in name.lower() and name.lower().endswith('.raw')]
    return  rawFiles




def getRecentRawFiles(fileDir):
    """
    This function inspects the folder defined by config['SEARCH_DIR'],
    extract the list of recently modified folders as specified by 
    config['SEARCH_MAXDAY'] searches for Promix raw files and returns a
    list of files.
    """
    

    # Search for recently modified folders
    deltaTimeLimit = config['SEARCH_MAXDAY'] * 24 * 60 * 60
    
    recentlyModifiedDirs = []
    for name in os.listdir(fileDir):
        path = os.path.join(fileDir, name)

        if os.path.isdir(path):
            deltaTime = time.mktime(localtime()) - os.stat(path).st_mtime

            if(deltaTime < deltaTimeLimit):
                recentlyModifiedDirs.append(path)
                

    # Inspect folder for recent Promix files
    rawFiles = []
    for directory in recentlyModifiedDirs:
        files = [os.path.join(root, name)
                     for root, dirs, files in os.walk(directory)
                     for name in files
                     if 'promix' in name.lower() and name.lower().endswith('.raw')]
        rawFiles.extend(files)

    
    return rawFiles




# Script Main section ########################################################


# Prepare log file
logFile_fh = open(config['ARCHIVE_DIR'] + r'\MSQCdb.log', 'a+')
sys.stdout = logFile_fh
sys.stderr = logFile_fh


# Get list of samples from the databases
sampleFiles = list(Sample.objects.all().values_list('raw_file_fullPath',
                                                    flat=True))


# Read the list of files to ignore
ignoreFiles = getIgnoreFiles()



# Daemon infinite loop
while True:
    
    try:
        # Inspect folder for new files
        rawFiles = []
        #rawFiles.extend(getRawFiles(r'G:\Thibault\-=Proteomics_Raw_Data=-\QEXACTIVE\tyers_data'))
        for fileDir in config['SEARCH_DIRS']:
            rawFiles.extend(getRawFiles(fileDir))
            #rawFiles.extend(getRecentRawFiles(fileDir))
        
        # Compute list difference with files in db and to ignore
        rawFiles = diff(rawFiles, sampleFiles)
        rawFiles = diff(rawFiles, ignoreFiles)
    
        # Log list of files    
        print strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' --  ' + \
                        str(len(rawFiles)) + " files to process: " + \
                        str(rawFiles) + '\n'
        logFile_fh.flush()
        
        
        # Process new files
        time.sleep(60)  # Sleep 1 min to be sure that RAW file are completely copied to the network drive.
        for raw_file_fullPath in rawFiles:
            processing.process(raw_file_fullPath, logFile_fh)
            
            # Add to file in the list of files stored in the database
            sampleFiles.append(raw_file_fullPath)
            
            #sys.exit()
            
    except (EnvironmentError, IOError), e: # parent of IOError, OSError *and* WindowsError where available
        print('MSQC error:' + str(e))
    except OperationalError, e:
        print('MSQC error:' + str(e))

    # Dummy query to DB to keep connection alive
    instruments = list(Instrument.objects.all())
            
    # Sleep for the specified amount of time
    time.sleep(config['SEARCH_INTERVAL'])




