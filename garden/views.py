from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Garden
from .forms import CreateGardenForm

# Create your views here.
class CreateGardenView(LoginRequiredMixin, CreateView):
    form_class = CreateGardenForm
    success_url = reverse_lazy('gardenlistview')
    template_name = 'gardens/create.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        try:
            newGarden = form.save(commit=False)
            newGarden.owner = self.request.user
            newGarden.save()
            return HttpResponseRedirect(self.success_url)
        except ValueError as e:
            return render(self.request, self.template_name, {"errormessage": "Something went wrong. Note: Length and Width cannot be longer than 30 meters each", "form": self.form_class})

class GardenListView(LoginRequiredMixin, TemplateView):
    template_name = 'gardens/list.html'
    def get(self, request, *args, **kwargs):
        currentUser = self.request.user
        userGardens = Garden.objects.filter(owner=currentUser)
        return render(self.request, self.template_name, {"gardens": userGardens})

class GardenView(LoginRequiredMixin, TemplateView):
    template_name = 'gardens/view.html'
    def get(self, request, *arg, **kwargs):
        self.garden_id = kwargs.get("garden_id")
        garden = get_object_or_404(Garden, pk = self.garden_id)
        width = range(0, garden.width)
        length = range(0 , garden.length)
        return render(self.request, self.template_name, {"garden": garden, "width": width, 'length': length})
