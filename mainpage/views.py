from django.shortcuts import render
# from serializers import
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from .serializers import MainBannerSerializer, AboutMeSerializer, ExperienceSerializer, WorkExperienceSerializer, \
    LeadershipSerializer, PortfolioSerializer


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

