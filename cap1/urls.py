from django.urls import path, re_path, include
from . import views
from .admin import admin
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register('users', views.UserViewset)
router.register('locations', views.LocationViewset)
router.register('trips', views.TripViewSet)







urlpatterns = [
    path('', include(router.urls)),
    path("signup/", views.SignUpViewset.as_view(), name='signup'),
    path("login/", views.LoginViewset.as_view(), name='login'),
    path("tripcreate/", views.TripCreateViewSet.as_view(), name='trip' ),
    path("mytrips/", views.UserTripsViewSet.as_view(), name='mytrips'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify')
    
    # path('admin/', admin.site.urls)
]
