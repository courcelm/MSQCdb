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
This module generates view to display information contained in the database.
"""


# Import standard libraries


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
def chartView(request, chartId):
    """
    This function prepares the Context to display the metrics and Event using
    the Highstock JavaScript plotting library. 
    """
    
    chartObject = MSQCdbModels.Chart.objects.get(pk=chartId)
    
    series = chartObject.chartseries_set.all()

    q_outer_object = Q()

    
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
        
    
    chart_data_link = '/MSQCdb/chartDataJSON'
    t = loader.get_template('chart.html')
    c = Context({ 'chart_data_link': chart_data_link, 
                 'chartObject': chartObject, 'series': series, 
                 'events': events,  'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))




@login_required
def chartDataJSON(request, seriesId):
    """
    This function generates a JSON output of data to generate a chart using the 
    Highstock JavaScript plotting library.
    """
    
    seriesObject = MSQCdbModels.ChartSeries.objects.get(pk=seriesId)
    
    m = MSQCdbModels.models.get_model('MSQCdb_app', seriesObject.table)
    o = m.objects.all()
    
    if seriesObject.instrument_name is not None:
        o = o.filter(sample__instrument_name=seriesObject.instrument_name)
        
    if seriesObject.keyword is not None:
        o = o.filter(sample__raw_file__contains=seriesObject.keyword)
        
    
    o = o.order_by('sample__experimentdate')
    o = o.extra(select={'chartValue': seriesObject.field})

    callback = request.GET.get('callback', '')  # For javascript getJSON
    t = loader.get_template('json.html')
    c = Context({ 'callback': callback, 'objects': o})
    
    return HttpResponse(t.render(c), mimetype='application/json')
    



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





    
