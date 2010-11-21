from django.conf.urls.defaults import *

urlpatterns = patterns('kifur.kifu_users.views',
    (r'^user/(?P<user_id>\d+)/$', 'user_profile_from_id'),
    (r'^user/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'user_profile'),
)