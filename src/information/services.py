from django.core.mail import send_mail
from library import settings
from rest_framework.response import Response
from celery import shared_task

@shared_task(bind=True)
def send_mail_func(self,to,subject,body):
    send_mail(
        recipient_list=[to],
        subject=subject,
        message=body,
        from_email=settings.EMAIL_HOST_USER
    )