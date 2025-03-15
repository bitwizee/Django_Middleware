from django.utils.timezone import now
from .models import UserActivityLog



class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        ip = request.META.get('REMOTE_ADDR', '')

        user = request.user if request.user.is_authenticated else None



        UserActivityLog.objects.create(
            user=user,
            is_address=ip,
            path=request.path,
            time=now()
        )

        return response