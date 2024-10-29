from rest_framework import routers

from . import views
from django.urls import path

from .views import main_banner, MainBannerViewset, AboutMeViewset, ExperienceViewset, WorkExperienceViewset, LeadershipViewset, PortfolioViewset

router = routers.DefaultRouter()

router.register("api/mainbanner", MainBannerViewset, basename="mainbanner")
router.register("api/aboutme", AboutMeViewset, basename="aboutme")
router.register("api/exp", ExperienceViewset, basename="exp")
router.register("api/workexp", WorkExperienceViewset, basename="workexp")
router.register("api/leader", LeadershipViewset, basename="leader")
router.register("api/portfolio", PortfolioViewset, basename="portfolio")

