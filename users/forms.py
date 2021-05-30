from django import forms
from .models import Users


class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('first_name','last_name','address','area_code','mobile', 'user_type')
        labels = {
            'First Name':'first_name',
            'Mobile':'mobile'
        }

    def __init__(self, *args, **kwargs):
        super(UsersForm,self).__init__(*args, **kwargs)
        self.fields['user_type'].empty_label = "Select"
        self.fields['mobile'].required = True
