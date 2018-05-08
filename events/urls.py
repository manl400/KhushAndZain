from django.conf.urls import url, include
from django.views.generic import DetailView

from . import views
from events.models import Event

urlpatterns = [
    url(r'^$', views.events, name='events'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Event, template_name = "events/event.html"))
]