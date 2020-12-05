from django.db import models
# from multiselectfield import MultiSelectField
# from django.utils.encoding import python_2_unicode_compatible


# Create your models here.


class TuitionPost(models.Model):
    per_day_choice = [('01', '1 day/week'), ('02', '2 day/week'), ('03', '3 day/week'), ('04', '4 day/week'),
                      ('05', '5 day/week'), ('06', '6 day/week'), ('07', '7 day/week')]
    gender = [('g1', 'Male'), ('g2', 'Female'), ('g3', 'Other')]
    style = (('online', 'Online'), ('private', 'Private'),
             ('coaching', 'Coaching'), ('group', 'Group'))
    prefer_medium = [('En', 'English'), ('Bn', 'Bangla'),
                     ('Ar', 'Arabic'), ('Ot', 'Other')]
    fullname = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    select_area = models.CharField(max_length=100)
    class_other = models.CharField(max_length=100)
    medium = models.CharField(
        max_length=2, choices=prefer_medium, default='Bn')
    subjects = models.CharField(max_length=250)
    school_college = models.CharField(max_length=500)
    detail_tuition = models.TextField()
    day_per_week = models.CharField(
        max_length=2, choices=per_day_choice, default='03')
    salary = models.CharField(max_length=50)
    desire_tutor_gender = models.CharField(
        max_length=2, choices=gender, default='g3')
    # preference_tuition_style = MultiSelectField(
    #     max_length=50, max_choices=2, choices=style)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

