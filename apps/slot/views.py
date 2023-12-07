from django.shortcuts import render
import json
from .models import Slot
from django.http import JsonResponse
from users.models import Profile

def Play(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    user_id = request.GET.get('userID')
    try:
        user_id = int(user_id)
    except:
        return JsonResponse({'error': 'Invalid user ID'}, status=400)

    profile = Profile.objects.filter(id=user_id)
    if profile.count() != 1:
        return JsonResponse({'error': 'Invalid user ID'}, status=400)
    else:
        profile = profile.first()


    slot = Slot()
    slot.created_by = profile
    slot.save()

    data = {
        'slots': slot.get_slots(),
        'points': slot.points
    }
    return JsonResponse(data)


def Last(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    user_id = request.GET.get('userID')
    try:
        user_id = int(user_id)
    except:
        return JsonResponse({'error': 'Invalid user ID'}, status=400)

    profile = Profile.objects.filter(id=user_id)
    if profile.count() != 1:
        return JsonResponse({'error': 'Invalid user ID'}, status=400)
    else:
        profile = profile.first()

    limit = request.GET.get('limit')
    try:
        limit = int(limit)+1
    except:
        limit = 1

    plays = profile.get_last(limit)
    slots = []

    for i, play in enumerate(plays):
        if i > 0:
            slots.append([*play.get_slots(), play.points])

    profile.refresh_data()
    data = {
        'slots': slots, 
        'points': profile.total_points, 
        'rounds_played': profile.rounds_played,
        'average_points': profile.average_points
    }
    return JsonResponse(data)