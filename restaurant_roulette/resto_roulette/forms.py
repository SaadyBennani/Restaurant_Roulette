from django import forms
from .models import Business_Search


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business_Search
        fields = [
            'biz_category',
            'location',
        ]
