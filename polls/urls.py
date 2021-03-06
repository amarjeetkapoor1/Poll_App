
from django.conf.urls import patterns, include, url
from django.contrib import admin

from polls import views



urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    
    url(r'^result_all/$', views.result_all, name='result_all'),
    
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),


)
