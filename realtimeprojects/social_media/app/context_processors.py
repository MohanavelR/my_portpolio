from .models import Notification
from .models import Message
# ==========================================================
def notification_count(request):
    if request.user.is_authenticated:
        no_of_notification = Notification.objects.filter(user=request.user,is_seen=False).count()
    else:
        no_of_notification = 0
    return {
        'no_of_notification': no_of_notification
        }
# =========================================================
def message_count(request):
    if request.user.is_authenticated:
        no_of_messages=Message.objects.filter(receiver=request.user,is_seen=False).count()
    else:
        no_of_messages=0
    return {
        'no_of_messages':no_of_messages
    }    