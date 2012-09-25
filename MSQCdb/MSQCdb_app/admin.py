from django.contrib import admin
from MSQCdb.MSQCdb_app.models import *



## Register admin panels
admin.site.register(MetadataOverview)
admin.site.register(MetadataOverviewTuneFileValue)
admin.site.register(MetadataOverviewPositivePolarity)
admin.site.register(MetadataOverviewNegativePolarity)
admin.site.register(MetadataOverviewAdditionalFtTuneFileValue)
admin.site.register(MetadataOverviewReagentIonSourceTuneFileValue)
admin.site.register(MetadataOverviewCalibrationFileValue)

