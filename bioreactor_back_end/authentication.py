from rest_framework.authentication import SessionAuthentication as BaseSessionAuthentication
from bioreactor_auth.models import DeviceAuthenticationToken


class SessionAuthentication(BaseSessionAuthentication):
    def enforce_csrf(self, request):
        return

    def authenticate(self, request):
        token = request._request.GET.get('token')
        if token:
            try:
                token_object = DeviceAuthenticationToken.objects.get(token=token)
            except DeviceAuthenticationToken.DoesNotExist:
                return super().authenticate(request)
            return token_object.created_by, None
        return super().authenticate(request)
