from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from kifur.kifu_users.models import UserProfile

def user_profile(request, slug):
    u = get_object_or_404(UserProfile, slug=slug)
    return render_to_response('kifu_users/user_profile.html', {'user': u})

def user_profile_from_id(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    return render_to_response('kifu_users/user_profile.html', {'user': u})    