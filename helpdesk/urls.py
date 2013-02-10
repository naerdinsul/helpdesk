from django.conf.urls import patterns, include, url

urlpatterns = patterns('helpdesk.views',

	url( r'^thanks/$', 'thanks' ),
	url( r'^$', 'newticket' ),

)
