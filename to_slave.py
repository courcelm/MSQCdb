from django.contrib.contenttypes.models import ContentType

def run():

 def do(Table):
  print Table
  if Table is not None:
   table_objects = Table.objects.all()
   for i in table_objects:
    i.save(using='slave')
 
 ContentType.objects.using('slave').all().delete()


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.auth.models.User'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.sites.models.Site'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.sessions.models.Session'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.auth.models.Group'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.contenttypes.models.ContentType'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.admin.models.LogEntry'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'south.models.MigrationHistory'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'django.contrib.auth.models.Permission'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.Instrument'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.EventLog'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.Sample'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.Chart'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ChartEventFlag'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ChartSeries'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.Report'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportChart'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaCalibrationData'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaConfigurationData'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaTuneData'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaAdditionalFtTuneFileValue'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaCalibrationFileValue'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaCalibrationFileValueFtCal'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaCalibrationFileValueMass'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaCalibrationFileValueResEject'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetadataOverview'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaNegativePolarity'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaPositivePolarity'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaReagentIonSourceTuneFileValue'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.MetaTuneFileValue'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistribution1RtQuartile'>":
   do(i.model_class())
  

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistribution2RtQuartile'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistribution3RtQuartile'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistribution4RtQuartile'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistributionLastSegment'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAbundanceDistributionTotal'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAveragePeptideLengthsForCharge2ForDifferentN'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAveragePeptideLengthsForDifferentChargeState'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportAveragesVsRtForIdedPeptide'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportDifferentProtein'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportEarlyAndLateRtOversampling_SpectrumIdsUnique'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportFirstAndLastMs1Rt_Min'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportFractOfClusterAbundanceAt50PercentAnd90Perce'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportFractionOfMs2IdentifiedAtDifferentMs1MaxQuar'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportFractionOfRepeatPeptideIdsWithDivergentRt_Rt'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportHcdMetric'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIntensitiesVsDifferentMobileProton'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIonPeakClusterCountDistribution'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIonClusterAbundanceDistribution'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIonIdsByChargeState_RelativeToPlus2'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIonInjectionTimesForIds_Ms'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportIsotopicAbundanceVariation'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMZMediansForClustersAtDifferentCharge'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMZMediansForClustersAtRtQuartiles_Plus2Only'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMZMediansForClustersAtRtQuartiles_AllCharges'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMiddlePeptideRetentionTimePeriod_Min'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs1DuringMiddle_AndEarly_PeptideRetentionPer'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs1IdAbundAtMs2Acquisition'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs1IdMax'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs1TotalIonCurrentForDifferentRtPeriod'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs1MaxMs1SampledAbundanceRatioIdsInefficient'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs2IdAbundReported'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportMs2IdSpectra'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNearbyResamplingOfIdsOversamplingDetail'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNewMetric'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNumberOfIonsVsCharge'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNumbersOfClustersAtPlus1Plus2ChargesAtRtQuar'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNumbersOfClustersAtPlus3Plus2ChargesAtRtQuar'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNumbersOfClustersOfDifferentCharge'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportNumbersOfIonIdsAtDifferentChargesWith1Mobile'>":
   do(i.model_class())


 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportOtherIonClusterStatistic'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPeakWidthAtHalfHeightForId'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPeakWidthForMiddleHalfOfSignalForId'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPeakWidthsAtHalfMaxOverRtDecilesForId'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPeptideCount'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPeptideIonIdsByGt3Spectra_Hi_Vs13Spectra_Lo_'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPercentOfIdsAtDifferentChargesAndMobileProto'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPrecursorMZMonoisotopeExactMZ'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPrecursorMZPeptideIonMZ_Plus2ChargeOnlyRejec'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportPrecursorMZForId'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportRatiosOfPeptideIonsIdedByDifferentNumbersOfS'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportRt_Ms1Max_Rt_Ms2_ForIds_Sec'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportSingleSpectrumPeptideIonIdentificationsOvers'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportSpectrumCount'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportTop10NoidIon'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportTopIonAbundanceMeasure'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportTotalIonCurrentForIdsAtPeakMaxima'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportTrypticPeptideCount'>":
   do(i.model_class())

 for i in ContentType.objects.all():
  if str(i.model_class()) == "<class 'MSQCdb.MSQCdb_app.models.ReportWideRtDifferencesForIds_Gt4Min'>":
   do(i.model_class())



