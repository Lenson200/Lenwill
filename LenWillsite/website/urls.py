from django.urls import path
from django.conf.urls.static import static
from website import views
urlpatterns = [
    path('',views.index,name="index"),
   
]