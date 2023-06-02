from django.db import models

# Create your models here.

class Learner(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 50)
    physical_address = models.CharField(max_length=1000, default = True)
    password = models.CharField(max_length = 50)
    cellphone = models.CharField(max_length=10)
    id_copy = models.CharField(max_length=13)
    matric_certificate = models.CharField(max_length = 10)
    proof_of_income = models.CharField(max_length=10)

class Address(models.Model):
    block_number = models.BigIntegerField()
    street = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    postal_code = models.BigIntegerField()
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)

class Application(models.Model):
    application_type = models.CharField(max_length=20)
    current_academic_level = models.BigIntegerField()
    level_applying_for = models.CharField(max_length=20)
    first_choice_of_sponsor = models.CharField(max_length = 50)
    second_choice_of_sponsor = models.CharField(max_length=50)











