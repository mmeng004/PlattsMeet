from django.db import models

# Create your models here.
from django.db import models
#creation of a user

""" from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
#URL with the username
from autoslug import AutoSlugField """

# Create your models here.
#Models for Profiles
#required for a friend request
#Create Users
#Customize the prebuilt user function in Django
#Reference
#https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model



# class Profile(models.Model):
#     MAJOR = (
#         ('Accounting','Accounting'),
#         ('Africana Studies','Africana Studies'),
#         ('Anthropology','Anthropology'),
#         ('Art','Art'),
#         ('Art Studio','Art Studio'),
#         ('Audio-Radio Production','Audio-Radio Production'),
#         ('Biochemistry','Biochemistry'),
#         ('Biology','Biology'),
#         ('Biomedical Sciences','Biomedical Sciences'),
#         ('Broadcast Journalism','Broadcast Journalism'),
#         ('Business Administration','Business Administration'),
#         ('Chemistry','Chemistry'),
#         ('Childhood Education','Childhood Education'),
#         ('Communication Sciences and Disorders','Communication Sciences and Disorders'),
#         ('Communication Studies','Communication Studies'),
#         ('Computer Science','Computer Science'),
#         ('Computer Security','Computer Security'),
#         ('Criminal Justice','Criminal Justice'),
#         ('Digital Media Production','Digital Media Production'),
#         ('Earth Science','Earth Science'),
#         ('Ecology','Ecology'),
#         ('Economics','Economics'),
#         ('English:Language Arts','English:Language Arts'),
#         ('English:Literature','English:Literature'),
#         ('English:Writing Arts','English:Writing Arts'),
#         ('Entrepreneurship','Entrepreneurship'),
#         ('Environmental Geosciences','Environmental Geosciences'),
#         ('Environmental Science','Environmental Science'),
#         ('Environmental Studies','Environmental Studies'),
#         ('Expeditionary Studies','Expeditionary Studies'),
#         ('Finance','Finance'),
#         ('Fitness and Wellness Leadership','Fitness and Wellness Leadership'),
#         ('Gender and Women Studies','Gender and Women Studies'),
#         ('Geology','Geology'),
#         ('Global Supply Chain Management','Global Supply Chain Management'),
#         ('History','History'),
#         ('Hospitality Management','Hospitality Management'),
#         ('Human Development and Family Relations','Human Development and Family Relations'),
#         ('Individualized Studies','Individualized Studies'),
#         ('Information Technology','Information Technology'),
#         ('International Business','International Business'),
#         ('Journalism','Journalism'),
#         ('Latin American Studies','Latin American Studies'),
#         ('Law and Justice','Law and Justice'),
#         ('Management','Management'),
#         ('Management Information Systems','Management Information Systems'),
#         ('Marketing','Marketing'),
#         ('Mathematics','Mathematics'),
#         ('Medical Technology','Medical Technology'),
#         ('Music','Music'),
#         ('Music Arts Management','Music Arts Management'),
#         ('Nursing','Nursing'),
#         ('Nutrition','Nutrition'),
#         ('Philosophy','Philosophy'),
#         ('Physics','Physics'),
#         ('Political Science','Political Science'),
#         ('Psychology','Psychology'),
#         ('Public Relations','Public Relations'),
#         ('Robotics','Robotics'),
#         ('Social Work','Social Work'),
#         ('Sociology','Sociology'),
#         ('Spanish','Spanish'),
#         ('Spanish Language Broadcasting','Spanish Language Broadcasting'),
#         ('Theatre','Theatre'),
#         ('TV-Video Production','TV-Video Production'),
#     )
        
#     PRONOUNS = (
#         ('He','He/Him/His'),
#         ('She','She/Her/Hers'),
#         ('They','They/Them/Theirs'),
#         ('Ze','Ze/Hir/Hirs'),
#     )
#     #first_name = models.CharField(max_length=30)
#     #last_name = models.CharField(max_length=30)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     major = models.CharField(max_length=50, choices=MAJOR)
#     pronouns = models.CharField(max_length=6, choices=PRONOUNS)
#     hobbies = models.CharField(max_length=120)
#     bio = models.CharField(max_length=120)
#     slug = AutoSlugField(populate_from='user')
#     #image = models.ImageField(default='default.png', upload_to='profile_pics')
#     friends = models.ManyToManyField("Profile", blank=True)
    

#     def __str__(self):
#         return str(self.user.username)

#     def get_absolute_url(self):
#         return "/users/{}".format(self.slug)

# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Profile.objects.create(user=instance)
#         except:
#             pass

# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)



# class FriendRequest(models.Model):
#     to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
#     from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "From {}, to {}".format(self.from_user.username, self.to_user.username)
