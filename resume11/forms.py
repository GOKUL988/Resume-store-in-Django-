from django import forms
from .models import per
from .models import aca
from .models import cc
class person (forms.ModelForm):
    class Meta:
        model=per
        fields=[
            "perid",
            "name",
            "ph_no",
            "mail",
            "dob",
            "sx",
            "ambition",
            "lan",
            "add"
        ]

class qualf(forms.ModelForm):
    class Meta:
        model=aca
        fields=["cs","sch_clg","uni","year","per"]

class cer(forms.ModelForm):
    class Meta:
        model=cc
        fields=[
            "cer",
        ]