from app_teachers.models import PageSubject, PageTitle, AboutUs, OurServices, OurClasses, ImageOurClasses, ReadyForStart, OurTeam, ContactUs
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
        pass

class OurClassesSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ImageOurClassesSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ReadyForStartSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        pass