from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout

from blog_engine.views import (PostList,
                               PostCreate,
                               PostDetails,
                               Login)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PostList.as_view(), name="main"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', logout, {'next_page': 'main'}, name="logout"),

    url(r'^posts/create/$', PostCreate.as_view(), name="post_create"),
    url(r'^posts/(?P<post_id>\d+)/$', PostDetails.as_view(), name="post_details"),

    url(r'^admin/', include(admin.site.urls)),
)
