## Copyright 2012 Mathieu Courcelles
## Mike Tyers lab / IRIC / Universite de Montreal 

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
import time

# Import Django related libraries
from django.template import loader, Context
from django.http import HttpResponse
from MSQCdb.MSQCdb_app.models import *
from django.conf import settings




# Function definitions  ######################################################

def chartView(request):
    """
    This function prepares the Context to display the metrics and Event using
    the Highstock JavaScript plotting library. 
    """
    
    events = EventLog.objects.all()
    chart_data_link = '/MSQCdb/chartDataJSON?'
    t = loader.get_template('chart.html')
    c = Context({ 'chart_data_link': chart_data_link, 'events': events,  'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))




def chartDataJSON(request):
    """
    This function generates a JSON output of data to generate a chart using the 
    Highstock JavaScript plotting library.
    """
    
    strTmp = '[\n'    
    objects = ReportSpectrumCount.objects.all().order_by('sample__experimentdate')
    
    for obj in objects:
        epoch = int(time.mktime(obj.sample.experimentdate.timetuple())*1000)
        strTmp += '[%s,%s],\n' % (epoch, obj.ms1_scansfull)
    
    strTmp = strTmp.rstrip('\n')
    strTmp = strTmp.rstrip(',')
    strTmp += '\n]\n'
    
    
    callback = request.GET.get('callback', '')  # For javascript getJSON
    response = callback + '(' + strTmp + ');'
    
    return HttpResponse(response, mimetype='application/json')




def listEventLog(request):
    """
    This function prepare the Context to display the EventLog.
    """
    
    events = EventLog.objects.all()
    t = loader.get_template('events.html')
    c = Context({ 'events': events})
    return HttpResponse(t.render(c))





