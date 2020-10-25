from django.conf.urls import url
from .import views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.homepage, name= 'homepage'),
    url(r'^search/', views.search_results, name='search_project'),
    url(r'^profile/',views.profile, name = "profile"),
    url(r'^post_project/',views.post_project, name = "post_project"),

    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)