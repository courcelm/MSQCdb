from django.template import Library
from django.utils.safestring import mark_safe

import datetime
import calendar

register = Library()



@register.filter(expects_localtime=True)
def epoch(value):
    """Convert datetime object into milliseconds from epoch.
    Time is displayed in server time zone.
    
    Add {% load epoch_tag %} to the template and use it like this 
    {{ date_obj|epoch }} 
    
    Code from:
    http://j-syk.com/weblog/2012/08/23/converting-python-datetime-to-epoch-tim
    e-with-django-template-tag/
    """
    if isinstance(value, datetime.datetime):
        return int(calendar.timegm(value.timetuple())*1000)
    return '' #fails silently for non-datetime objects




@register.filter(is_safe=True)
def splitLine(value, lineLength = 30 ):
    """
    Wrap line to a defined length at space between words.
    """
    
    "wrap at first delimiter left of size"  
    wraplines = []
    
    
    line = ''
    for word in value.split(' '):
        if len(line) + len(word) <= lineLength:
            line += word + ' '
        else:
            wraplines.append(line)
            line = word + ' '
    wraplines.append(line)

    return mark_safe('<br />'.join(wraplines))
