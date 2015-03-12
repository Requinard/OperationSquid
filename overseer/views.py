from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from forms import NewsForm, AppointmentForm

from events.models import Event
# Create your views here.
class IndexView(View):
    def get(self, request, event_id=0):
        context = {}

        context['news_form'] = NewsForm()
        context['event'] = get_object_or_404(Event, id=event_id)

        return render(request, "overseer/index.html", context)

class NewsView(View):
    def get(self, request, event_id):
        context = {}

        context['news_form'] = NewsForm()

        return render(request, "overseer/createNews.html", context)

    def post(self, request, event_id):
        form = NewsForm(request.POST)

        if form.is_valid():
            model = form.save(commit=False)

            model.related_event = get_object_or_404(Event, id=event_id)

            model.save()

            return redirect("overseer:index", event_id)
        else:
            context = {}

            context['news_form'] = form
            context['event'] = get_object_or_404(Event, id=event_id)

            return render(request, "overseer/createNews.html", context)

class AppointmentView(View):
    def get(self, request, event_id):
        context = {}

        context['appointment_form'] = AppointmentForm()

        return render(request, "overseer/createAppointment.html", context)

    def post(self, request, event_id):
        form = AppointmentForm(request.POST)

        if form.is_valid():
            model = form.save(commit=False)

            model.related_event = get_object_or_404(Event, id=event_id)

            model.save()

            return redirect("overseer:index", event_id)
        else:
            context = {}

            context['appointment_form'] = form
            context['event'] = get_object_or_404(Event, id=event_id)

            return render(request, "overseer/createAppointment.html", context)