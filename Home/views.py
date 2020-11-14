from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView, UpdateView
from django.forms import ModelForm
from .models import Session



class SessionForm(ModelForm):
	class Meta:
		model = Session
		fields = ['sessionid', 'study_area', 'capacity', 'location', 'date', 'time', 'description']


def session_create(request):
	template_name = 'Home/session_create.html'
	form = SessionForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('home')

	return render(request, template_name, {'form':form})


class SessionUpdateView(UpdateView):
	model = Session
	fields = [
		'study_area',
		'capacity',
		'location',
		'date',
		'time',
		'description',
	]
	template_name = 'Home/session_update.html'
	success_url = '/home/'

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
	return render(request,'Home/home.html')

def login(request):
	template_name = 'Home/login.html'
	return render(request, template_name)

