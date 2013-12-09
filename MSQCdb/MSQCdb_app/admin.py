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
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import get_app, get_models
from django.utils.text import wrap

import reversion


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
    
    save_as = True
    
    search_fields = ('name', 'description')
    
    
    # Save the creator of the object
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        if request.user.is_superuser or obj.created_by == request.user:
            obj.save()
        else:
            messages.error(request, '%s is not allowed to modify this event. Ignore message below.'  
                                   % (request.user.username))
        
    
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
    
    
    fieldsets = (
        (None, {
            'fields': ('title', 'yAxisTitle', 'chart_type')
        }),
        ('Timeline options', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('plotMeanStd',)
        }),
        ('Histogram options', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('histo_min', 'histo_max', 'bin_width')
        }),
    )
    
    
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
        
        if request.user.is_superuser or request.user.groups.filter(name='editor').exists():            
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
            
        if request.user.is_superuser or request.user.groups.filter(name='editor').exists():            
            obj.save()
            
        
    def truncatedDescription(self, obj):
        lines = wrap(obj.description, 200).split('\n')
        lines = [line[:200] for line in lines]
        return '<br/>'.join(lines)
    truncatedDescription.short_description = 'Description'
    truncatedDescription.allow_tags = True



class ReservationForm(forms.ModelForm):
    """
    Reservation form to clean scheduled dates.
    """
    
    def __init__(self, *args,**kwargs):
        super (ReservationForm,self ).__init__(*args,**kwargs) # populates the post
        if 'instrument' in self.fields:
            self.fields['instrument'].queryset = MSQCdbModels.Instrument.objects.filter(active=True)
    
    
    class Meta:

        model = MSQCdbModels.Reservation


    def clean(self):
        """
        Check that end date is not before start date.
        """
        
        if 'scheduled_start_date' in self.cleaned_data and \
            'scheduled_end_date' in self.cleaned_data and \
            self.cleaned_data['scheduled_end_date'] < self.cleaned_data['scheduled_start_date']:
            msg = u"Scheduled end date is earlier than start date."
            raise forms.ValidationError(msg)
 
        return self.cleaned_data



