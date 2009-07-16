from django.conf.urls.defaults import *

from django.views.generic.list_detail import object_list
from models import Storyline

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        {"queryset": Storyline.objects.all(),"template_object_name":"storyline"},
        name="archive"),
)
