from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

import forms

from .models import *
# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}

        context['events_open'] = Event.objects.filter(registration_open=True)
        return render(request, "events/index.html", context)

class EventView(View):
    def get(self, request, event_id):
        context = {}

        context['event_specified'] = get_object_or_404(Event, pk=event_id)

        return render(request, "events/event.html", context)

class NewEventView(View):
    def get(self, request):
        context = {}

        context['event_form'] = forms.EventForm()

        return render(request, 'events/createEvent.html', context)