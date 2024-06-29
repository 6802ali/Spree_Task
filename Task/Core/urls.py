from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Register, UserListView, Login , CreateItem, ItemDetail, ItemList


urlpatterns = [
    path("register/", Register.as_view(), name="register_route"),
    path("Login/", Login.as_view(), name="register_route"),
    path('users/', UserListView.as_view(), name='user-list'),
    path('createitem/', CreateItem.as_view(), name='create-item-route'),
    path('itemlist/', ItemList.as_view(), name='item-list-route'),
    path('<int:pk>', ItemDetail.as_view(), name='item-list-route')
]