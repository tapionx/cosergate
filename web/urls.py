from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^login', views.cosergate_login, name='login'),
	url(r'^logout', views.cosergate_logout, name='logout'),
	url(r'^signup', views.cosergate_signup, name='signup'),
	url(r'^home', views.home, name='home'),
	url(r'^account', views.account, name='account')
)
