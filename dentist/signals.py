from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

# from dentist.models import Patient


# def patient_profile(sender, instance, created, **kwargs):
#     if created:
#         # 'created' is there because get_or_create returns the object and whether it was created or not.
#         group, created = Group.objects.get_or_create(name='patient')
#         instance.groups.add(group)

#         Patient.objects.create(
#             user=instance,
#             name=instance.username,
#         )


# post_save.connect(patient_profile, sender=User)
