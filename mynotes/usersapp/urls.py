from django.urls import path, include
from django.contrib.auth import views as auth_views
from usersapp import views


urlpatterns =[
	path('accounts/', include('django.contrib.auth.urls')),
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
	path('register/', views.register, name='register'),
]

'''
La ligne path('accounts/', include('django.contrib.auth.urls')) ci-dessus ajoute en réalité les lignes suivantes :

accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
1
accounts/ login/ [name='login']
2
accounts/ logout/ [name='logout']
3
accounts/ password_change/ [name='password_change']
4
accounts/ password_change/done/ [name='password_change_done']
5
accounts/ password_reset/ [name='password_reset']
6
accounts/ password_reset/done/ [name='password_reset_done']
7
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
8
accounts/ reset/done/ [name='password_reset_complete']


'''
