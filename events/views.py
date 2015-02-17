from django.shortcuts import render
from django.views.generic import View

from .models import *
# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}

        context['events_open'] = Event.objects.filter(registration_open=True)
        return render(request, "events/index.html", context)
