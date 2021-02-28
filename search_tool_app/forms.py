from django import forms
import datetime
from .models import Type, Year, Language, Paper, Material, PaperUsedMaterial, Tag


class PaperForm(forms.ModelForm):
    title = forms.CharField(label='Publications Title', max_length=200,)
    abstract = forms.Textarea()
    reviewed = forms.BooleanField(initial=False, required=False)
    # date_added = forms.DateField(widget=forms.HiddenInput, required=False)
    year_id = forms.ModelChoiceField(queryset=Year.objects.all(), blank=False)
    type_id = forms.ModelChoiceField(queryset=Type.objects.all(), blank=False)
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), blank=False)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), blank=False)
    material = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), blank=False)

    class Meta:
        model = Paper
        fields = '__all__'
        exclude = ('date_added',)


class TypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, help_text="Please enter the type's name")

    class Meta:
        model = Type
        fields = ('type',)


class LanguageForm(forms.ModelForm):
    language = forms.CharField(max_length=100, help_text="Please enter the language")

    class Meta:
        model = Language
        fields = ('language',)

