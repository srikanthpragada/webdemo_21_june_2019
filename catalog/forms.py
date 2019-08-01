from django import forms


class PublisherForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    contact = forms.CharField(label="Contacts", max_length=50, required=False)
