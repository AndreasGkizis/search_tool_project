from django import forms
from search_tool_app.models import Type, Year, Language, Papers, Materials, PaperUsedMaterial, Tags


class PapersForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Enter the title of the publication ")
    abstract = forms.CharField(max_length=1000, help_text="Enter the abstract of the publication ")
    reviewed = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    date_added = forms.DateField(widget=forms.HiddenInput())

    class Meta:
        model = Papers
        fields = ('Title',)

