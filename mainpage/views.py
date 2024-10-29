

from django.shortcuts import render
from django.template import context
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

# from serializers import
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from django.core.mail import EmailMessage
from .serializers import MainBannerSerializer, AboutMeSerializer, ExperienceSerializer, WorkExperienceSerializer, \
    LeadershipSerializer, PortfolioSerializer, ContactMeSerializer
from .smtp import smtp


def main_banner(request):
    main_info = PersonalInfo.objects.all()
    additional = AdditionalInfo.objects.all()
    experience = Experience.objects.all()
    work_experience = WorkExperience.objects.all()
    portfolio = Portfolio.objects.all()
    leadership = WorkExperience.objects.filter(leadership=True)

    return render(
        request,
        "base.html",
        {
            "main_info": main_info,
            "additional": additional,
            "experience":experience,
            "work_experience": work_experience,
            "portfolio": portfolio,
            "leadership": leadership,
        }
    )


class MainBannerViewset(ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = MainBannerSerializer

class AboutMeViewset(ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = AboutMeSerializer

class ExperienceViewset(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class WorkExperienceViewset(ListAPIView):
    queryset = WorkExperience.objects.filter(leadership=False)
    serializer_class = WorkExperienceSerializer

class LeadershipViewset(ListAPIView):
    queryset = WorkExperience.objects.filter(leadership=True)
    serializer_class = LeadershipSerializer

class PortfolioViewset(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ContactMeViewSet(viewsets.ViewSet):
    queryset = ContactMe.objects.all()

    @extend_schema(tags=["Отправка сообщения на почту"], summary='Отправка сообщения на почту')
    def create(self, request):
        serializer = ContactMeSerializer(data=request.data, context={"context": context})
        if serializer.is_valid():
            contact = serializer.save()
            message_text = f"Пришло сообщение от {contact.fullname}, текст {contact.text}"
            connection = smtp()
            message = EmailMessage(
                subject='Новое обращение',
                body=message_text,
                from_email="nurdinovbaiel2005@gmail.com",
                to="nurdinovbaiel2005@gmail.com",
            )
            connection.send_messages([message])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
