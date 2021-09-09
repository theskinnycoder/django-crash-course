
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm
