from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # First try the standard Authorization header
        header = self.get_header(request)
        if header is not None:
            return super().authenticate(request)

        # Then fallback to access_token from cookies
        raw_token = request.COOKIES.get('access_token')
        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except Exception:
            raise AuthenticationFailed("Invalid or expired token from cookie")
