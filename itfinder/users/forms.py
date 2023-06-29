# Here, we import the necessary modules for creating forms in Django.
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message

# This class defines a form that inherits from Django's UserCreationForm. The form is customized for User model instance creation.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # The model associated with the form is the User model.
        model = User
        # The fields to be included in the form.
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        # Customize the labels for the form fields.
        labels = {
            'first_name': 'Name',
        }

    # Custom initialization of the form to update widget attributes.
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# A form for creating and updating Profile model instances.
class ProfileForm(ModelForm):
    class Meta:
        # The model associated with the form is the Profile model.
        model = Profile
        # The fields to be included in the form.
        fields = ['name', 'email', 'username', 'city', 'bio', 'intro', 'image', 'github', 'linkedin', 'twitter', 'youtube', 'website']

    # Custom initialization of the form to update widget attributes.
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# A form for creating and updating Skill model instances.
class SkillForm(ModelForm):
    class Meta:
        # The model associated with the form is the Skill model.
        model = Skill
        # All fields from the model are included in the form, except 'owner'.
        fields = '__all__'
        exclude = ['owner']

    # Custom initialization of the form to update widget attributes.
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# A form for creating and updating Message model instances.
class MessageForm(ModelForm):
    class Meta:
        # The model associated with the form is the Message model.
        model = Message
        # The fields to be included in the form.
        fields = ['name', 'email', 'subject', 'body']

    # Custom initialization of the form to update widget attributes.
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})




