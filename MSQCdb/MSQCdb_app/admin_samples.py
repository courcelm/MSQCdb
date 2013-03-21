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
from django.forms.models import BaseInlineFormSet
from django.utils.functional import curry
from django.utils.safestring import mark_safe

# Import project libraries
import MSQCdb.MSQCdb_app.models as MSQCdbModels



class SampleStackedInlineFormSet(BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SampleStackedInlineFormSet, self).__init__(*args, **kwargs)
    
    def save_new(self, form, commit=True):
        
        if self.request.user.is_superuser:
            return super(SampleStackedInlineFormSet, self).save_new(form, commit=commit)
        else:
            pass

    def save_existing(self, form, instance, commit=True):
        
        if self.request.user.is_superuser:
            return form.save(commit=commit)
        else:
            pass
    



class SampleStackedInline(admin.StackedInline):
    """
    StackedInline with overided save_model to restrict
    write to super user only.
    """

    extra = 0
    
    formset = SampleStackedInlineFormSet
    

    def get_formset(self, request, obj=None, **kwargs):

        formset = super(SampleStackedInline, self).get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, request=request)

        return formset




class MetadataOverviewInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetadataOverview

    classes = ('grp-collapse grp-open',)
    
    inline_classes = ('grp-collapse grp-open',)


class MetaTuneFileValueInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaTuneFileValue




class MetaPositivePolarityInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaPositivePolarity




class MetaNegativePolarityInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaNegativePolarity




class MetaAdditionalFtTuneFileValueInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaAdditionalFtTuneFileValue




class MetaReagentIonSourceTuneFileValueInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaReagentIonSourceTuneFileValue




class MetaCalibrationFileValueInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaCalibrationFileValue




class MetaCalibrationFileValueResEjectInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaCalibrationFileValueResEject




class MetaCalibrationFileValueMassInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaCalibrationFileValueMass




class MetaCalibrationFileValueFtCalInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaCalibrationFileValueFtCal




class MetaTuneDataInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaTuneData


class MetaCalibrationDataInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaCalibrationData




class MetaConfigurationDataInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.MetaConfigurationData




class ReportSpectrumCountInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportSpectrumCount




class ReportFirstAndLastMs1Rt_MinInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportFirstAndLastMs1Rt_Min




class ReportTrypticPeptideCountInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportTrypticPeptideCount




class ReportPeptideCountInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPeptideCount




class ReportDifferentProteinInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportDifferentProtein




class ReportMiddlePeptideRetentionTimePeriod_MinInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMiddlePeptideRetentionTimePeriod_Min




class ReportMs1DuringMiddle_AndEarly_PeptideRetentionPerInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs1DuringMiddle_AndEarly_PeptideRetentionPer




class ReportMs1TotalIonCurrentForDifferentRtPeriodInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs1TotalIonCurrentForDifferentRtPeriod




class ReportTotalIonCurrentForIdsAtPeakMaximaInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportTotalIonCurrentForIdsAtPeakMaxima




class ReportPrecursorMZForIdInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPrecursorMZForId




class ReportNumberOfIonsVsChargeInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportNumberOfIonsVsCharge




class ReportAveragesVsRtForIdedPeptideInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportAveragesVsRtForIdedPeptide




class ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejecInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejec




class ReportIonIdsByChargeState_RelativeToPlus2Inline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIonIdsByChargeState_RelativeToPlus2




class ReportAveragePeptideLengthsForDifferentChargeStateInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportAveragePeptideLengthsForDifferentChargeState




class ReportAveragePeptideLengthsForCharge2ForDifferentNInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportAveragePeptideLengthsForCharge2ForDifferentN




class ReportNumbersOfIonIdsAtDifferentChargesWith1MobileInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportNumbersOfIonIdsAtDifferentChargesWith1Mobile




class ReportPercentOfIdsAtDifferentChargesAndMobileProtoInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPercentOfIdsAtDifferentChargesAndMobileProto




class ReportIntensitiesVsDifferentMobileProtonInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIntensitiesVsDifferentMobileProton




class ReportPrecursorMZMonoisotopeExactMZInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPrecursorMZMonoisotopeExactMZ




class ReportMs2IdSpectraInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs2IdSpectra




class ReportMs1IdMaxInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs1IdMax




class ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuarInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuar




class ReportMs1IdAbundAtMs2AcquisitionInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs1IdAbundAtMs2Acquisition




