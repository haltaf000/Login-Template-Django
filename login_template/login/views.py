from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.http import Http404
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

def home(request):
      return render(request, "login/home.html")


@login_required
def index(request):
      context = {"name": request.user}
      return render(request, "login/index.html", context)

def logout_request(request):
      logout(request)
      return render(request, 'login/home.html')
  
class SignUp(CreateView):
      form_class = UserCreationForm
      success_url = reverse_lazy("login")
      template_name = "registration/signup.html"
