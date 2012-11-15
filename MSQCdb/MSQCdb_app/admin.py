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
This is the Admin module for the MSQCdb.
"""


# Import standard librariesdjang

# Import Django related libraries
from django import forms
from django.contrib import admin
from django.db.models import get_app, get_models
from django.utils.safestring import mark_safe


# Import project libraries
from admin_samples import SampleAdmin
import MSQCdb.MSQCdb_app.models as MSQCdbModels



class EventLogAdmin(admin.ModelAdmin):
    """
    Admin config for EventLog model
    """
    
    datetime = 'datetime'
    
    list_display   = ('datetime', 'created_by', 'instrument_name',
                      'event_type', 'name')
    
    list_filter = ('event_type', 'instrument_name', 'created_by')
    
    search_fields = ('name', 'description')


    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()


            

class MetadataOverviewAdmin(admin.ModelAdmin):
    """
    Admin config for MetadataOverview
    """

    date_hierarchy = 'experimentdate'
    
    list_display   = ('sample', 'thermo_raw_file', 'instrument_name',
                      'instrumentmethod', 'instrument_software_version',
                      'experimentdate')
    
    list_filter = ('instrument_name', 'instrument_software_version')
    
    search_fields = ('thermo_raw_file', 'instrument_name', 'instrumentmethod',)


    

class ChartSeriesForm(forms.ModelForm):
    """
    Admin config for ChartSeries model
    """

    app = get_app('MSQCdb_app')

    tableChoices = [(model.__name__, model._meta.verbose_name) for model in 
                    get_models(app) if model.__name__.startswith('Report') or 
                    model.__name__.startswith('Meta')]
    
    tableChoices.insert(0, ('',''))
    
    table = forms.ChoiceField(choices=tableChoices, label = 'Table', 
            widget=forms.Select(attrs={'onchange':'get_fieldOptions(this);'}))
    
    field = forms.CharField(label = 'Field', widget=forms.TextInput(
            attrs={'readonly': 'true', 'style': 'width: 250px;'}), 
            help_text='Change table to activate.')




class ChartSeriesInline(admin.TabularInline):
    """
    Admin config for ChartSeries InLine
    """
    
    extra = 2
    
    model = MSQCdbModels.ChartSeries
    
    form = ChartSeriesForm
    


    
class ChartEventFlagInline(admin.TabularInline):
    """
    Admin config for EventFlag InLine
    """
    
    extra = 1
    
    model = MSQCdbModels.ChartEventFlag
    
    classes = ('grp-collapse grp-closed',)
    
    inline_classes = ('grp-collapse grp-closed',)
    



class ChartAdmin(admin.ModelAdmin):
    """
    Admin config for Chart model
    """
    
    change_form_template = 'admin/chart_change_form.html'
    
    inlines = [ChartSeriesInline, ChartEventFlagInline]
    
    list_display   = ('title', 'created_by',)
    
    list_filter = ('created_by',)
    
    search_fields = ('title', )
    
    
    
    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()
    




## Register admin panels
admin.site.register(MSQCdbModels.MetadataOverview, MetadataOverviewAdmin)
admin.site.register(MSQCdbModels.EventLog, EventLogAdmin)
admin.site.register(MSQCdbModels.Sample, SampleAdmin)
admin.site.register(MSQCdbModels.Chart, ChartAdmin)