class ReportMs2IdAbundReportedInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs2IdAbundReported




class ReportPeakWidthAtHalfHeightForIdInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPeakWidthAtHalfHeightForId




class ReportPeakWidthsAtHalfMaxOverRtDecilesForIdInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPeakWidthsAtHalfMaxOverRtDecilesForId




class ReportNearbyResamplingOfIdsOversamplingDetailInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportNearbyResamplingOfIdsOversamplingDetail




class ReportWideRtDifferencesForIds_Gt4MinInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportWideRtDifferencesForIds_Gt4Min




class ReportFractionOfRepeatPeptideIdsWithDivergentRt_RtInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportFractionOfRepeatPeptideIdsWithDivergentRt_Rt




class ReportEarlyAndLateRtOversampling_SpectrumIdsUniqueInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportEarlyAndLateRtOversampling_SpectrumIdsUnique




class ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_Inline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_




class ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfSInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfS




class ReportSingleSpectrumPeptideIonIdentificationsOversInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportSingleSpectrumPeptideIonIdentificationsOvers




class ReportMs1MaxMs1SampledAbundanceRatioIdsInefficientInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportMs1MaxMs1SampledAbundanceRatioIdsInefficient




class ReportRt_Ms1Max_Rt_Ms2_ForIds_SecInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportRt_Ms1Max_Rt_Ms2_ForIds_Sec




class ReportIonInjectionTimesForIds_MsInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIonInjectionTimesForIds_Ms




class ReportTopIonAbundanceMeasureInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportTopIonAbundanceMeasure




class ReportIsotopicAbundanceVariationInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIsotopicAbundanceVariation




class ReportIonPeakClusterCountDistributionInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIonPeakClusterCountDistribution




class ReportIonClusterAbundanceDistributionInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportIonClusterAbundanceDistribution




class ReportAbundanceDistributionTotalInline(SampleStackedInline):
    """
    Admin config for InLine
    """
    
    model = MSQCdbModels.ReportAbundanceDistributionTotal




class ReportAbundanceDistribution1RtQuartileInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportAbundanceDistribution1RtQuartile




class ReportAbundanceDistribution2RtQuartileInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportAbundanceDistribution2RtQuartile




class ReportAbundanceDistribution3RtQuartileInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportAbundanceDistribution3RtQuartile




class ReportAbundanceDistribution4RtQuartileInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportAbundanceDistribution4RtQuartile




class ReportAbundanceDistributionLastSegmentInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportAbundanceDistributionLastSegment




class ReportMZMediansForClustersAtRtQuartiles_AllChargesInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportMZMediansForClustersAtRtQuartiles_AllCharges




class ReportMZMediansForClustersAtRtQuartiles_Plus2OnlyInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportMZMediansForClustersAtRtQuartiles_Plus2Only




class ReportMZMediansForClustersAtDifferentChargeInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportMZMediansForClustersAtDifferentCharge




class ReportNumbersOfClustersOfDifferentChargeInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportNumbersOfClustersOfDifferentCharge




class ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuarInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuar




class ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuarInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuar




class ReportFractOfClusterAbundanceAt50PercentAnd90PerceInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportFractOfClusterAbundanceAt50PercentAnd90Perce




class ReportTop10NoidIonInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportTop10NoidIon




class ReportNewMetricInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportNewMetric




class ReportOtherIonClusterStatisticInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportOtherIonClusterStatistic



class ReportHcdMetricInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportHcdMetric
    
    
    
    
class ReportPeakWidthForMiddleHalfOfSignalForIdInline(SampleStackedInline):
    """
    Admin config for InLine
    """
        
    model = MSQCdbModels.ReportPeakWidthForMiddleHalfOfSignalForId    

               



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
               MetaTuneDataInline,
               MetaCalibrationDataInline,
               MetaConfigurationDataInline,
               ReportSpectrumCountInline, 
               ReportFirstAndLastMs1Rt_MinInline,
               ReportTrypticPeptideCountInline,
               ReportPeptideCountInline,
               ReportDifferentProteinInline,
               ReportMiddlePeptideRetentionTimePeriod_MinInline,
               ReportMs1DuringMiddle_AndEarly_PeptideRetentionPerInline,
               ReportMs1TotalIonCurrentForDifferentRtPeriodInline,
               ReportTotalIonCurrentForIdsAtPeakMaximaInline,
               ReportPrecursorMZForIdInline,
               ReportNumberOfIonsVsChargeInline,
               ReportAveragesVsRtForIdedPeptideInline,
               ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejecInline,
               ReportIonIdsByChargeState_RelativeToPlus2Inline,
               ReportAveragePeptideLengthsForDifferentChargeStateInline,
               ReportAveragePeptideLengthsForCharge2ForDifferentNInline,
               ReportNumbersOfIonIdsAtDifferentChargesWith1MobileInline,
               ReportPercentOfIdsAtDifferentChargesAndMobileProtoInline,
               ReportIntensitiesVsDifferentMobileProtonInline,
               ReportPrecursorMZMonoisotopeExactMZInline,
               ReportMs2IdSpectraInline,
               ReportMs1IdMaxInline,
               ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuarInline,
               ReportMs1IdAbundAtMs2AcquisitionInline,
               ReportMs2IdAbundReportedInline,
               ReportPeakWidthAtHalfHeightForIdInline,
               ReportPeakWidthsAtHalfMaxOverRtDecilesForIdInline,
               ReportNearbyResamplingOfIdsOversamplingDetailInline,
               ReportWideRtDifferencesForIds_Gt4MinInline,
               ReportFractionOfRepeatPeptideIdsWithDivergentRt_RtInline,
               ReportEarlyAndLateRtOversampling_SpectrumIdsUniqueInline,
               ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_Inline,
               ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfSInline,
               ReportSingleSpectrumPeptideIonIdentificationsOversInline,
               ReportMs1MaxMs1SampledAbundanceRatioIdsInefficientInline,
               ReportRt_Ms1Max_Rt_Ms2_ForIds_SecInline,
               ReportIonInjectionTimesForIds_MsInline,
               ReportTopIonAbundanceMeasureInline,
               ReportIsotopicAbundanceVariationInline,
               ReportIonPeakClusterCountDistributionInline,
               ReportIonClusterAbundanceDistributionInline,
               ReportAbundanceDistributionTotalInline,
               ReportAbundanceDistribution1RtQuartileInline,
               ReportAbundanceDistribution2RtQuartileInline,
               ReportAbundanceDistribution3RtQuartileInline,
               ReportAbundanceDistribution4RtQuartileInline,
               ReportAbundanceDistributionLastSegmentInline,
               ReportMZMediansForClustersAtRtQuartiles_AllChargesInline,
               ReportMZMediansForClustersAtRtQuartiles_Plus2OnlyInline,
               ReportMZMediansForClustersAtDifferentChargeInline,
               ReportNumbersOfClustersOfDifferentChargeInline,
               ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuarInline,
               ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuarInline,
               ReportFractOfClusterAbundanceAt50PercentAnd90PerceInline,
               ReportTop10NoidIonInline,
               ReportNewMetricInline,
               ReportOtherIonClusterStatisticInline,
               ReportHcdMetricInline,
               ReportPeakWidthForMiddleHalfOfSignalForIdInline,
               
               ]
    
    list_display   = ('raw_file', 'fileURI', 'instrument_name', 
                      'instrument_software_version',
                      'instrumentmethod', 
                      'experimentdate')
    
    list_filter = ('instrument_name__instrument_name', 
                   'metadataoverview_Meta__instrument_software_version',
                   'metadataoverview_Meta__instrumentmethod'
                   )
    
    search_fields = ('raw_file_fullPath', 'instrument_name__instrument_name',
                     'metadataoverview_Meta__instrument_software_version',
                     'metadataoverview_Meta__instrumentmethod'
                     )


    def fileURI(self, obj):
        return mark_safe('<a href="%s">%s</a>' % (obj.raw_file_fullPath, 
                                                  obj.raw_file_fullPath))
    # In Chrome use LocalLinks to download the file
    fileURI.allow_tags = True
    fileURI.short_description = 'Raw file full path'
    fileURI.admin_order_field = 'raw_file_fullPath'
    
    
    def instrumentmethod(self, obj):
        return obj.metadataoverview_Meta.all()[0].instrumentmethod
    instrumentmethod.short_description = 'InstrumentMethod'
    instrumentmethod.admin_order_field  = 'metadataoverview_Meta__instrumentmethod'
    
    
    def instrument_software_version(self, obj):
        return obj.metadataoverview_Meta.all()[0].instrument_software_version
    instrument_software_version.short_description = 'Instrument Software Version'
    instrument_software_version.admin_order_field  = 'metadataoverview_Meta__instrument_software_version'



    def save_model(self, request, obj, form, change):

        if request.user.is_superuser:            
            obj.save()



