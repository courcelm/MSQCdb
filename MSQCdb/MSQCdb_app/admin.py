from django import forms
from django.contrib import admin
from MSQCdb.MSQCdb_app.models import *
from django.utils.safestring import mark_safe



class EventLogForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EventLogForm, self).__init__(*args, **kwargs)
        instrumentsChoice = [(metadataOverviewObject.instrument_name, metadataOverviewObject.instrument_name) for metadataOverviewObject in MetadataOverview.objects.all().distinct().order_by('instrument_name')]
        instrumentsChoice.insert(0, (u'', u'---------'))
        
        self.fields['instrument_name'] = forms.ChoiceField(choices=instrumentsChoice)

    class Meta:
        model = EventLog
    

    


class EventLogAdmin(admin.ModelAdmin):
    
    datetime = 'datetime'
    
    form = EventLogForm
    
    list_display   = ('datetime', 'created_by', 'instrument_name', 'event_type', 'name')
    
    list_filter = ('event_type', 'instrument_name', 'created_by')
    
    search_fields = ('name', 'description')


    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()


            

class MetadataOverviewAdmin(admin.ModelAdmin):

    date_hierarchy = 'experimentdate'
    
    list_display   = ('sample', 'thermo_raw_file', 'instrument_name', 'instrumentmethod', 'instrument_software_version', 'experimentdate')
    
    list_filter = ('instrument_name', 'instrument_software_version')
    
    search_fields = ('thermo_raw_file', 'instrument_name', 'instrumentmethod',)
    

class SampleAdmin(admin.ModelAdmin):

    date_hierarchy = 'experimentdate'
    
    list_display   = ('raw_file', 'fileURI', 'instrument_name', 'experimentdate')
    
    list_filter = ('instrument_name',)
    
    search_fields = ('raw_file_fullPath', 'instrument_name',)


    def fileURI(self, obj):
        return mark_safe('<a href="%s">%s</a>' % (obj.raw_file_fullPath, obj.raw_file_fullPath))
    # In Chrome use LocalLinks to download the file
    
    
    fileURI.allow_tags = True
    
    fileURI.short_description = 'Raw file full path'




## Register admin panels
admin.site.register(MetadataOverview, MetadataOverviewAdmin)
admin.site.register(EventLog, EventLogAdmin)
admin.site.register(Sample, SampleAdmin)

