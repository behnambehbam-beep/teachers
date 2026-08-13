from django.http import JsonResponse
from rest_framework.decorators import api_view
from app_teachers.models import PageSubject, PageTitle, AboutUs, OurServices, EducationCategory, CourseTable, CourseSchedule, ImageOurClasses
from app_teachers.api.serializers import PageSubjectSerializer, PageTitleSerializer, AboutUsSerializer, OurServicesSerializer, EducationCategorySerializer, CourseTableSerializer, CourseScheduleSerializer, ImageOurClassesSerializer

@api_view()
def page_subject(request):
    qs = PageSubject.objects.all()
    serializer = PageSubjectSerializer(qs, many=True)
    return JsonResponse ({
        'result' : serializer.data
    })

@api_view()
def page_title(request):
    qs = PageTitle.objects.last()
    serializer = PageTitleSerializer(qs)
    return JsonResponse ({
        'result' : serializer.data
    })

@api_view()
def about_us(request):
    qs = AboutUs.objects.last()
    serializer = AboutUsSerializer(qs)
    return JsonResponse ({
        'result' : serializer.data
    })

@api_view()
def our_services(request):
    qs = OurServices.objects.all()
    serializer = OurServicesSerializer(qs, many=True)
    return JsonResponse({
        'result': serializer.data
    })

@api_view()
def education_category(request):
    qs = EducationCategory.objects.all()
    serializer = EducationCategorySerializer(qs, many=True)
    return JsonResponse({
        'result': serializer.data
    })

@api_view()
def course_table(request):
    qs = CourseTable.objects.all()
    serializer = CourseTableSerializer(qs, many=True)
    return JsonResponse({
        'result': serializer.data
    })

@api_view()
def course_schedule(request):
    qs = CourseSchedule.objects.all()
    serializer = CourseScheduleSerializer(qs, many=True)
    return JsonResponse({
        'result': serializer.data
    })

@api_view()
def image_ourclasses(request):
    qs = ImageOurClasses.objects.all()
    serializer = ImageOurClassesSerializer(qs, many=True)
    return JsonResponse({
        'result': serializer.data
    })
