from django.conf.urls import url
import views

urlpatterns = [

    url(r'^users$', views.users),
    url(r'^users/add$', views.add),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/(?P<id>\d+)$', views.display),
    url(r'^users/create$', views.create),
    url(r'^changes/(?P<id>\d+)$', views.changes),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^back$', views.back)

]