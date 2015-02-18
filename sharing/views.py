from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self, request, event_id):
        return render(request, "sharing/index.html", {})