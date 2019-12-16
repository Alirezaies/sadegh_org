
from ..models import (
    Bio,
    Language,
    SocialLinks,
    Specialities,
    SkillCategory,
    Skill
)

class HomeView():
    def bio(self):
        bio = Bio.objects.first().bio
        
        return bio

    def get_langs(self):
        langs = Language.objects.all()

        return langs

    def socal_links(self):
        objects = SocialLinks.objects.all()

        return objects

    def expertise(self):
        """
        For easy understanding:
        imagine we have five items in our db (1,2,3,4,5)
        this function returns a list called object
        the output for the above datas would be like:
        objects = [[1,2], [3,4], [5]]

        so I can use len(objects) to make 'row's and nest other shits using for loop
        """
        expertise = Specialities.objects.all()
        q_counter = Specialities.objects.count()

        #prepare objects
        # for now, only me and God know how this code works
        # for upcoming questions, ask God about it

        objects = []
        List = []
        counter = 0
        master_counter = 0

        for item in expertise:
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

    def skills(self):
        skills_q = SkillCategory.objects.all()

        return skills_q

    