from calendar import calendar
from django.core.mail import EmailMessage
from django.shortcuts import render

from lib2to3.fixes.fix_input import context

from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView

from drf_spectacular.utils import extend_schema

from .models import *
from .serializers import MainBannerSerializer, AboutMeSerializer, ExperienceSerializer, WorkExperienceSerializer, \
    LeadershipSerializer, PortfolioSerializer, ContactMeSerializer
from .smtp.sender import smtp


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

@extend_schema(
    tags=["Главный баннер"],
    summary="Апишка для получения данных для главного баннера"
)
class MainBannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = MainBannerSerializer


@extend_schema(
    tags=["Главный баннер"],
    summary="Апишка для получения данных для второй секции"
)
class AboutMeViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = AboutMeSerializer

class ExperienceViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer



class WorkExperienceViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WorkExperience.objects.filter(leadership=False)
    serializer_class = WorkExperienceSerializer

class LeadershipViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WorkExperience.objects.filter(leadership=True)
    serializer_class = LeadershipSerializer


class PortfolioViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

@extend_schema(tags=["Отправка сообщения на почту"], summary='Отправка сообщения на почту')
class ContactMeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer

    def create(self, request):
        serializer = ContactMeSerializer(data=request.data, context={"context": context})
        if serializer.is_valid():
            contact = serializer.save()
            message_text = f"Пришло сообщение от {contact.fullname}, текст {contact.text}"
            connection = smtp()
            message = EmailMessage(
                subject='Новое обращение',
                body=message_text,
                from_email="omurkanovd22@gmail.com",
                to=["omurkanovd22@gmail.com",]
            )
            connection.send_messages([message])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
