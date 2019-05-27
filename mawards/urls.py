from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home_page,name = 'home_page'),
    path('profile/(?P<username>\w+)', views.profile, name='profile'),
    # path('login',views.login,name ='login'),
    # path('logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
    path('upload/', views.upload_project, name='upload_project'),
    path('search/', views.search_results, name='search_results'),
    path('edit', views.edit, name='edit_profile'),
    path('score/(?P<project_id>\d+)',views.score_project, name='score'),
    path('vote/(?P<project_id>\d+)',views.vote, name='vote'),
    path('api/profile/', views.ProfileList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)