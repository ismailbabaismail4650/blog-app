from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit  import FormView, UpdateView
from django.views.generic import DetailView,CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LoginView
from .forms import SingUpForm, EditProfileForm,PasswordChangingForm,ProfileForm
from base.models import Profile


# Create your views here.
class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





class EditProfilePage(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/user_bio.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfilePage(DetailView):
    model = Profile
    template_name ='registration/user_profile.html'


    def get_context_data (self, *args, **kwargs):
        context = super(ProfilePage, self).get_context_data()
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context ["page_user"] = page_user
        return context


class ChangePassword(PasswordChangeView):
    template_name = 'registration/change-password.html'
    form_class  = PasswordChangingForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("logout") 


    
    
class MyloginViews(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class Registerpage(FormView):
    template_name = 'registration/register.html'
    form_class  = SingUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        user =form.save()
        if user is not None:
            login(self.request, user)
        return super(Registerpage, self).form_valid(form)
    
    def get(self, *args,  **kwargs ):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(Registerpage, self).get(*args, **kwargs)
    

def Mylogout (request):
    logout(request)
    return redirect('login')

class Editpage(UpdateView):
    template_name = 'registration/edit_profile.html'
    form_class  = EditProfileForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home') 

    def get_object(self):
        return self.request.user

   
