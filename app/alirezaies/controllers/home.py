
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)

from .forms.contact_form import ContactUsForm
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

    def sinergy(self, model, order_by=None):
        """
        For easy understanding:
        imagine we have five items in our db (1,2,3,4,5)
        this function returns a list called object
        the output for the above datas would be like:
        objects = [[1,2], [3,4], [5]]

        so I can use len(objects) to make 'row's and nest other things using for loop
        """
        if order_by is None:
            q = model.objects.all()
        else:
            q = model.objects.all().order_by(order_by)
            
        q_counter = model.objects.count()
        

        #prepare objects
        # for now, only me and God know how this code works
        # for upcoming questions, ask God about it (not me!)

        objects = []
        List = []
        counter = 0
        master_counter = 0

        for item in q:
            List.append(item)
            counter += 1
            master_counter += 1

            if counter == 2:
                objects.append(List)
                counter = 0
                List = []

            if master_counter == q_counter:
                objects.append(List)
                break

        return objects

# ================ Home View Controller ================
    def home_controller(self, request):
                
        langs = Language.objects.all()
        bio = get_object_or_404(Bio, id=1)
        social = SocialLinks.objects.all()
        expertise = self.sinergy(Specialities)
        skills = SkillCategory.objects.all()
        experience = self.sinergy(Experience, 'start_time')
        contact_info =ContactInfo.objects.first()

        data = {
            'langs': langs,
            'bio': bio,
            'social': social,
            'expertise': expertise,
            'skills': skills,
            'exp': experience,
            'c_info': contact_info,
        }

        if request.method == 'POST':
            form = ContactUsForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return(
                    redirect('/hearts/')
                )
        else:
            form = ContactUsForm()
            data.update({'form': form})
            return(
                render(request, 'index.html', data)
            )