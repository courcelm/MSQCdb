from MSQCdb.MSQCdb_app.models import *

print models.get_models()
print models.get_apps()


from django.db.models import get_app, get_models

app = get_app('MSQCdb_app')
print app
for model in get_models(app):
    print model



print Sample._meta.get_all_field_names()


print models.get_model('MSQCdb_app', 'Sample')
#print models.get_model('MSQCdb_app', 'Sample').__dict__['experimentdate']

s = Sample.objects.all()[0]
print s.__dict__['experimentdate']

s =  Sample.objects.extra(select={'is_adult': "experimentdate"})
for o in s :
    print o.is_adult



#from django.contrib.contenttypes.models import ContentType
#
#for ct in ContentType.objects.all():
#    m = ct.model_class()
#    print "%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count())