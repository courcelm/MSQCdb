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
from django.contrib.admin.sites import site
from django.db.models import get_app, get_models
from django.utils.text import wrap



# Import project libraries
from admin_samples import SampleAdmin
import MSQCdb.MSQCdb_app.models as MSQCdbModels
from adminWidgets import *





class EventLogAdmin(admin.ModelAdmin):
    """
    Admin config for EventLog model
    """
    
    datetime = 'datetime'
    
    list_display   = ('datetime', 'created_by', 'instrument_name',
                      'event_type', 'name', 'truncatedDescription')
    
    list_filter = ('event_type', 'instrument_name', 'created_by')
    
    search_fields = ('name', 'description')
    
    
    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()
        
    
    def truncatedDescription(self, obj):
        lines = wrap(obj.description, 200).split('\n')
        lines = [line[:200] for line in lines]
        return '<br/>'.join(lines)
    truncatedDescription.short_description = 'Description'
    truncatedDescription.allow_tags = True
        


            

class ChartSeriesForm(forms.ModelForm):
    """
    Admin config for ChartSeries model
    """

    app = get_app('MSQCdb_app')

    tableChoices = [(model.__name__, model._meta.verbose_name) for model in 
                    get_models(app) if model.__name__.startswith('Report') or 
                    model.__name__.startswith('Meta')]
    
    tableChoices.pop(0)
    tableChoices.pop(0)
    tableChoices.pop(0)
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
    
    list_display   = ('title', 'created_by', 'yAxisTitle', 'seriesString',
                      'flagsString')
    
    list_filter = ('created_by', 
                   'chartseries__instrument_name__instrument_name',
                   'chartseries__table',
                   'chartseries__field',
                   'charteventflag__event_type',
                   'charteventflag__instrument_name__instrument_name',
                   )
    
    search_fields = ('title', 'yAxisTitle', 
                     'chartseries__name',
                     'chartseries__instrument_name__instrument_name',
                     'chartseries__keyword',
                     'chartseries__table',
                     'chartseries__field',
                     'charteventflag__event_type',
                     'charteventflag__instrument_name__instrument_name',
                     )
    
    save_as = True
      
    
    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()
        
    
    def seriesString(self, obj):
        series = [str(series) for series in obj.chartseries_set.all()]
        return '<br/>'.join(series)
    seriesString.short_description = 'Series'
    seriesString.allow_tags = True
    
    def flagsString(self, obj):
        flags = [str(flag) for flag in obj.charteventflag_set.all()]
        return '<br/>'.join(flags)
    flagsString.short_description = 'Event Flags'
    flagsString.allow_tags = True
            
    

class ReportChartForm(forms.ModelForm):
    class Meta:
        model = MSQCdbModels.ReportChart

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(ReportChartForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = HiddenInput()




class ReportChartInline(admin.TabularInline):
    """
    Admin config for ReportChart InLine.
    """
    
    extra = 1
    
    form = ReportChartForm
    
    model = MSQCdbModels.ReportChart
    
    raw_id_fields = ('chart',)

    # define the sortable
    sortable_field_name = "position"
    
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        
        if db_field.name in self.raw_id_fields:
            
            kwargs.pop("request", None)
            fType = db_field.rel.__class__.__name__
            if fType == "ManyToOneRel":
                kwargs['widget'] = VerboseForeignKeyRawIdWidget(db_field.rel, site)
            elif fType == "ManyToManyRel":
                kwargs['widget'] = VerboseManyToManyRawIdWidget(db_field.rel, site)
            return db_field.formfield(**kwargs)
        return super(ReportChartInline, self).formfield_for_dbfield(db_field, **kwargs)
    
    
class ReportAdmin(admin.ModelAdmin):
    """
    Admin config for Report model.
    """

    change_form_template = 'admin/report_change_form.html'

    fieldsets = (
                 (None, {
                         'fields' : (( ('name', 'column_num'),
                                       'description',
                                      )
                                     )
                         }
                  ),
                 )
    
    inlines = [ReportChartInline]

    list_display   = ('name', 'truncatedDescription', 'chartString', 
                      'column_num', 'created_by')

    list_filter = ('created_by', )
    
    search_fields = ('name', 'description', 
                     'reportchart__chart__title')
    
    save_as = True

    

    def chartString(self, obj):
        charts = [chart.chart.html_url() for chart in obj.reportchart_set.all()]
        return '<br/>'.join(charts)
    chartString.short_description = 'Charts'
    chartString.allow_tags = True
    


    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        obj.save()
        
    def truncatedDescription(self, obj):
        lines = wrap(obj.description, 200).split('\n')
        lines = [line[:200] for line in lines]
        return '<br/>'.join(lines)
    truncatedDescription.short_description = 'Description'
    truncatedDescription.allow_tags = True


    

## Register admin panels
admin.site.register(MSQCdbModels.EventLog, EventLogAdmin)
admin.site.register(MSQCdbModels.Sample, SampleAdmin)
admin.site.register(MSQCdbModels.Chart, ChartAdmin)
admin.site.register(MSQCdbModels.Report, ReportAdmin)