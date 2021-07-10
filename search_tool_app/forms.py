from django import forms
import datetime
from .models import Type, Year, Language, Paper, Material, PaperUsedMaterial, Tag


class PaperForm(forms.ModelForm):
    title = forms.CharField(label='Publications Title', max_length=400,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          }))
    reviewed = forms.BooleanField(initial=False, required=False)
    pdf = forms.FileField(label="PDF file", required=False, widget=forms.FileInput(attrs={'class': 'form-control',
                                                                                          }))
    year_id = forms.ModelChoiceField(queryset=Year.objects.all(), blank=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    type_id = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), blank=False, widget=forms.CheckboxSelectMultiple)
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), blank=False, widget=forms.CheckboxSelectMultiple)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), blank=False, widget=forms.CheckboxSelectMultiple)
    material = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), blank=False, widget=forms.CheckboxSelectMultiple)
    abstract = forms.Textarea()

    class Meta:
        model = Paper
        fields = '__all__'
        exclude = ('date_added', 'slug')


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


class SearchForm(forms.Form):
    title = forms.CharField(max_length=200,
                            required=False, widget=forms.TextInput)

    year = forms.ModelMultipleChoiceField(queryset=Year.objects.all(),
                                          required=False,
                                          widget=forms.CheckboxSelectMultiple)

    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
                                          required=False,
                                          widget=forms.CheckboxSelectMultiple)

    #     type = forms.ModelChoiceField(queryset=Type.objects.all(),
    #                                   required=False,
    #                                   widget=forms.CheckboxSelectMultiple) DO NOT KNOW WHY THIS WAS FIXED BY THE ABOVE

    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(),
                                              required=False,
                                              widget=forms.CheckboxSelectMultiple)

    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                         required=False,
                                         widget=forms.CheckboxSelectMultiple)

    material = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
                                              required=False,
                                              widget=forms.CheckboxSelectMultiple)

    # material_used = forms.ModelMultipleChoiceField(queryset=PaperUsedMaterial.objects.exclude())
    abstract = forms.Textarea()
