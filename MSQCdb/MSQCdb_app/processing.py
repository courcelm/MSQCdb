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


### The daemon should start this script to process each data file

from config import *
import os
import parseAndStore
import shutil
import subprocess
import sys



def archiveAndCleanOut(rawFile):
    shutil.copy(r'%s\out_report.msqc' % (config['OUT_DIR']), r'%s\%s.msqc' % (config['ARCHIVE_DIR'], rawFile) )
    shutil.copy(r'%s\out_report.msqc.LOG' % (config['OUT_DIR']), r'%s\%s.msqc.LOG' % (config['ARCHIVE_DIR'], rawFile) )
    shutil.copy(r'%s\%s.metadata' % (config['OUT_DIR'], rawFile), r'%s' % (config['ARCHIVE_DIR']) )
    
    for fileName in os.listdir(config['OUT_DIR']):
        os.remove(config['OUT_DIR'] + "/" + fileName)
        
    for fileName in os.listdir(config['IN_DIR']):
        os.remove(config['IN_DIR'] + "/" + fileName)
    
    
def getFileName():
    for fileName in os.listdir(config['IN_DIR']):
        return fileName
    

def runNISTMSQC():
    param = '--in_dir %s --out_dir %s --library Promix --instrument_type ORBI --search_engine OMSSA --overwrite_searches --pro_ms --log_file --verbose --mode full' % (config['IN_DIR'], config['OUT_DIR'])
    cmd = r'%s\perl.exe run_NISTMSQC_pipeline.pl %s' % (config['PERL_PATH'], param)
    
    subprocess.call(cmd, cwd=config['NISTMSQC_PATH'])
    
    
    





#### Main ######

rawFile = getFileName()


print 'Running NISTMSQC...'    
#runNISTMSQC()
print 'Done\n'

print 'Storing metadata and report to database...'    
parseAndStore.parseAndStore(rawFile)
print 'Done\n'

print 'Archiving and Cleaning IN and OUT...'    
#archiveAndCleanOut(rawFile)
print 'Done\n'
