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

import os, sys, time
from config import *
from MSQCdb.MSQCdb_app.models import Sample
import processing
from time import  localtime, strftime
from datetime import datetime



def getRawFiles():
    # Inspect folder for Promix files
    rawFiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(config['SEARCH_DIR'])
                 for name in files
                 if name.startswith("Promix") and name.endswith(".RAW")]
    return  rawFiles



def getRecentRawFiles():

    # Inspect folder for recent Promix files

    deltaTimeLimit = config['SEARCH_MAXDAY'] * 24 * 60 * 60
    
    dirs = []
    for name in os.listdir(config['SEARCH_DIR']):
        path = os.path.join(config['SEARCH_DIR'], name)
        if os.path.isdir(path):
            
            deltaTime = time.mktime(localtime()) - os.stat(path).st_mtime
            if(deltaTime < deltaTimeLimit):
                dirs.append(path)

    rawFiles = []
    for directory in dirs:
        files = [os.path.join(root, name)
                     for root, dirs, files in os.walk(directory)
                     for name in files
                     if name.startswith("Promix") and name.endswith(".RAW")]
        rawFiles.extend(files)

    
    return rawFiles




def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]




def getIgnoreFiles():
    fh_in = open(config['ARCHIVE_DIR'] + r"\ignoreFiles.txt", 'r')
    
    ignoreFiles = []
    
    for line in fh_in:
        ignoreFiles.append(line.rstrip('\n').rstrip('*'))
    
    fh_in.close()
    
    return ignoreFiles




# Prepare log file
logFile_fh = open(config['ARCHIVE_DIR'] + r'\MSQCdb.log', 'a+')
sys.stdout = logFile_fh
sys.stderr = logFile_fh




# Read samples in db
samples = list(Sample.objects.all().values_list('raw_file_fullPath', flat=True))
#print type(samples)
#print samples


# Read ignore files
ignoreFiles = getIgnoreFiles()


# Daemon infinite loop
while True:
    
    # Inspect folder for Promix files
    rawFiles = getRawFiles()
    
    # Compute list difference with files in db
    #print len(rawFiles)
    rawFiles = diff(rawFiles, samples)
    rawFiles = diff(rawFiles, ignoreFiles)
    #print len(rawFiles)
    #print len(samples)
    
    print strftime("%Y-%m-%d %H:%M:%S",  localtime()) + ' --  ' + str(len(rawFiles)) + " files to process: " + str(rawFiles) + '\n'
    logFile_fh.flush() 
    # Should consider to add a datetime filter to be more efficient when the db is upto date
    
    
    # Process new Promix files
    for raw_file_fullPath in rawFiles:
        processing.process(raw_file_fullPath, logFile_fh)
        
        # Add to files in db
        samples.append(raw_file_fullPath)
    
    
    # Sleep for the specified amount of time
    time.sleep(config['SEARCH_INTERVAL'])




