from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect

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
        try:
            context['registration'] = Registration.objects.get(related_event__id=event_id, related_user=request.user)
        except:
            pass

        return render(request, "events/event.html", context)


class AttendEventView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)

        obj, created = Registration.objects.get_or_create(related_event=event, related_user=request.user)

        obj.save()

        return redirect("events:event", event_id)


class NewEventView(View):
    def get(self, request):
        context = {}

        context['event_form'] = forms.EventForm()

        return render(request, 'events/createEvent.html', context)

    def post(self, request):
        context = {}

        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            return redirect("events:index")
        else:
            context["event_form"] = form
            return render(request, 'events/createEvent.html', context)
