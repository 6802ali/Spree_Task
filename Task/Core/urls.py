from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Register, UserListView, Login , CreateItem, ItemDetail, ItemList


urlpatterns = [
    # path("api/token/", TokenObtainPairView.as_view(), name='login'),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # # path("api/user/", UserApi.as_view(), name="user"),
    # path("api/register/", Signup.as_view(), name="register"),
    # path("api/login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register_route"),
    path("Login/", Login.as_view(), name="register_route"),
    path('users/', UserListView.as_view(), name='user-list'),
    path('createitem/', CreateItem.as_view(), name='create-item-route'),
    path('itemlist/', ItemList.as_view(), name='item-list-route'),
    path('<int:pk>', ItemDetail.as_view(), name='item-list-route')
]