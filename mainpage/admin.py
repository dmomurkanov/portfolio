from django.contrib import admin

from .models import PersonalInfo, AdditionalInfo, Experience, WorkExperience, Portfolio, ContactMe
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    pass
