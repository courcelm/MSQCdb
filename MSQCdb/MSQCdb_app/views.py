## Copyright 2012 Mathieu Courcelles
## Mike Tyers's lab / IRIC / Universite de Montreal 
from collections import OrderedDict

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
This module generates view to display information contained in the database.
"""


# Import standard libraries
from datetime import datetime, timedelta, date
import numpy as np


# Import Django related libraries
from django.conf import settings
from django.contrib.auth.decorators import login_required
import django.db.models
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader, Context

# Import project libraries
import MSQCdb.MSQCdb_app.models as MSQCdbModels



# Function definitions  ######################################################


@login_required
def chartView(request, chartId, position):
    """
    This function prepares the Context to display the metrics and Event using
    the Highstock JavaScript plotting library. 
    """
    
    chartObject = MSQCdbModels.Chart.objects.get(pk=chartId)
    
    
    if chartObject.chart_type == 'Timeline':
        return timelineView(request, chartObject, position)
    else:
        return histoView(request, chartObject, position)
    

@login_required
def timelineView(request, chartObject, position):
    """
    This function prepares the Context to display the metrics and Event using
    the Highstock JavaScript plotting library. 
    """
    
    
    series = chartObject.chartseries_set.all()

    q_outer_object = Q()

    events = []
    
    header = True 
    if request.GET.get('header') == 'False':
        header = False
    

    
    if chartObject.charteventflag_set is not None:
        
        # "Adding" Q objects in Django
        # Ref: http://bradmontgomery.blogspot.ca/2009/06/adding-q-objects-in-django.html

        
        for flag_filter in chartObject.charteventflag_set.all():
            
            q_inner_object = Q()
            if flag_filter.instrument_name is not None:
                q_inner_object.add(Q(instrument_name=flag_filter.instrument_name), Q.AND)
                                   
            if flag_filter.event_type is not None:
                q_inner_object.add(Q(event_type=flag_filter.event_type), Q.AND)
            
            q_outer_object.add(q_inner_object, Q.OR)
            
            
            events = MSQCdbModels.EventLog.objects.all().filter(q_outer_object)
        
    
    chart_data_link = '/MSQCdb/timelineDataJSON'
    t = loader.get_template('timeline.html')
    c = Context({ 'chart_data_link': chart_data_link, 'position': position,
                 'chartObject': chartObject, 'series': series,
                 'header': header,
                 'events': events,
                 'plotMeanStd': chartObject.plotMeanStd,  
                 'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))



@login_required
def histoView(request, chartObject, position):
    """
    This function prepares the Context to display the histogram using
    the Highstock JavaScript plotting library. 
    """
    
    series = chartObject.chartseries_set.all()

    header = True 
    if request.GET.get('header') == 'False':
        header = False
    
     
    
    bin_labels = np.arange(chartObject.histo_min, chartObject.histo_max, chartObject.bin_width)
    
    chart_data_link = '/MSQCdb/histoDataJSON'
    t = loader.get_template('histogram.html')
    c = Context({ 'chart_data_link': chart_data_link, 'position': position,
                 'chartObject': chartObject, 'series': series,
                 'header': header,
                 'bin_width': chartObject.bin_width,
                 'bin_labels': bin_labels,
                 'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))



def chartDataValues(seriesId):
    """
    This function prepares objects to generate a chart using the 
    Highstock JavaScript plotting library.
    """
    
    seriesObject = MSQCdbModels.ChartSeries.objects.get(pk=seriesId)
    
    m = MSQCdbModels.models.get_model('MSQCdb_app', seriesObject.table)
    o = m.objects.all()
    
    if seriesObject.instrument_name is not None:
        o = o.filter(sample__instrument_name=seriesObject.instrument_name)
        
    if seriesObject.keyword is not None:
        o = o.filter(sample__raw_file__contains=seriesObject.keyword)
        
    o = o.extra(select={'chartValue': seriesObject.field})
    
    return o, seriesObject.chart


@login_required
def timelineDataJSON(request, seriesId):
    """
    This function generates a JSON output of data to generate a chart using the 
    Highstock JavaScript plotting library.
    """

    o, chart = chartDataValues(seriesId)
    o = o.order_by('sample__experimentdate')

    callback = request.GET.get('callback', '')  # For javascript getJSON
    t = loader.get_template('timeline_json.html')
    c = Context({ 'callback': callback, 'objects': o})
    
    return HttpResponse(t.render(c), mimetype='application/json')


@login_required
def histoDataJSON(request, seriesId):
    """
    This function generates a JSON output of data to generate a chart using the 
    Highstock JavaScript plotting library.
    """

    o, chart = chartDataValues(seriesId)
    
    values_list = []
    for obj in o:
        values_list.append(obj.chartValue)
    
    
    bin_values, bin_labels = np.histogram(values_list, bins=np.arange(chart.histo_min,
                                                                      chart.histo_max, 
                                                                      chart.bin_width))
    

    callback = request.GET.get('callback', '')  # For javascript getJSON
    t = loader.get_template('histo_json.html')
    c = Context({ 'callback': callback, 'bin_values': bin_values,
                  
                 })
    
    return HttpResponse(t.render(c), mimetype='application/json')


@login_required
def reservationJSON(request):
    """
    This function generates a JSON output of data to generate 
    reservation calendar.
    """
    how_many_days = 180
    reservations = MSQCdbModels.Reservation.objects.filter(\
                        scheduled_start_date__gte=datetime.now()-timedelta(days=how_many_days))
    
    t = loader.get_template('reservation_json.html')
    c = Context({ 'reservations': reservations})
    
    return HttpResponse(t.render(c), mimetype='application/json')


@login_required
def reservationCalendar(request):
    """
    This function generates a reservation calendar.
    """
    how_many_days = 180
    reservationInstruments = MSQCdbModels.Reservation.objects.filter(\
                        scheduled_start_date__gte=datetime.now()-timedelta(days=how_many_days))\
                        .values('instrument__pk', 'instrument__instrument_name').distinct()
    
    t = loader.get_template('reservation_calendar.html')
    c = Context({'reservationInstruments': reservationInstruments})
    
    return HttpResponse(t.render(c), mimetype='text/html')




@login_required
def reservationPerUser(request, year):
    """
    This function generates report of instrument usage for each user.
    """
    
    year = int(year)
    
    start = date(year, 1, 1)
    stop = date(year, 12, 31)
    
    reservations = MSQCdbModels.Reservation.objects.filter(scheduled_start_date__gte=start, 
                                                           scheduled_start_date__lte=stop)
    
    instruments = dict()
    usage = dict()
    
    
    for reservation in reservations:
        
        user = reservation.created_by.get_full_name()
        instrument = reservation.instrument.instrument_name
        
        instruments[instrument] = 1


        if user not in usage:        
            usage[user] = dict()
            usage[user]['Total'] = 0
        
        if instrument not in usage[user]:
            usage[user][instrument] = 0
        
        days = (reservation.scheduled_end_date - reservation.scheduled_start_date).days + 1
        
        usage[user][instrument] +=  days
        usage[user]['Total'] +=  days
        
    usage = OrderedDict(sorted(usage.items(), key=lambda t: t[0]))
    instruments = sorted(instruments.keys())
    instruments.append('Total')
        
    t = loader.get_template('reservation_peruser.html')
    c = Context({'instruments': instruments, 'usage': usage,
                 'year': year})
    
    return HttpResponse(t.render(c), mimetype='text/html')



def fieldOptions(request, modelName):
    """
    View that generates the fields option in the chart admin page.
    """
    

    model =  django.db.models.get_model('MSQCdb_app', modelName)

    fields =  [field for field in model._meta.fields if 
               field.get_internal_type().startswith('Int') or 
               field.get_internal_type().startswith('Float') ]
    
    t = loader.get_template('fieldOptions.html')
    c = Context({ 'fields': fields})
    
    
    return HttpResponse(t.render(c))




@login_required
def reportView(request, reportId):
    """
    This function prepares the Context to display multiple charts
    to generates a report. 
    """
    
    reportObject = MSQCdbModels.Report.objects.get(pk=reportId)
    charts = reportObject.reportchart_set.all()
    
    header = True 
    if request.GET.get('header') == 'False':
        header = False
    
    t = loader.get_template('report.html')
    c = Context({ 
                 'columns': reportObject.column_num, 'charts': charts,
                 'header': header,
                 'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))