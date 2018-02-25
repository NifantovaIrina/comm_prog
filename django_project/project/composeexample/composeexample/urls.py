from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from main.views import main, new_note, NoteDelete

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', new_note, name='main'),
    url(r'^delete/(?P<pk>\d+)', NoteDelete.as_view(), name='delete')
]
