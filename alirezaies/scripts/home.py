
from django.shortcuts import get_object_or_404

from .sinergy import sinergy
from ..models import (
    Bio,
    Language,
    SocialLinks,
    Specialities,
    SkillCategory,
    Skill,
    Experience,
    ContactInfo,
)

class HomeView():
    def bio(self):
        bio = get_object_or_404(Bio, id=1)
        
        return bio

    def get_langs(self):
        langs = Language.objects.all()

        return langs

    def socal_links(self):
        objects = SocialLinks.objects.all()

        return objects

    def expertise(self):
        data = sinergy(Specialities)

        return data

    def skills(self):
        skills_q = SkillCategory.objects.all()

        return skills_q

    def experience(self):
        data = sinergy(Experience, 'start_time')

        return data

    def contact_info(self):
        data = ContactInfo.objects.first()

        return data