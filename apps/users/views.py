from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

def UserList(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    users = Profile.objects.all().values('id', 'name', 'email', 'total_points', 'rounds_played', 'average_points')

    return JsonResponse(list(users), safe=False)

@csrf_exempt
def UserNew(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)

    name = data['name']
    email = data['email']

    if not name or not email:
        return JsonResponse({'error': 'Invalid data'}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already exists'}, status=400)

    user = User.objects.create_user(
        username=email,
        email=email
    )

    profile = Profile(
        user=user,
        name=name,
        email=email
    )
    profile.save()

    data = {
        'id': profile.user.pk,
        'name': profile.name,
        'email': profile.email,
        'total_points': profile.total_points,
        'rounds_played': profile.rounds_played,
        'average_points': profile.average_points
    }    

    return JsonResponse({'message': 'User created', 'user': data}, status=201)

