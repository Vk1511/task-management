from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users


@receiver(post_save, dispatch_uid="adhisAY^&*D(h", sender=Users)
def send_email(sender, instance, created, **kwargs):
    pass
    # user_name = instance.first_name.capitalize() + " " + instance.last_name.capitalize()

    # if created:
    #     send_email_and_generate_token(
    #         instance.email,
    #         user_name=user_name,
    #         email_template="../templates/mails/registration.html",
    #         email_subject="Email Verification Link",
    #     )
