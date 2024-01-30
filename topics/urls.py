# blog_app/urls.py
from django.urls import path
from .views import home, topic_list, topic_detail, topic_create, topic_update, topic_delete

urlpatterns = [
   path('', home, name='home'),
   path('topics/', topic_list, name='topics_list'),  
   path('topics/<int:pk>/', topic_detail, name='topic_detail'),
   path('topics/create', topic_create, name='topic_create'),
   path('topics/<int:pk>/update/', topic_update, name='topic_update'),
   path('topics/<int:pk>/delete/', topic_delete, name='topic_delete'),

]

