from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.homepage, name= 'homepage'),
    url(r'^search/', views.search_results, name='search_project'),
    url(r'^profile/',views.profile, name = "profile"),
    url(r'^update_profile/',views.update_profile, name = "update_profile"),
    url(r'^post_project/',views.post_project, name = "post_project"),
    url(r'^project/(?P<project_id>\d+)', views.view_project,name="project" ),
    url(r'^rating/(?P<project_id>\d+)', views.rating,name="rating" ),
    url(r'^api/profiles/', views.ProfileView.as_view()),
    url(r'^api/projects/', views.ProjectView.as_view()),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)