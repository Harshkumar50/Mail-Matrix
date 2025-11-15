from django import forms
from django.contrib.auth.models import User
from .models import Mail


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password")
        p2 = cleaned.get("confirm_password")
        if p1 and p2 and p1 != p2:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned


class ComposeForm(forms.ModelForm):
    to = forms.CharField(label="To (username)")

    class Meta:
        model = Mail
        fields = ["to", "subject", "body"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Write your message..."}),
        }

    def clean_to(self):
        username = self.cleaned_data.get("to")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Receiver username not found.")
        return user




