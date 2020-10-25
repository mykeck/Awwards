from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    # image = CloudinaryField('image')
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=80)
    pub_date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_project(self):
        return self.save()

    def delete_project(self):
        return self.delete()

    @classmethod
    def update_title(cls,id,tittle):
        cls.objects.filter(id=id).update(title= title)
        updated_tittle = cls.objects.filter(id=id)
        return updated_title 

    @classmethod
    def update_description(cls,id,description):
        cls.objects.filter(id=id).update(description=description) 
        update_description = cls.objects.filter(id=id) 
        return updated_description

    @classmethod
    def update_link(cls,id,link):
        cls.objects.filter(id=id).update(link=link)
        updated_link = cls.objects.filter(id=id)
        return updated_link

    @classmethod
    def search_project(cls,search_term):
        return Project.objects.filter(title_icontains=search_term) 

    @classmethod
    def get_project_by_id(cls,id):
        project = cls.objects.filter(id=id)
        return project       


