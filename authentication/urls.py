from django.urls import path,include
from . import views
urlpatterns = [
    path('Signup',views.Signup,name="Signup"),
    #path('Login',views.login,name="Login"),
    #path('Logout',views.LogoutView.as_view(template_name='authentication/logout.html'),name="Logout"),
]