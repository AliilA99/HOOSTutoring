from django.urls import path
from . import views
from . views import SessionListView, SessionDetailView, SessionDeleteView, SessionUpdateView



urlpatterns = [
	
		path('', views.login, name = 'login'),
		path('home/', views.home, name = 'home'),
		path('create/', views.session_create, name = 'session_create'),
		path('view/', SessionListView.as_view(), name = 'session_view'),
		path('view/<int:pk>', SessionDetailView.as_view(), name = 'session_detail'),
		path('view/<int:pk>/update/', SessionUpdateView.as_view(), name = 'session_update'),
		path('view/<int:pk>/delete/', SessionDeleteView.as_view(), name = 'session_delete'),

]