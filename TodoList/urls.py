from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from simpleTodo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleTodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.todolist, name='todo'),
    url(r'^simpleTodo/', include('simpleTodo.urls')),
)
