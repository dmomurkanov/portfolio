from . import views
from django.urls import path

from .views import main_banner, MainBannerViewset, AboutMeViewset, ExperienceViewset, WorkExperienceViewset, LeadershipViewset, PortfolioViewset
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("", main_banner),
    path("api/mainbanner", MainBannerViewset.as_view()),
    path("api/aboutme", AboutMeViewset.as_view()),
    path("api/exp", ExperienceViewset.as_view()),
    path("api/workexp", WorkExperienceViewset.as_view()),
    path("api/leadership", LeadershipViewset.as_view()),
    path("api/portfolio", PortfolioViewset.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

]

