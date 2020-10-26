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
    url(r'^project/<int:id>', views.view_project,name="project" ),

    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)