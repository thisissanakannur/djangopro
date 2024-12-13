# from django.urls import path
# from . import views



# urlpatterns = [
#     path('',views.nos,name='safa'),
#     path('add/',views.ipls,name='jeez'),
#     path('login/',views.login,name='login'),
#     path('logout/',views.logout,name='logout'),
# ]

from django.urls import path
from . import views
from.views import send_email_view

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),   # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout page
    path('', views.home, name='home'),  # Protected homepage

    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete_session'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),

    path('send-email/', send_email_view, name='send_email'),
]


