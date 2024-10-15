from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')



urlpatterns = [
    # path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
]
