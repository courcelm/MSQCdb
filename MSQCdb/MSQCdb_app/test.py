from MSQCdb.MSQCdb_app.models import *
from django.db.models import Q
import sys


#print models.get_models()
#print models.get_apps()


for obj in Report.objects.all():
    charts = [str(chart.chart) for chart in obj.reportchart_set.all()]
    print charts
sys.exit()

reportObject = Report.objects.get(pk=1)
    
print reportObject.column_num
divList = []
for i in range(reportObject.column_num):
    print i
    divList.append(i)

sys.exit()

s = Sample.objects.all()[0]
m = s.metadataoverview_set.all()[0]

sys.exit()

filtersEvent = []
        
        
# "Adding" Q objects in Django
# Ref: http://bradmontgomery.blogspot.ca/2009/06/adding-q-objects-in-django.html

q_object = Q()
for flag_filter in Chart.objects.all()[0].charteventflag_set.all():
    
    q_object.add(Q(instrument_name=flag_filter.instrument_name), Q.OR)
            

events = EventLog.objects.all().filter(q_object)
print events
sys.exit()



c = Chart.objects.all()[0]
q_object = Q()

if c.charteventflag_set is not None:
        for flag_filter in c.charteventflag_set.all():
            print flag_filter.instrument_name
            q_object.add(Q(instrument_name=flag_filter.instrument_name), Q.OR)
            
            
events = EventLog.objects.all().filter(q_object)
print events
sys.exit()

print c
for series in c.chartseries_set.all():
    print series
    print series.name
sys.exit()

from django.db.models import get_app, get_models

app = get_app('MSQCdb_app')
print app
for model in get_models(app):
    
    print model
#models.


print Sample._meta.get_all_field_names()
for field in MetaTuneFileValue._meta.fields:
    print field.name
    print field.verbose_name
    print field.get_internal_type()
sys.exit()




print models.get_model('MSQCdb_app', 'Sample')
#print models.get_model('MSQCdb_app', 'Sample').__dict__['experimentdate']

s = Sample.objects.all()[0]
print s.__dict__['experimentdate']

s =  Sample.objects.extra(select={'is_adult': "experimentdate"})
for o in s :
    print o.is_adult
    print 'hi'
    print o.experimentdate 



#from django.contrib.contenttypes.models import ContentType
#
#for ct in ContentType.objects.all():
#    m = ct.model_class()
#    print "%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count())



