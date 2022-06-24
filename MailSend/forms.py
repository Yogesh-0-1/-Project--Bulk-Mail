from django import forms

from BulkMail.MailSend.models import Login
class UserForm(forms.ModelForm):
    class Meta:
        model = Login
        widgets = {
        'Password': forms.PasswordInput(),
    }