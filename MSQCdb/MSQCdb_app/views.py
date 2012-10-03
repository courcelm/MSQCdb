# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from MSQCdb.MSQCdb_app.models import *
from django.conf import settings
import time


def listEventLog(request):
    
    events = EventLog.objects.all()
    t = loader.get_template('events.html')
    c = Context({ 'events': events})
    return HttpResponse(t.render(c))





def chartView(request):
    
    events = EventLog.objects.all()
    chart_data_link = '/MSQCdb/chartDataJSON?'
    t = loader.get_template('chart.html')
    c = Context({ 'chart_data_link': chart_data_link, 'events': events,  'MEDIA_URL': settings.MEDIA_URL})
    return HttpResponse(t.render(c))




def chartDataJSON(request):
    
    strTmp = '[\n'    
    objects = MetadataOverviewPositivePolarity.objects.all().order_by('metadata__experimentdate')
    
    for obj in objects:
        epoch = int(time.mktime(obj.metadata.experimentdate.timetuple())*1000)
        strTmp += '[%s,%s],\n' % (epoch, obj.multipole_0_offset_v)
    
    strTmp = strTmp.rstrip('\n')
    strTmp = strTmp.rstrip(',')
    strTmp += '\n]\n'
    
    
    callback = request.GET.get('callback', '')  # For javascript getJSON
    response = callback + '(' + strTmp + ');'
    return HttpResponse(response, mimetype="application/json")

