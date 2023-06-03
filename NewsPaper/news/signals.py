from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from NewsPaper import settings
from .models import Subscriber, PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers_emails = []
        for cat in categories:
            subscribers = Subscriber.objects.filter(category=cat)
            subscribers_emails += [s.user.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)


def send_notifications(preview, pk, title, subscribers_email):
    html_content = render_to_string (
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
