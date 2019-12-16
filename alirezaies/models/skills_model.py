from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    percent = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name