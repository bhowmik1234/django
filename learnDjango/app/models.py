from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class varity(models.Model):
    gender_type = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender_type)
    image = models.ImageField(upload_to='assests/', default="")
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
    

# one to many
class review(models.Model):
    rev = models.ForeignKey(varity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    createAt = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.user.username} review for {self.rev.name}"
    

# many to many
class collage(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    varity = models.ManyToManyField(varity, related_name='collage')

    def __str__(self) -> str:
        return self.name
    

# one to one
class cetificate(models.Model):
    cer = models.OneToOneField(varity, on_delete=models.CASCADE, related_name='certificate')
    cer_no = models.CharField(max_length=100)
    issueDate = models.DateTimeField(default=timezone.now)
    validUntil = models.DateTimeField()

    def __str__(self) -> str:
        return f"certificate for {self.name.chai}"