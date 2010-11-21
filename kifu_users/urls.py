from django.conf.urls.defaults import *

urlpatterns = patterns('kifur.kifu_users.views',
    (r'^user/(?P<user_id>\d+)/$', 'user_profile'),
)