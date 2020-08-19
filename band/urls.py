from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='band-home'),
    path('about/', views.about, name='band-about'),
    path('gallery/', views.gallery, name='band-gallery'),
    path('download/', views.download, name='band-download'),
    path('blog/', views.blog, name='band-blog'),
    path('contact/', views.contact, name='band-contact'),
    path('bookings/', views.booking, name='band-booking'),
]