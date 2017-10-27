from django.db import models


# Create your models here.

class employees (models.Model):
    employee_id = models.IntegerField (primary_key=True)
    first_name = models.CharField (max_length=25, null=False)
    last_name = models.CharField (max_length=25, null=True)
    email = models.CharField (max_length=25)

    def __str__(self):
        return "{0} {1}".format (self.first_name, self.last_name)


class project (models.Model):
    project_id = models.IntegerField (primary_key=True)
    project_name = models.CharField (max_length=30, null=False)
    project_client = models.CharField (max_length=25, null=False)
    project_details = models.CharField (max_length=50, null=True)

    def __str__(self):
        return self.project_name


class projectEmployee (models.Model):
    projectEmployee_id = models.IntegerField (primary_key=True)
    project_name = models.CharField (max_length=25)
    porject_employee = models.CharField (max_length=25, null=True)
    project_TL = models.CharField (max_length=25, null=True)
    project_manager = models.CharField (max_length=25)

    def __str__(self):
        return "{0} -- {1}".format (self.project_name, self.porject_employee)
