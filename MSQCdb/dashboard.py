"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'MSQCdb.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        
        # append a group for "Administration" & "Applications"
#        self.children.append(modules.Group(
#            _('Group: Administration & Applications'),
#            column=1,
#            collapsible=True,
#            children = [
#                modules.AppList(
#                    _('Administration'),
#                    column=1,
#                    collapsible=False,
#                    models=('django.contrib.*',),
#                ),
#                modules.AppList(
#                    _('Applications'),
#                    column=1,
#                    css_classes=('collapse closed',),
#                    exclude=('django.contrib.*',),
#                )
#            ]
#        ))
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            collapsible=True,
            column=2,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))
        
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administration'),
            column=2,
            #collapsible=False,
            models=('django.contrib.*',),
        ))
        
        # append another link list module for "support".
#        self.children.append(modules.LinkList(
#            _('Media Management'),
#            column=2,
#            pre_content= 'Tsetetets1',
#            content= 'Tsetetets2',
#            post_content= 'Tsetetets3',
#            children=[
#                {
#                    'title': _('FileBrowser'),
#                    'url': '/admin/filebrowser/browse/',
#                    'external': False,
#                },
#            ]
#        ))
        
        
        # append another link list module for "Quick start".
        self.children.append(modules.LinkList(
            _('Quick start'),
            column=1,
            post_content='<ul class="grp-listing-small">\
                          <li class="grp-row">\
                          <span style="font-weight: bold;">Charts</span><br />\
                          Plot the history of one or multiple performance metrics\
                          (chromatography, ion source, MS & MS/MS sampling, \
                          identifications) or MS instrument meta data (calibration\
                          and tune parameters). Comparison between MS instruments\
                          can be done over here.<br/><br/>\
                          <span style="font-weight: bold;">Event logs</span><br />\
                          Users can log, in this section, date of calibration, \
                          failure (and how it was resolved), maintenance and other\
                          notes related to each MS instrument, LC-system, columns \
                          and auto-sampler. This section should be consulted to \
                          know the state of the instrument before using it to \
                          prevent wasting time. Events can be displayed on \
                          chart as flags.<br/><br/>\
                          <span style="font-weight: bold;">Report</span><br />\
                          Reports are a collection of charts to display \
                          simultaneously multiple metrics about an MS instrument \
                          in order to review its performance.<br/><br/>\
                          <span style="font-weight: bold;">Samples</span><br />\
                          This section lists all the standard samples \
                          (e.g. Promix) that are stored in the database and \
                          available to this application. A daemon searches at \
                          regular intervals for new files, runs the NIST MSCQC \
                          pipeline and stores results in the database. \
                          User can see for each \
                          sample all the performance metrics and meta data \
                          associcated. Only administrators can modify Sample \
                          values.<br/><br/>\
                          <span style="font-weight: bold;">Reservations</span><br />\
                          MS instrument time requirements should be entered in this section.\
                          Platform manager will then schedule each entry. MS instrument\
                          schedule can be consulted in this section.<br/><br/>\
                          </li>\
                          </ul>',

        ))
        
        # append another link list module for "NIST MSQC Documentation".
        self.children.append(modules.LinkList(
            _('NIST MSQC Documentation'),
            column=1,
            post_content='<ul class="grp-listing-small">\
                          <li class="grp-row">\
                          Read NIST MSQC paper to learn more about the\
                          performance metrics available.\
                          </li>\
                          </ul>',
            children=[
                {
                    'title': _('Website'),
                    'url': 'http://peptide.nist.gov/software/nist_msqc_pipeline/NIST_MSQC_Pipeline.html',
                    'external': True,
                },
                {
                    'title': _('MCP paper'),
                    'url': 'http://www.mcponline.org/content/9/2/225.long',
                    'external': True,
                },
            ]
        ))
        
        # append a feed module
#        self.children.append(modules.Feed(
#            _('Latest Django News'),
#            column=2,
#            feed_url='http://www.djangoproject.com/rss/weblog/',
#            limit=5
#        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            #collapsible=False,
            column=3,
        ))

        
        # append another link list module for "Instrument performance report".
        self.children.append(modules.LinkList(
            _('Instrument performance reports'),
            column=2,

            children=[
                {
                    'title': _('LTQ-Orbitrap Elite'),
                    'url': '/MSQCdb/reportView/7',
                    'external': True,
                },
                {
                    'title': _('LTQ-Orbitrap XL'),
                    'url': '/MSQCdb/reportView/3',
                    'external': True,
                },
                {
                    'title': _('Q-Exactive'),
                    'url': '/MSQCdb/reportView/5',
                    'external': True,
                },
                {
                    'title': _('Q-Exactive Plus slot #104'),
                    'url': '/MSQCdb/reportView/13',
                    'external': True,
                },
                {
                    'title': _('Q-Exactive Plus slot #160'),
                    'url': '/MSQCdb/reportView/16',
                    'external': True,
                },
                {
                    'title': _('Orbitrap VS'),
                    'url': '/MSQCdb/reportView/11',
                    'external': True,
                },
                
            ]
        ))
        
