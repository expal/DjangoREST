"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from user.views import AuthorViewSet
from user import views

router = DefaultRouter()
router.register('Authors', AuthorViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('generic/retrieve/<int:pk>/', views.AuthorViewSet.as_view()),
    path('generic/update/<int:pk>/', views.AuthorViewSet.as_view()),
    path('generic/update/<int:pk>/', views.ProjectViewSet.as_view()),
    path('generic/create/<int:pk>/', views.ProjectViewSet.as_view()),
    path('generic/retrieve/<int:pk>/', views.ProjectViewSet.as_view()),
    path('generic/destroy/<int:pk>/', views.ProjectViewSet.as_view()),
    path('generic/update/<int:pk>/', views.TODOViewSet.as_view()),
    path('generic/create/<int:pk>/', views.TODOViewSet.as_view()),
    path('generic/retrieve/<int:pk>/', views.TODOViewSet.as_view()),
    path('generic/destroy/<int:pk>/', views.TODOViewSet.as_view())

]
