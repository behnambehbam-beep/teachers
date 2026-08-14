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
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500, blank=True)

class EducationCategory(models.Model):
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class CourseTable(models.Model):
    category = models.ForeignKey(EducationCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.teacher}"

class CourseSchedule(models.Model):
    course = models.ForeignKey(CourseTable,on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=20, blank=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.course.title} - {self.day}"

class ImageOurClasses(models.Model):
    course = models.ForeignKey(CourseTable, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return f"تصویر - {self.course.title if self.course else 'بدون دوره'}"

class OurTeacher(models.Model):
    image = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    experience = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AcademyNews(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
            return self.title

class ContactUs(models.Model):
    address = models.CharField(max_length=200, blank=True)
    tel = models.CharField(max_length=11, blank=True)
    Fax = models.CharField(max_length=11, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)

class ReadyForStart(models.Model):
    pass