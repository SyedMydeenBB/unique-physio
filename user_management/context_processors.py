
from .models import Function
def custom_permissions(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return {
                'user_permissions': [data.function_name for data in Function.objects.all()], 
            }
        else:
            return {
                'user_permissions': [data.function_name for data in user.roles.permissions.all()] if user.roles else [], 
            }
    return {}