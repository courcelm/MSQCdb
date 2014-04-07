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
This module stores the parameters for running the daemon and the processing
of the NISTMSCQC pipeline.

Edit those parameters before running
"""


config = dict()

# Softwares path
config['NISTMSQC_PATH'] = r'H:\Mathieu\NIST_MSQC_pipeline_test\NISTMSQCv1_5_0\NISTMSQCv1_5_0\scripts'
config['PERL_PATH'] = r'C:\Perl\bin'
config['PROTEOWIZARD_DIR'] = r'C:\Proteowizard'

# Temporary path were the raw file is store for processing
# Note: For best performance use local drive
config['SUFFIX'] = r''
config['IN_DIR'] = r'C:\NISTMSQC_TMP\in' + config['SUFFIX']

# Temporary path were the NISTMSQC will generate his output
# Note: For best performance use local drive
config['OUT_DIR'] = r'C:\NISTMSQC_TMP\out' + config['SUFFIX']

# Directory where the metadata and NISTMSQC report files will be archive
config['ARCHIVE_DIR'] = r'H:\Mathieu\NIST_MSQC_pipeline_test\archive' + config['SUFFIX']

# Directory to save the temporary data model generated when metadata and 
# report files are parsed.
config['TMPMODEL_DIR'] = r'H:\Mathieu\NIST_MSQC_pipeline_test\tmpmodel'

# Directory where the current data model is stored
config['MODEL_DIR'] = r'C:\Users\Mathieu\Documents\Aptana Studio 3 Workspace\MSQCdb\MSQCdb\MSQCdb_app'

# Directory where the daemon will search for new raw files
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\QExactivePlus',]
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\QEXACTIVE',]
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\ORBITRAP',]
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\VELOS',]
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\ELITE',]
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\ORBITRAP', r'G:\Thibault\-=Proteomics_Raw_Data=-\VELOS', r'G:\Thibault\-=Proteomics_Raw_Data=-\ELITE']
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\ORBITRAP', r'G:\Thibault\-=Proteomics_Raw_Data=-\ELITE']
config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\QExactivePlus_slot_160', 
                         r'G:\Thibault\-=Proteomics_Raw_Data=-\ORBITRAP', 
                         r'G:\Thibault\-=Proteomics_Raw_Data=-\ELITE', 
                         'G:\Thibault\-=Proteomics_Raw_Data=-\QExactivePlus']
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\Tyers_ProhitsStorage\QEXACTIVE', r'G:\Thibault\-=Proteomics_Raw_Data=-\QEXACTIVE']
#config['SEARCH_DIRS'] = [r'G:\Thibault\-=Proteomics_Raw_Data=-\ORBITRAP',]

# Time interval that the daemon will wait before searching for new files
config['SEARCH_INTERVAL'] = 180

# Number of days from cuurent time that the daemon is looking for new files
config['SEARCH_MAXDAY'] = 30



