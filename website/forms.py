from django import forms
from website.models import contact,NewsLetter


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = contact
        fields ='__all__'

   

class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'