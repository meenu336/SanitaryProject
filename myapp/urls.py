
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('',views.index,name="index"),
   path('registration/',views.registration,name="registration"),
   path('login/',views.user_login,name="login"),
   path('home/',views.home,name="home"),
   path('logout/', views.logout_view, name='logout'),

   path('accounts/login/',views.user_login,name="login"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
  
]