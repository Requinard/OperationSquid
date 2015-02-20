from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from events.models import Event
import models
import forms

# Create your views here.
class IndexView(View):
    @method_decorator(login_required)
    def get(self, request, event_id):
        context = {}
        context['event'] = get_object_or_404(Event, pk=event_id)
        context['latest_messages'] = models.Message.objects.all()[:10]
        return render(request, "sharing/index.html", context)

class NewMessageView(View):
    @method_decorator(login_required)
    def get(self, request, event_id):
        context = {}
        context['event'] = get_object_or_404(Event, pk=event_id)
        context['upload-form'] = forms.MessageForm()

        return render(request, "sharing/newMessage.html", context)

    @method_decorator(login_required)
    def post(self, request, event_id):
        form = forms.MessageForm(request.POST, request.FILES)

        if form.is_valid():
            model = form.save(commit=False)
            model.related_user = request.user
            model.related_event = get_object_or_404(Event, pk=event_id)

            form.save()

            return redirect("live:index", event_id)
        else:
            context = {}
            context['upload-form'] = form
            return render(request, "sharing/newMessage.html", context)

class MessageView(View):
    @method_decorator(login_required)
    def get(self, request, event_id, message_id):
        context = {}

        context['event'] = get_object_or_404(Event, pk=event_id)
        context['message'] = get_object_or_404(models.Message, pk=message_id)

        return render(request, "sharing/message.html", context)