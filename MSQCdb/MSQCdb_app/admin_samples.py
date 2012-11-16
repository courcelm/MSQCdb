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




class ReportMs1DuringMiddle_AndEarly_PeptideRetentionPerInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs1DuringMiddle_AndEarly_PeptideRetentionPer




class ReportMs1TotalIonCurrentForDifferentRtPeriodInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs1TotalIonCurrentForDifferentRtPeriod




class ReportTotalIonCurrentForIdsAtPeakMaximaInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportTotalIonCurrentForIdsAtPeakMaxima




class ReportPrecursorMZForIdInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPrecursorMZForId




class ReportNumberOfIonsVsChargeInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNumberOfIonsVsCharge




class ReportAveragesVsRtForIdedPeptideInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAveragesVsRtForIdedPeptide




class ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejecInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejec




class ReportIonIdsByChargeState_RelativeToPlus2Inline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIonIdsByChargeState_RelativeToPlus2




class ReportAveragePeptideLengthsForDifferentChargeStateInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAveragePeptideLengthsForDifferentChargeState




class ReportAveragePeptideLengthsForCharge2ForDifferentNInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAveragePeptideLengthsForCharge2ForDifferentN




class ReportNumbersOfIonIdsAtDifferentChargesWith1MobileInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNumbersOfIonIdsAtDifferentChargesWith1Mobile




class ReportPercentOfIdsAtDifferentChargesAndMobileProtoInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPercentOfIdsAtDifferentChargesAndMobileProto




class ReportIntensitiesVsDifferentMobileProtonInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIntensitiesVsDifferentMobileProton




class ReportPrecursorMZMonoisotopeExactMZInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPrecursorMZMonoisotopeExactMZ




class ReportMs2IdSpectraInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs2IdSpectra




class ReportMs1IdMaxInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs1IdMax




class ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuarInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuar




class ReportMs1IdAbundAtMs2AcquisitionInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs1IdAbundAtMs2Acquisition




class ReportMs2IdAbundReportedInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs2IdAbundReported




class ReportPeakWidthAtHalfHeightForIdInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPeakWidthAtHalfHeightForId




class ReportPeakWidthsAtHalfMaxOverRtDecilesForIdInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPeakWidthsAtHalfMaxOverRtDecilesForId




class ReportNearbyResamplingOfIdsOversamplingDetailInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNearbyResamplingOfIdsOversamplingDetail




class ReportWideRtDifferencesForIds_Gt4MinInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportWideRtDifferencesForIds_Gt4Min




class ReportFractionOfRepeatPeptideIdsWithDivergentRt_RtInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportFractionOfRepeatPeptideIdsWithDivergentRt_Rt




class ReportEarlyAndLateRtOversampling_SpectrumIdsUniqueInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportEarlyAndLateRtOversampling_SpectrumIdsUnique




class ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_Inline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_




class ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfSInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfS




class ReportSingleSpectrumPeptideIonIdentificationsOversInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportSingleSpectrumPeptideIonIdentificationsOvers




class ReportMs1MaxMs1SampledAbundanceRatioIdsInefficientInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMs1MaxMs1SampledAbundanceRatioIdsInefficient




class ReportRt_Ms1Max_Rt_Ms2_ForIds_SecInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportRt_Ms1Max_Rt_Ms2_ForIds_Sec




class ReportIonInjectionTimesForIds_MsInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIonInjectionTimesForIds_Ms




class ReportTopIonAbundanceMeasureInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportTopIonAbundanceMeasure




class ReportIsotopicAbundanceVariationInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIsotopicAbundanceVariation




class ReportIonPeakClusterCountDistributionInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIonPeakClusterCountDistribution




class ReportIonClusterAbundanceDistributionInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportIonClusterAbundanceDistribution




class ReportAbundanceDistributionTotalInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistributionTotal




class ReportAbundanceDistribution1RtQuartileInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistribution1RtQuartile




class ReportAbundanceDistribution2RtQuartileInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistribution2RtQuartile




class ReportAbundanceDistribution3RtQuartileInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistribution3RtQuartile




class ReportAbundanceDistribution4RtQuartileInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistribution4RtQuartile




class ReportAbundanceDistributionLastSegmentInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportAbundanceDistributionLastSegment




class ReportMZMediansForClustersAtRtQuartiles_AllChargesInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMZMediansForClustersAtRtQuartiles_AllCharges




class ReportMZMediansForClustersAtRtQuartiles_Plus2OnlyInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMZMediansForClustersAtRtQuartiles_Plus2Only




class ReportMZMediansForClustersAtDifferentChargeInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportMZMediansForClustersAtDifferentCharge




class ReportNumbersOfClustersOfDifferentChargeInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNumbersOfClustersOfDifferentCharge




class ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuarInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuar




class ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuarInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuar




class ReportFractOfClusterAbundanceAt50PercentAnd90PerceInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportFractOfClusterAbundanceAt50PercentAnd90Perce




class ReportTop10NoidIonInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportTop10NoidIon




class ReportNewMetricInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportNewMetric




class ReportOtherIonClusterStatisticInline(admin.StackedInline):
    """
    Admin config for InLine
    """
    
    extra = 0
    
    model = MSQCdbModels.ReportOtherIonClusterStatistic




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


