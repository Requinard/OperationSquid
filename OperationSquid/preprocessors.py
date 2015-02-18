from events.models import Registration
from django.contrib.auth.decorators import login_required

def get_active_events(request):
    if request.user.is_authenticated():
        return {"user_events_active" : Registration.objects.filter(related_user=request.user)}
    else:
        return {}
