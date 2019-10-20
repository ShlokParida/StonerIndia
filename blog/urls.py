from django.urls import path
import blog.views
urlpatterns = [
    path('',blog.views.allblogs,name = 'allblog'),
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    ] 
