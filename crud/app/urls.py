from .views import ProductView,SeenView,DelView, UpdateView, SignupView, LoginView, logoutView
from django.urls import path

urlpatterns = [
    path('prodfill/', ProductView, name='prodfill'),
    path('seen/', SeenView, name='seen'),
    path('delview/<int:id>/',DelView, name='delview' ),
    path('update/<int:id>/', UpdateView, name='update'),
    path('signup/', SignupView, name='signup'),
    path('login/', LoginView, name='login'),
    path('logout/',logoutView, name='logout' )
]