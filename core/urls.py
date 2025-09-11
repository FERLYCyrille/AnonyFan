from django.urls import path
from . import views

urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.upload_photo, name='upload_photo'),
    path('view/<uuid:photo_id>/', views.view_links, name='view_links'),
    path('c/<uuid:photo_id>/<str:token>/', views.view_comments, name='view_comments'),  # ✔️ lien plus propre
    path('photo/<uuid:photo_id>/', views.photo_page, name='photo_page'),
]
