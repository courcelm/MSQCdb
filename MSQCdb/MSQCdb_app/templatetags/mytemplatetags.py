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



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '-')


@register.simple_tag
def get_year():
    return datetime.date.today().year


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


@register.filter(is_safe=True)
def int2color(value):
    
    colors = ['black', 'darkcyan', 'darkgreen', 'darkred', 'darkslateblue',
               'dodgerblue', 'mediumaquamarine', 'mediumvioletred', 'olive', 'slategray',
               'navy', 'teal', 'limegreen', 'lightsteelblue', 'indianred',
               ]
    
    return colors[value % len(colors)]


from django import template
from django.template import resolve_variable
from django.contrib.auth.models import Group


@register.tag()
def ifusergroup(parser, token):
    """ Check to see if the currently logged in user belongs to a specific
    group. Requires the Django authentication contrib app and middleware.

    Usage: {% ifusergroup Admins %} ... {% endifusergroup %}

    """
    try:
        tag, group = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifusergroup' requires 1 argument.")
    nodelist = parser.parse(('endifusergroup',))
    parser.delete_first_token()
    return GroupCheckNode(group, nodelist)


class GroupCheckNode(template.Node):
    def __init__(self, group, nodelist):
        self.group = group
        self.nodelist = nodelist
    def render(self, context):
        user = resolve_variable('user', context)
        if not user.is_authenticated():
            return ''
        try:
            group = Group.objects.get(name=self.group)
        except Group.DoesNotExist:
            return ''
        if group in user.groups.all():
            return self.nodelist.render(context)
        return ''
