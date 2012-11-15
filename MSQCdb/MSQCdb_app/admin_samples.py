## Copyright 2012 Mathieu Courcelles
## Mike Tyers's lab / IRIC / Universite de Montreal 

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
This is the Admin Samples module for the MSQCdb.
"""


# Import standard librariesdjang

# Import Django related libraries
from django.contrib import admin
from django.utils.safestring import mark_safe


# Import project libraries
import MSQCdb.MSQCdb_app.models as MSQCdbModels




class MetadataOverviewInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetadataOverview




class MetaTuneFileValueInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaTuneFileValue




class MetaPositivePolarityInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaPositivePolarity




class MetaNegativePolarityInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaNegativePolarity




class MetaAdditionalFtTuneFileValueInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaAdditionalFtTuneFileValue




class MetaReagentIonSourceTuneFileValueInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaReagentIonSourceTuneFileValue




class MetaCalibrationFileValueInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaCalibrationFileValue




class MetaCalibrationFileValueResEjectInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaCalibrationFileValueResEject




class MetaCalibrationFileValueMassInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaCalibrationFileValueMass




class MetaCalibrationFileValueFtCalInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.MetaCalibrationFileValueFtCal




class ReportSpectrumCountInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportSpectrumCount




class ReportFirstAndLastMs1Rt_MinInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportFirstAndLastMs1Rt_Min




class ReportTrypticPeptideCountInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportTrypticPeptideCount




class ReportPeptideCountInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPeptideCount




class ReportDifferentProteinInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportDifferentProtein




class ReportMiddlePeptideRetentionTimePeriod_MinInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMiddlePeptideRetentionTimePeriod_Min




#class Inline(admin.StackedInline):
#    """
#    Admin config for InLine
#    """
#    
#    extra = 0
#    
#    model = MSQCdbModels.




class SampleAdmin(admin.ModelAdmin):
    """
    Admin config for Sample model
    """

    date_hierarchy = 'experimentdate'

    inlines = [MetadataOverviewInline, 
               MetaTuneFileValueInline,
               MetaPositivePolarityInline, 
               MetaNegativePolarityInline,
               MetaAdditionalFtTuneFileValueInline, 
               MetaReagentIonSourceTuneFileValueInline,
               MetaCalibrationFileValueInline,
               MetaCalibrationFileValueResEjectInline,
               MetaCalibrationFileValueMassInline,
               MetaCalibrationFileValueFtCalInline,
               ReportSpectrumCountInline, 
               ReportFirstAndLastMs1Rt_MinInline,
               ReportTrypticPeptideCountInline,
               ReportPeptideCountInline,
               ReportDifferentProteinInline,
               ReportMiddlePeptideRetentionTimePeriod_MinInline,
               
               ]
    
    list_display   = ('raw_file', 'fileURI', 'instrument_name', 'experimentdate')
    
    list_filter = ('instrument_name__instrument_name',)
    
    search_fields = ('raw_file_fullPath', 'instrument_name__instrument_name',)


    def fileURI(self, obj):
        return mark_safe('<a href="%s">%s</a>' % (obj.raw_file_fullPath, 
                                                  obj.raw_file_fullPath))
    # In Chrome use LocalLinks to download the file
    fileURI.allow_tags = True
    fileURI.short_description = 'Raw file full path'



