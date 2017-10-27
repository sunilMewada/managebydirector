from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/$',views.projects, name='projects'),
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^projectDetail/$',views.projectDetail, name='projectDetail'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
]
