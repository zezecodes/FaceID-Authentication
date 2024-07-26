from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .utils import is_ajax, classify_face
import base64
from logs.models import Logs
from django.core.files.base import ContentFile
from profiles.models import Profile

def login_view(request):
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'main.html', {})

def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')
        decoded_file = base64.b64decode(str_img)

        x = Logs()
        x.photo = ContentFile(decoded_file, 'upload.png')
        x.save()

        result = classify_face(x.photo.path)
        user_exists = User.objects.filter(username=result).exists
        if user_exists:
            user = User.objects.get(username=result)
            profile = Profile.objects.get(user=user)
            x.profile = profile
            x.save()

            login(request, user)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})