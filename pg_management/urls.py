"""pg_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pg import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
 
    path("", views.home, name='home'),
    path("add/<str:name>", views.add, name='add'),
    path("about", views.about, name='about'),
    path("admdash", views.admdash, name='admdash'),
    path("book/<int:pg_id>", views.book, name='book'),
    path("cities", views.cities, name='cities'),
    path("cities/<str:city>", views.pg_by_cities, name='pg_by_cities'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("booking_details", views.booking_details, name='booking_details'),
    path("booking_details/<int:pg_id>", views.booking_details_pg , name='booking_details_pg'),
    path("Ownerdetailtable", views.Ownerdetailtable, name='Ownerdetailtable'),
    path("pginfo/<int:id>", views.pginfo, name='pginfo'),
    path("pgOwner/", views.pgOwner, name='pgOwner'),
    path("userdetailtable", views.userdetailtable, name='userdetailtable'),
    path("deleteowner/<int:id>", views.deleteowner, name='deleteowner'),
    path("deletestudent/<int:id>", views.deletestudent, name='deletestudent'),

    path('amenity/create', views.ManageAmenities.amenities_create, name='create_amenity'),
    path('amenity/', views.ManageAmenities.amenities_list, name='amenity_list'),
    path('amenity/update/<int:id>/', views.ManageAmenities.amenities_update, name='amenity_update'),
    path('amenity/delete/<int:id>/', views.ManageAmenities.amenities_delete, name='amenity_delete'),
 

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
