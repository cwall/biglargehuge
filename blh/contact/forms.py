from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=200)
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'you@awesomeco.com'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'We love your work and would like to give you money to do cool things all day'}), required=True)