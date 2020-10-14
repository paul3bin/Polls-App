from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='polls'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]