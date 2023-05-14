from django.db import models
from account.models import MyUser
from django.utils import timezone
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
    age = models.DurationField()
    completion_date = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    deletion_date = models.DateTimeField(null=True,blank=True)
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default=LOWEST_LOWER,
    )
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.created_at:
            self.age = datetime.timedelta(timezone.now()-self.created_at)
        else:
            self.age = datetime.timedelta(days=0)
        super().save()
