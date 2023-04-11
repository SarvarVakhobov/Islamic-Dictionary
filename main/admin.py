from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from .models import Category, Words

# class WordAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Words
#         fields = "__all__"
        
# class WordAdmin(admin.ModelAdmin):
#     form = WordAdminForm

# Register your models here.
admin.site.register(Category)
admin.site.register(Words)