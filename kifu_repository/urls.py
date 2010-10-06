from django.conf.urls.defaults import *

urlpatterns = patterns('kifur.kifu_repository.views',
    (r'^$', 'index'),
    (r'^kifu/$', 'kifu_index'),
    (r'^kifu/add/$', 'kifu_add'),
    (r'^kifu/edit/(?P<kifu_id>\d+)/$', 'kifu_edit'),
    (r'^kifu/(?P<kifu_id>\d+)/$', 'kifu_detail'),
    (r'^player/(?P<player_id>\d+)/$', 'player_detail'),
)