from django import forms
from quiz_app.models import QuestionModel
class quiz_form(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'
