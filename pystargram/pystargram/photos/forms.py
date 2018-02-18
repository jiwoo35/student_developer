from __future__ import unicode_literals
from django import forms
from .models import Photo

# forms.ModelForm = models.py
class PhotoForm(forms.ModelForm):
    # Meta: 실제로 내용 반영X -> 추상화
    class Meta:
        model = Photo
        fields = ('image', 'content', )
