# myapp/forms.py
from django import forms
# from .models import Stream

# class StreamForm(forms.ModelForm):
#     class Meta:
#         model = Stream
#         fields = ['name', 'subjects']
#         widgets = {
#             'subjects': forms.CheckboxSelectMultiple
#         }
# forms.py
# from django import forms
# from .models import Survey

# class SurveyForm(forms.ModelForm):
#     class Meta:
#         model = Survey
#         fields = ['question_1', 'question_2']
#         widgets = {
#             'question_1': forms.RadioSelect,
#             'question_2': forms.RadioSelect,
#         }

# forms.py
from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['optimum_learning', 'assesments']
        widgets = {
            'optimum_learning': forms.RadioSelect,
            'assesments': forms.RadioSelect,
        }
        labels = {
            'optimum_learning': 'What do you think is optimum learning according to you:',
            'assesments':'What kind of assesments do you prefer:'
        }