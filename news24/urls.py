from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index, name= "index"),
   path("contact", views.contactsave, name="contact"),
   path("ct", views.contactlist, name="ct"),
   path("upload", views.uploaddata, name="upload"),
   path("sports", views.sports, name="sports"),
   path("fashion", views.fashion, name="fashion"),
   path("tech", views.tech, name="tech"),
   path("news", views.latestnews, name="news"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)