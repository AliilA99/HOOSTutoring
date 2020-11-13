from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from django.forms import ModelForm
from Home.models import Session, User


class SessionForm(ModelForm):
	class Meta:
		model = Session
		fields = ['sessionid', 'study_area', 'capacity', 'location', 'date', 'time', 'description']


def login(request):
	template_name = 'Home/login.html'
	return render(request, template_name)

def session_create(request):
	template_name = 'Home/session_create.html'
	form = SessionForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('home')

	return render(request, template_name, {'form':form})


class SessionListView(ListView):
	model = Session
	template_name = 'Home/session_view.html'
	context_object_name = 'sessions'
	paginate_by = 3
	ordering = ['sessionid']

	def get_queryset(self):
		return Session.objects.all()

class SessionDetailView(DetailView):
	model = Session
	template_name = 'Home/session_detail.html'

class SessionDeleteView(DeleteView):
	model = Session
	template_name = 'Home/session_delete.html'
	success_url = '/home/'


def home(request):
	if request.method == 'GET':
		if request.GET['login-signup'] == 'login':
			user_in = False
			for i in User.objects.all():
				if i.name_first == request.GET['f_name'] and i.name_last == request.GET['l_name'] and i.computingid == request.GET['user_id']:
					user_in = True
					break
			if not user_in:
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			# Redirect back to last page if info provided isn't in the DB
			# Make an ELSE statmemnt to pass through user id through to other pages
		else:
			user_in = False
			for i in User.objects.all():
				if i.computingid == request.GET['user_id']:
					user_in = True
					break
			if user_in:
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			# Make ELSE statement to pass through a session var to the other pages AND add it to the DB
			# Redirect back if userid already found in DB, otherwise set session var to user id
	return render(request,'Home/home.html')

