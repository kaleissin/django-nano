from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('nano.privmsg.views',
    url(r'^add$',          'add_pm', name='add_pm'),
    url(r'^(?P<msgid>[1-9][0-9]*)/archive$', 'move_to_archive', name='archive_pm'),
    url(r'^(?P<msgid>[1-9][0-9]*)/delete$', 'delete', name='delete_pm'),
    #url(r'^(?:(?P<action>(archive|sent))/?)?$', 'show_pms', name='show_pms'),
    url(r'^archive/$', 'show_pms', {u'action': u'archive'}, name='show_archived_pms'),
    url(r'^sent/$', 'show_pms', {u'action': u'sent'}, name='show_sent_pms'),
    url(r'^$', 'show_pms', {u'action': u'received'}, name='show_pms'),
)
