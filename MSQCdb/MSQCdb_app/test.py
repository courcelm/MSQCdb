from MSQCdb.MSQCdb_app.models import *
import sys


#print models.get_models()
#print models.get_apps()





c = Chart.objects.all()[0]
if c.charteventflag_set is not None:
        for flag_filter in c.charteventflag_set.all():
            print flag_filter.instrument_name
            events = EventLog.objects.all().filter(instrument_name=flag_filter.instrument_name)
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