class ReservationAdmin(reversion.VersionAdmin):
    """
    Admin config for Reservation model.
    """
    
    actions=['really_delete_selected']
    
    change_list_template = 'admin/MSQCdb_app/reservation/change_list.html'
    
    datetime = 'modification_date'
    
    form = ReservationForm
    
    list_display   = ('pk','created_by', 'modification_date', 'instrument', 
                      'time_needed', 'sample_count', 'comment',
                      'prefered_start_date', 'scheduled_start_date',
                      'scheduled_end_date', 'status')
    
    

    list_filter = ('created_by', 'instrument', 'status')
    
    list_per_page = 30
    
    search_fields = ('comment',)
    
    
    def delete_model(self, request, obj):
        """
        Checks permission before deleting a reservation.
        """
        
        if request.user.is_superuser or obj.created_by == request.user or \
           request.user.groups.filter(name='ms_scheduling').count() == 1:
            obj.delete()
        else:
            self.message_user(request, "Permission denied. Reservation was not deleted.",
                              level=messages.ERROR)
    
    
    def get_actions(self, request):
        """
        From http://stackoverflow.com/questions/1471909/django-model-delete-not-triggered
        """
        
        actions = super(ReservationAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


    def really_delete_selected(self, request, queryset):
        """
        Limit deletion of multiple reservations by permission
        """
        
        count = 0
        for obj in queryset:
            if request.user.is_superuser or obj.created_by == request.user or \
               request.user.groups.filter(name='ms_scheduling').count() == 1:
                obj.delete()
                count += 1

        message_bit = "%s reservation entries were" % count
        self.message_user(request, "%s successfully deleted." % message_bit)
    really_delete_selected.short_description = "Delete selected reservations"

    
    def get_changelist_form(self, request, **kwargs):
        """
        Custom form for cleaning data.
        """
        
        return ReservationForm
    
    
    def get_readonly_fields(self, request, obj=None):
        """
        This method sets some fields read only based on user group. 
        """
                
        readonly_fields = list(self.readonly_fields)
        
        if not request.user.is_superuser and \
           not request.user.groups.filter(name='ms_scheduling').count() == 1:
            readonly_fields.extend(['scheduled_start_date'])
            readonly_fields.extend(['scheduled_end_date'])
    
        return readonly_fields
    
    
    def changelist_view(self, request, extra_context=None):
        """
        Limits user that can change scheduled dates
        """
        
        self.list_editable = ('status', ) # Reset
        # Bug fix - Some how this vaue stay set between users sessions
        
        if request.user.is_superuser or \
           request.user.groups.filter(name='ms_scheduling').count() == 1:
            self.list_editable = ('status', 'scheduled_start_date', 'scheduled_end_date')
        
        return super(ReservationAdmin, self).changelist_view(request, extra_context)
    
    
    def save_model(self, request, obj, form, change):

        ## Store the obj creator
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            
        # Send email to lab manager to notify reservation change
        # Mcafee viruscan block email
        if request.user.pk != settings.SCHEDULER_USERID:
            subject, from_email, to = 'New/Modification MS instrument reservation', \
                                      'msqcdb@gmail.com', settings.SCHEDULER_EMAIL
            text_content = 'New/Modification MS instrument reservation'
            html_content = '<html><body>Reservation id: %s (%s)<br /><br /> Created by: %s<br/><br/>Modified at: %s<br/>%s</body></html>' %\
                           (obj.pk, obj.instrument.instrument_name, obj.created_by, obj.modification_date, form.as_p())
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        
        # Send email to user if someone else modifies your reservation
        # It should be limited to user in the ms_scheduling group
        if request.user != obj.created_by:
            subject, from_email, to = 'Modification to your MS instrument reservation', \
                                      'msqcdb@gmail.com', request.user.email
            text_content = 'Modification to your MS instrument reservation'
            html_content = '<html><body>Reservation id: %s (%s)<br /><br /> Created by: %s<br/><br/>Modified at: %s<br/>%s</body></html>' %\
                           (obj.pk, obj.instrument.instrument_name, obj.created_by, obj.modification_date, form.as_p())
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            
        # Alert next user if running late or completed
        if obj.status == 3 or obj.status == 4:
            next_reservations = MSQCdbModels.Reservation.objects.exclude(pk=obj.pk)\
                                                                        .filter(instrument=obj.instrument, 
                                                                        scheduled_start_date__gte=obj.scheduled_end_date)\
                                                                        .order_by('scheduled_start_date')
            
            if next_reservations.count() > 0:
                next_reservation_email = next_reservations[0].created_by.email
                
                subject, from_email, to = 'MS instrument status update', \
                                      'msqcdb@gmail.com', next_reservation_email
                text_content = 'MS instrument status update'
                html_content = '<html><body>Reservation id: %s (%s)<br /><br /> Created by: %s<br/><br/>Modified at: %s<br/>%s</body></html>' %\
                           (obj.pk, obj.instrument.instrument_name, obj.created_by, obj.modification_date, form.as_p())
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            
        
        if request.user.is_superuser or obj.created_by == request.user or \
            request.user.groups.filter(name='ms_scheduling').count() == 1:
            obj.save()
        else:
            messages.error(request, '%s is not allowed to modify this reservation.'  
                                   % (request.user.username))
    

## Register admin panels
admin.site.register(MSQCdbModels.EventLog, EventLogAdmin)
admin.site.register(MSQCdbModels.Sample, SampleAdmin)
admin.site.register(MSQCdbModels.Chart, ChartAdmin)
admin.site.register(MSQCdbModels.Report, ReportAdmin)
admin.site.register(MSQCdbModels.Reservation, ReservationAdmin)
admin.site.register(MSQCdbModels.Instrument)