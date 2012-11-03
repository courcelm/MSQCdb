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
from django.contrib.auth.decorators import login_required




# Function definitions  ######################################################
from django.template import Library
register = Library()
@register.filter(expects_localtime=True)
def datetime_to_milliseconds(some_datetime_object):
    timetuple = some_datetime_object.timetuple()
    timestamp = time.mktime(timetuple)
    return '{0:.0f}'.format(timestamp * 1000.0)


@login_required
def chartView(request):
    """
    This function prepares the Context to display the metrics and Event using
    the Highstock JavaScript plotting library. 
    """
    
    events = EventLog.objects.all()
    #for event in events:
    #    event.datetime = datetime_to_milliseconds(event.datetime)
    chart_data_link = '/MSQCdb/chartDataJSON?'
    t = loader.get_template('chart.html')
    c = Context({ 'chart_data_link': chart_data_link, 'events': events,  'MEDIA_URL': settings.MEDIA_URL})
    
    return HttpResponse(t.render(c))



@login_required
def chartDataJSON(request):
    """
    This function generates a JSON output of data to generate a chart using the 
    Highstock JavaScript plotting library.
    """
    
    objects = ReportSpectrumCount.objects.all().order_by('sample__experimentdate')

    callback = request.GET.get('callback', '')  # For javascript getJSON
    t = loader.get_template('json.html')
    c = Context({ 'callback': callback, 'objects': objects})
    return HttpResponse(t.render(c), mimetype='application/json')
    

