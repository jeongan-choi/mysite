from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    
    
# 회원 가입이 완료된 후 실행될 함수    
def on_send_mail(**kwargs):
    if kwargs['created'] :
        user = kwargs['instance']
        send_mail('hello', 'welcome....', 'admin@kt.com', [user.email], fail_silently=False)

post_save.connect(on_send_mail, sender=settings.AUTH_USER_MODEL)