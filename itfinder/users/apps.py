from django.apps import AppConfig


# Define a new class named UsersConfig, which is inheriting from AppConfig.
class UsersConfig(AppConfig):
    # This line defines the default field type for auto generated fields as BigAutoField.
    default_auto_field = 'django.db.models.BigAutoField'
    # This line sets the name of the app to 'users'.
    name = 'users'

    # The ready() method is overridden here to allow importing and registering signals from the 'users' app.
    def ready(self):
        import users.signals

