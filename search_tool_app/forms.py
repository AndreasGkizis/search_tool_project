from django import forms
import datetime
from search_tool_app.models import Type, Year, Language, Paper, Material, PaperUsedMaterial, Tag


class PaperForm(forms.ModelForm):
    title = forms.CharField(label='Publications Title', max_length=200, help_text="Enter the title of the publication ")
    abstract = forms.CharField(max_length=1000, help_text="Enter the abstract of the publication ")
    reviewed = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    date_added = forms.DateField(initial=datetime.date.today())

    class Meta:
        model = Paper
        fields = ('title', 'abstract',)
        exclude = ('year_id', 'type_id', 'language', 'reviewed', )


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

