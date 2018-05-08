
from django.conf.urls import include, url
from django.views.generic import DetailView, ListView
from . import views
from feed.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="feed/feed.html"), {'navbar': 'feed'}, name='feed' ),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name = "feed/post.html")),
    url(r'^getfeed/$', views.getfeed, name="getfeed")
]
