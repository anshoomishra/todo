from django.db import models
from account.models import MyUser
from django.utils import timezone
from django.db.models.signals import post_save

import datetime

# Create your models here.
LOWEST_LOWER = "9"
PRIORITY_CHOICES = (
    ("highest", "1"),
    ("middle_highest", "2"),
    ("lower_highest", "3"),
    ("highest_middle", "4"),
    ("middle_middle", "5"),
    ("lowest_middle", "6"),
    ("highest_lower", "7"),
    ("middle_lower", "8"),
    ("lowest_lower", "9"),
)


class Task(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    age = models.DurationField(blank=True)
    completion_date = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    deletion_date = models.DateTimeField(null=True,blank=True)
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default=LOWEST_LOWER,
    )
    finishing_date = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.completion_date:
            difference = self.completion_date-timezone.now()
            self.age = datetime.timedelta(days=difference.days)
        else:
            self.age = datetime.timedelta(days=0)
        super().save()

def post_save_task_receiver(sender,instance:Task,*args,**kwargs):
    if instance.completion_date:
        difference = instance.completion_date - instance.created_at
        print(datetime.timedelta(days=difference.days))
        instance.age = datetime.timedelta(days=difference.days)
    else:
        instance.age = datetime.timedelta(days=0)



post_save.connect(post_save_task_receiver,sender=Task)