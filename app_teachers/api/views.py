from django.http import JsonResponse
from app_teachers.models import PageSubject, PageTitle, AboutUs
from rest_framework.decorators import api_view
from app_teachers.api.serializers import PageSubjectSerializer, PageTitleSerializer, AboutUsSerializer

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
