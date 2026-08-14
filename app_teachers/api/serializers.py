from app_teachers.models import PageSubject, PageTitle, AboutUs, OurServices, EducationCategory, CourseSchedule, ImageOurClasses, CourseTable, OurTeacher, AcademyNews, ContactUs, ReadyForStart
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

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
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        if obj.image:
            thumbnail = get_thumbnail(obj.image, '400x300', crop='center', quality=90)
            request = self.context.get("request")
            return request.build_absolute_uri(thumbnail.url)
        return None
    class Meta:
        model = ImageOurClasses
        fields = ["id", "course", "image"]

class CourseTableSerializer(serializers.ModelSerializer):
    schedules = CourseScheduleSerializer(many=True, read_only=True)
    images = ImageOurClassesSerializer(many=True, read_only=True)
    class Meta:
        model = CourseTable
        fields = ["id", "category", "title", "teacher", "price", "schedules", "images"]

class OurTeacherSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        if obj.image:
            thumbnail = get_thumbnail(obj.image, "400x500", crop="center", quality=90)
            request = self.context.get("request")
            return request.build_absolute_uri(thumbnail.url)
        return None
    class Meta:
        model = OurTeacher
        fields = ["id", "image", "first_name", "last_name", "experience"]

class AcademyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademyNews
        fields = ["id", "title", "description"]

class ContactUsSerializer(serializers.ModelSerializer):
    social_media = serializers.SerializerMethodField()
    def get_social_media(self, obj):
        about = AboutUs.objects.first()
        if not about:
            return {}
        social_media = {}

        if about.instagram:
            social_media["instagram"] = about.instagram

        if about.telegram:
            social_media["telegram"] = about.telegram

        if about.facebook:
            social_media["facebook"] = about.facebook

        if about.twitter:
            social_media["twitter"] = about.twitter

        if about.linkedin:
            social_media["linkedin"] = about.linkedin
            
        return social_media

    class Meta:
        model = ContactUs
        fields = ["id", "address", "tel", "Fax", "phone", "email", "social_media",]

class ReadyForStartSerializer(serializers.ModelSerializer):
    class Meta:
        pass