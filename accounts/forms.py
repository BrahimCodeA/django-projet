from django import forms

class ContactForm(forms.Form):
    utilisateur = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur", 'class': 'w-full p-2 border rounded-md'}),
        max_length=128
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'w-full p-2 border rounded-md'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Entrez votre message ... ', 'class': 'w-full p-2 border rounded-md'})
    )
