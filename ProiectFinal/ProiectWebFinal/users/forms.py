from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']   #daca vreau sa mai adaug un field aici?

        # widgets = {
        #     'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form_control'})   #Varianta numarul 1 de form control
        #     }

    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class']='form-control'                                  #Varianta numarul 2 de form control

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        if User.objects.filter(email = email_value).exists():
            self._errors['email'] = self.error_class(["Email address already in use. Have you forgotten your password?"])
        return field_data