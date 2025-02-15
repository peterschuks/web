from django.shortcuts import render
# views.py
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserLocation

@csrf_exempt
@login_required
def save_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            user_location, created = UserLocation.objects.update_or_create(
                user=request.user,
                defaults={'latitude': latitude, 'longitude': longitude}
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=400)
    return JsonResponse({'status': 'fail'}, status=400)


def Home(request):
    
    return render(request, 'home.html')