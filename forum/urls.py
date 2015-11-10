from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name = "landing"),
    url(r'^main$', views.main, name = "main"),
    url(r'^about$', views.about, name = "about"),
    url(r'^idea/(?P<pk>[0-9]+)/$', views.idea_detail, name='idea_detail'),
    url(r'^new_idea/', views.new_idea, name='new_idea'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.comment_add, name = "comment_add"),
    url(r'^signup$', views.signup, name = "signup"),
    url(r'^thankyou/(?P<pk>[0-9]+)/$', views.thankyou, name = "thankyou"),
]