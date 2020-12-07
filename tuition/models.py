from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Style(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Area(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=False,default='Dhaka')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PerDay(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TuitionPost(models.Model):
    # per_day_choice = [('01', '1 day/week'), ('02', '2 day/week'), ('03', '3 day/week'), ('04', '4 day/week'),
    #                   ('05', '5 day/week'), ('06', '6 day/week'), ('07', '7 day/week')]
    # gender = [('g1', 'Male'), ('g2', 'Female'), ('g3', 'Other')]
    # style = (('online', 'Online'), ('private', 'Private'),
    #          ('coaching', 'Coaching'), ('group', 'Group'))
    # prefer_medium = [('En', 'English'), ('Bn', 'Bangla'),
    #                  ('Ar', 'Arabic'), ('Ot', 'Other')]
    fullname = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    class_other = models.CharField(max_length=100)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=250)
    school_college = models.CharField(max_length=500)
    detail_tuition = models.TextField()
    day_per_week = models.ForeignKey(PerDay, on_delete=models.CASCADE)
    salary = models.CharField(max_length=50)
    desire_tutor_gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    # preference_tuition_style = MultiSelectField(
    #     max_length=50, max_choices=2, choices=style,default='private')
    preference_tuition_style = models.ForeignKey(Style, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
