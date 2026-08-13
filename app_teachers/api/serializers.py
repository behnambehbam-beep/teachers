from app_teachers.models import PageSubject, PageTitle, AboutUs, OurServices, EducationCategory, CourseSchedule, ImageOurClasses, CourseTable, ReadyForStart, Teacher, ContactUs
from rest_framework import serializers

class PageSubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageSubject
        fields = ["id", "pagesubject"]

class PageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageTitle
        fields = ["id", "image", "link", "title", "description"]

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["id", "image", "title", "description", "linkedin", "instagram", "twitter", "facebook", "telegram"]

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = ["id", "title", "description"]

class EducationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationCategory
        fields = ["id", "title"]

class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = ["id", "course", "day", "date", "start_time", "end_time"]

class ImageOurClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOurClasses
        fields = ["id", "course", "image"]

class CourseTableSerializer(serializers.ModelSerializer):
    schedules = CourseScheduleSerializer(many=True, read_only=True)
    images = ImageOurClassesSerializer(many=True, read_only=True)
    class Meta:
        model = CourseTable
        fields = ["id", "category", "title", "teacher", "price", "schedules", "images"]

class ReadyForStartSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        pass