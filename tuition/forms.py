from django import forms
from .models import TuitionPost, Area


class TuitionForm(forms.ModelForm):
    class Meta:
        model = TuitionPost
        fields = ['fullname', 'district', 'area', 'class_other', 'medium', 'subjects', 'school_college',
                  'detail_tuition', 'day_per_week', 'salary', 'desire_tutor_gender', 'preference_tuition_style',
                  'mobile', 'email', 'address']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['area'].queryset = Area.objects.none()

            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['area'].queryset = Area.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['area'].queryset = self.instance.district.area_set.order_by('name')
