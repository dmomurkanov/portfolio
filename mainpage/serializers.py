from rest_framework.serializers import ModelSerializer
from .models import PersonalInfo, AdditionalInfo, Experience, WorkExperience, Portfolio


class MainBannerSerializer(ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ('fullname', 'profession', 'resume_file', 'image', 'image_mobile')

class AdditionalInfoSerializer(ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = "__all__"
class AboutMeSerializer(ModelSerializer):
    additional_info = AdditionalInfoSerializer(many=True)
    class Meta:
        model = PersonalInfo
        fields = ("about_me", "additional_info")


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ("title", "text")

class WorkExperienceSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ("icon", "company_name", "position", "responsibility")

class LeadershipSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ("icon", "company_name", "position", "responsibility")


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ("image", "image_mobile", "project_name", "github_link", "live_demo")