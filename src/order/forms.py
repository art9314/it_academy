from django import forms


class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(
        label="Additional info",
        required=True,
        widget=forms.TextInput,
        help_text = "Enter your shipping address and phone number."
        )