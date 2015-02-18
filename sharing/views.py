from django.shortcuts import render
from django.views.generic import View
import models

# Create your views here.
class IndexView(View):
    def get(self, request, event_id):
        context = {}

        context['latest_messages'] = models.Message.objects.all()[:10]
        return render(request, "sharing/index.html", context)