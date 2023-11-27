# forms.py
from django import forms
from .models import Property

class CustomTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super().__init__(*args, **kwargs)

class PropertyUpdateForm(forms.ModelForm):
    description = forms.CharField(
        widget=CustomTextarea(attrs={'rows': 5}),
        required=True,
        error_messages={'required': 'This field is required.'}
    )

    class Meta:
        model = Property
        fields = ['description']
