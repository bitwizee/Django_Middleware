from django.shortcuts import render
from .models import UserActivityLog


def activity_log_view(request):
    logs = UserActivityLog.objects.all().order_by('-time')[:10]
    return render(request, 'logger.html', {'logs': logs})