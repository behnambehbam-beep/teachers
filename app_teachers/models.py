from django.db import models

class PageSubject(models.Model):
    pagesubject = models.CharField(max_length=30)

class PageTitle(models.Model):
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

class AboutUs(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    telegram = models.URLField(blank=True)


class OurServices(models.Model):
    pass

class OurClasses(models.Model):
    pass

class ImageOurClasses(models.Model):
    pass

class ReadyForStart(models.Model):
    pass

class OurTeam(models.Model):
    pass

class ContactUs(models.Model):
    pass