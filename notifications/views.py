from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def notifications_list(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    notifications.filter(is_read=False).update(is_read=True)
    return render(request, 'notifications/notifications.html', {'notifications': notifications})