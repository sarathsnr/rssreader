from django import forms


from .models import Urllist


class UrlForm(forms.ModelForm):
    class Meta:
        model = Urllist
        fields = [
	    "title",
            "url",
            ]
