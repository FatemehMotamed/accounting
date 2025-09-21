from django import forms

class DateForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date", 
            "class": "border px-3 py-2 rounded w-full"
        })
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date", 
            "class": "border px-3 py-2 rounded w-full"
        })
    )
