from django.urls import path
from . import views
from . views import SessionListView, SessionDetailView, SessionUpdateView



urlpatterns = [
	
		path('', views.login, name = 'login'),
		path('home/', views.home, name = 'home'),
		path('sort/', views.sort, name = 'sort'),
		path('create/', views.session_create, name = 'session_create'),
		path('view/', SessionListView.as_view(), name = 'session_view'),
		path('view/<int:pk>', SessionDetailView.as_view(), name = 'session_detail'),
		path('view/<int:pk>/update/', SessionUpdateView.as_view(), name = 'session_update'),
		path('session_delete/', views.session_delete, name = 'session_delete'),


]
