from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
     MAJOR = (
         ('Accounting','Accounting'),
         ('Africana Studies','Africana Studies'),
         ('Anthropology','Anthropology'),
         ('Art','Art'),
         ('Art Studio','Art Studio'),
         ('Audio-Radio Production','Audio-Radio Production'),
         ('Biochemistry','Biochemistry'),
         ('Biology','Biology'),
         ('Biomedical Sciences','Biomedical Sciences'),
         ('Broadcast Journalism','Broadcast Journalism'),
         ('Business Administration','Business Administration'),
         ('Chemistry','Chemistry'),
         ('Childhood Education','Childhood Education'),
         ('Communication Sciences and Disorders','Communication Sciences and Disorders'),
         ('Communication Studies','Communication Studies'),
         ('Computer Science','Computer Science'),
         ('Computer Security','Computer Security'),
         ('Criminal Justice','Criminal Justice'),
         ('Digital Media Production','Digital Media Production'),
         ('Earth Science','Earth Science'),
         ('Ecology','Ecology'),
         ('Economics','Economics'),
         ('English:Language Arts','English:Language Arts'),
         ('English:Literature','English:Literature'),
         ('English:Writing Arts','English:Writing Arts'),
         ('Entrepreneurship','Entrepreneurship'),
         ('Environmental Geosciences','Environmental Geosciences'),
         ('Environmental Science','Environmental Science'),
         ('Environmental Studies','Environmental Studies'),
         ('Expeditionary Studies','Expeditionary Studies'),
         ('Finance','Finance'),
         ('Fitness and Wellness Leadership','Fitness and Wellness Leadership'),
         ('Gender and Women Studies','Gender and Women Studies'),
         ('Geology','Geology'),
         ('Global Supply Chain Management','Global Supply Chain Management'),
         ('History','History'),
         ('Hospitality Management','Hospitality Management'),
         ('Human Development and Family Relations','Human Development and Family Relations'),
         ('Individualized Studies','Individualized Studies'),
         ('Information Technology','Information Technology'),
         ('International Business','International Business'),
         ('Journalism','Journalism'),
         ('Latin American Studies','Latin American Studies'),
         ('Law and Justice','Law and Justice'),
         ('Management','Management'),
         ('Management Information Systems','Management Information Systems'),
         ('Marketing','Marketing'),
         ('Mathematics','Mathematics'),
         ('Medical Technology','Medical Technology'),
         ('Music','Music'),
         ('Music Arts Management','Music Arts Management'),
         ('Nursing','Nursing'),
         ('Nutrition','Nutrition'),
         ('Philosophy','Philosophy'),
         ('Physics','Physics'),
         ('Political Science','Political Science'),
         ('Psychology','Psychology'),
         ('Public Relations','Public Relations'),
         ('Robotics','Robotics'),
         ('Social Work','Social Work'),
         ('Sociology','Sociology'),
         ('Spanish','Spanish'),
         ('Spanish Language Broadcasting','Spanish Language Broadcasting'),
         ('Theatre','Theatre'),
         ('TV-Video Production','TV-Video Production'),
     )
        
     PRONOUNS = (
         ('He','He/Him/His'),
         ('She','She/Her/Hers'),
         ('They','They/Them/Theirs'),
         ('Ze','Ze/Hir/Hirs'),
     )
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     major = models.CharField(max_length=50, choices=MAJOR)
     pronouns = models.CharField(max_length=6, choices=PRONOUNS)
     hobbies = models.CharField(max_length=120)
     bio = models.CharField(max_length=120)
     friends = models.ManyToManyField("Profile", blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()