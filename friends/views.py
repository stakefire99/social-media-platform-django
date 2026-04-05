from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import FriendRequest
from notifications.models import Notification

@login_required
def send_request(request, username):
    to_user = get_object_or_404(User, username=username)
    existing = FriendRequest.objects.filter(from_user=request.user, to_user=to_user).first()
    if existing:
        messages.info(request, f'Friend request already sent to {to_user.username}!')
    else:
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)
        # Create notification
        Notification.objects.create(
            recipient=to_user,
            sender=request.user,
            notification_type='friend_request',
            message=f'sent you a friend request.'
        )
        messages.success(request, f'Friend request sent to {to_user.username}!')
    return redirect('user-profile', username=username)

@login_required
def accept_request(request, pk):
    friend_request = get_object_or_404(FriendRequest, pk=pk)
    friend_request.accepted = True
    friend_request.save()
    messages.success(request, f'You are now friends with {friend_request.from_user.username}!')
    return redirect('friend-list')

@login_required
def friend_list(request):
    pending_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False)
    friends_sent = FriendRequest.objects.filter(from_user=request.user, accepted=True)
    friends_received = FriendRequest.objects.filter(to_user=request.user, accepted=True)
    return render(request, 'friends/friend_list.html', {
        'requests': pending_requests,
        'friends_sent': friends_sent,
        'friends_received': friends_received,
    })