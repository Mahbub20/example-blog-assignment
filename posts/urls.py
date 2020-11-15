from django.urls import path
from posts.views import post_details,posts

app_name = 'posts'

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:post_id>', post_details, name='post_details'),
]
