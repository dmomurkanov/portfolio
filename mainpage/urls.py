from crypt import methods

from . import views
from django.urls import path, include
from rest_framework import routers
from .views import main_banner, MainBannerViewset, AboutMeViewset, ExperienceViewset, WorkExperienceViewset, \
    LeadershipViewset, PortfolioViewset, ContactMeViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()

router.register("api/contact", ContactMeViewSet, basename="contact")
router.register("api/mainbanner", MainBannerViewset, basename="mainbanner")
urlpatterns = [
    path("", main_banner),
    # path("api/aboutme", AboutMeViewset.as_view()),
    # path("api/exp", ExperienceViewset.as_view()),
    # path("api/workexp", WorkExperienceViewset.as_view()),
    # path("api/leadership", LeadershipViewset.as_view()),
    # path("api/portfolio", PortfolioViewset.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('', include(router.urls))

]

