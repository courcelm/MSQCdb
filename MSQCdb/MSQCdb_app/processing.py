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






def archive(rawFile):
    shutil.copy(r'%s\out_report.msqc' % (config['OUT_DIR']), r'%s\%s.msqc' % (config['ARCHIVE_DIR'], rawFile) )
    shutil.copy(r'%s\out_report.msqc.LOG' % (config['OUT_DIR']), r'%s\%s.msqc.LOG' % (config['ARCHIVE_DIR'], rawFile) )
    shutil.copy(r'%s\%s.metadata' % (config['OUT_DIR'], rawFile), r'%s' % (config['ARCHIVE_DIR']) )


def cleanInOut():    
    for fileName in os.listdir(config['OUT_DIR']):
        os.remove(config['OUT_DIR'] + "/" + fileName)
        
    for fileName in os.listdir(config['IN_DIR']):
        os.remove(config['IN_DIR'] + "/" + fileName)
    
    
def getFileName():
    for fileName in os.listdir(config['IN_DIR']):
        return fileName
    

def runNISTMSQC(logFile_fh):
    param = '--in_dir %s --out_dir %s --library Promix --instrument_type ORBI --search_engine OMSSA --overwrite_searches --pro_ms --log_file --verbose --mode full' % (config['IN_DIR'], config['OUT_DIR'])
    cmd = r'%s\perl.exe run_NISTMSQC_pipeline.pl %s' % (config['PERL_PATH'], param)
    
    subprocess.call(cmd, cwd=config['NISTMSQC_PATH'], stdout = logFile_fh, stderr= logFile_fh)
    
    
    

def testIntegrity(raw_file_fullPath):
    cmd = r'%s\msconvert.exe %s --filter "msLevel 5" -o %s' % (config['PROTEOWIZARD_DIR'], raw_file_fullPath, config['OUT_DIR'])

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    
    return not out.__contains__('Error')


def testMSMS(raw_file_fullPath):
    cmd = r'%s\msconvert.exe %s --filter "msLevel 2" --mgf -o %s --outfile testMSMS.mgf' % (config['PROTEOWIZARD_DIR'], raw_file_fullPath, config['OUT_DIR'])

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    
    b = os.path.getsize(r'%s\testMSMS.mgf' % (config['OUT_DIR']))
    
    if b == 0:
        return False
    else:
        return True



#### Main ######
def process(raw_file_fullPath, logFile_fh):
    
    
    print "Processing %s ...\n" % (raw_file_fullPath)
    
    cleanInOut()
    
    # Copy raw file to IN_DIR
    shutil.copy(r'%s' % (raw_file_fullPath), r'%s' % (config['IN_DIR']) )
    
    
    # Test file integrity
    if testIntegrity(raw_file_fullPath):
        
        # Test file for MSMS
        if testMSMS(raw_file_fullPath):

            rawFile = getFileName()
            
            
            print 'Running NISTMSQC...' 
            logFile_fh.flush()   
            runNISTMSQC(logFile_fh)
            print 'Done\n'
            
            print 'Storing metadata and report to database...'
            logFile_fh.flush()    
            parseAndStore.parseAndStore(rawFile, raw_file_fullPath, logFile_fh)
            print 'Done\n'
            
            print 'Archiving and Cleaning IN and OUT...'    
            archive(rawFile)
            cleanInOut()
            print 'Done\n'
            
            print "Processing of %s is completed.\n" % (raw_file_fullPath)
            logFile_fh.flush()
        
        else:
            # Add file to ignore list
            fh_out = open(config['ARCHIVE_DIR'] + r"\ignoreFiles.txt", 'a')
            fh_out.write('%s**\n' % (raw_file_fullPath))
            fh_out.close()
            
            print '%s has no MSMS. File was added to ignore list\n' % (raw_file_fullPath)
            logFile_fh.flush()
    else:
        # Add file to ignore list
        fh_out = open(config['ARCHIVE_DIR'] + r"\ignoreFiles.txt", 'a')
        fh_out.write('%s*\n' % (raw_file_fullPath))
        fh_out.close()
        
        print '%s failed file integrity test. File was added to ignore list\n' % (raw_file_fullPath)
        logFile_fh.flush() 
