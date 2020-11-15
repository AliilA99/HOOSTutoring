from django.shortcuts import render, redirect
from django.db import connection
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView, UpdateView
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_date
from Home.models import User, Creates, Session
from django.contrib import messages
import datetime



class SessionForm(ModelForm):
	class Meta:
		model = Session
		fields = ['study_area', 'capacity', 'location', 'date', 'time', 'description']

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['computingid', 'name_first', 'name_last']


def login(request):
	template_name = 'Home/login.html'
	return render(request, template_name)

def session_create(request):
	'''
	template_name = 'Home/session_create.html'
	form1 = UserForm(request.POST or None)
	form2 = SessionForm(request.POST or None)


	if form1.is_valid() and form2.is_valid():
		form1.save()
		form2.save()
		computingid = form1.cleaned_data['computingid']
		sessionid = Session.objects.latest('sessionid').sessionid
		creates = Creates(computingid = computingid, sessionid = sessionid)
		creates.save()
		return redirect('home')
	'''
	template_name = 'Home/session_create.html'

	if request.method == 'GET' and (request.GET['computingid'] is not None and request.GET['computingid'] != ''):
		user_in = False
		for i in User.objects.all():
			if i.computingid == request.GET['computingid']:
				user_in = True
				if i.name_first != request.GET['name_first'] or i.name_last != request.GET['name_last']:
					return render(request, template_name)
					#Redirecting back to create page if it sees it exists AND the names don't match - will implement error later
		if not user_in:
			u = User(computingid=request.GET['computingid'], name_last=request.GET['name_last'],
					 name_first=request.GET['name_first'])
			u.save()
		cur_session_id = Session.objects.latest('sessionid').sessionid + 1
		new_session = Session(sessionid=cur_session_id, study_area=request.GET['study_area'], capacity=request.GET['capacity'], location=request.GET['location'], description=request.GET['description'], time=datetime.datetime.strptime(request.GET['time'], '%H:%M:%S').time(), date=datetime.datetime.strptime(request.GET['date'], "%Y-%m-%d").date())
		new_session.save()
		creates = Creates(computingid=request.GET['computingid'], sessionid = cur_session_id)
		creates.save()

			# If user isn't in, then create a new user object, otherwise don't
		return redirect('home')

	return render(request, template_name)


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
	'''
	if request.method == 'GET':
		if request.GET['login-signup'] == 'login':
			user_in = False
			messages.info(request, 'INVALID LOGIN ATTEMPT')
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
			else:
				u = User(computingid = request.GET['user_id'], name_last = request.GET['l_name'], name_first = request.GET['f_name'])
				u.save();
			# Make ELSE statement to pass through a session var to the other pages AND add it to the DB
			# Redirect back if userid already found in DB, otherwise set session var to user id
			'''
	return render(request,'Home/home.html')

def login(request):
	template_name = 'Home/login.html'
	return render(request, template_name)

