from django import forms
from .models import TeamMember

class TeamForm(forms.ModelForm):

    class Meta:
        model = TeamMember
        fields = ("firstname", "lastname", "email", "mobile")
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email',
            'mobile': 'Mobile Number'
        }

        # firstname = forms.CharField(max_length = 100)
        # lastname = forms.CharField(max_length = 100)
        # email = forms.EmailField(max_length = 254)
        # mobile = forms.CharField(max_length = 100)
        # role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

