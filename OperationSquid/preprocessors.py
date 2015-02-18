from events.models import Registration

def get_active_events(request):
    return {"user_events_active" : Registration.objects.filter(related_user=request.user)}
