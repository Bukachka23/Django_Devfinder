from django.contrib import admin
from .models import Profile, Skill

# This line registers the Profile model with Django's admin site.
# This allows the model to be managed via the admin interface.
admin.site.register(Profile)

# This line registers the Skill model with Django's admin interface.
# This allows the model to be managed via the admin interface.
admin.site.register(Skill)

