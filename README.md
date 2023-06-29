# DevFinder - Django Project

DevFinder is an innovative web application designed to connect developers and showcase their projects. This application serves as a platform where developers can create a comprehensive profile, add their technical skills, and share their innovative projects. Built using Django, a high-level Python Web framework, this project exhibits the robustness of Django's components and its capability in creating industry-level applications.

## Project Structure and Details
DevFinder is divided into two main Django apps, namely users and projects. Each app has its dedicated set of models, views, form handlers, utility scripts, and signal handlers.

```
├── itfinder
│   ├── settings.py        # Main configurations for the Django project
│   └── urls.py            # URL mappings for the entire project
├── media
│   ├── profiles_images    # Directory containing profile pictures of users
│   └── project_images     # Directory containing images related to projects
├── projects
│   ├── admin.py           # Admin configurations for the projects app
│   ├── forms.py           # Form declarations for handling project-related forms
│   ├── apps.py            # Basic configuration for the projects app
│   ├── models.py          # Data models related to projects
│   ├── urls.py            # URL mappings for the projects app
│   ├── views.py           # View handlers for projects related web pages
│   └── utils.py           # Utility functions used across the projects app
├── users
│   ├── admin.py           # Admin configurations for the users app
│   ├── forms.py           # Form declarations for handling user-related forms
│   ├── apps.py            # Basic configuration for the users app
│   ├── models.py          # Data models related to users
│   ├── urls.py            # URL mappings for the users app
│   ├── views.py           # View handlers for user-related web pages
│   ├── utils.py           # Utility functions used across the users app
│   └── signals.py         # Signal handlers for performing actions triggered by model changes
├── templates
│   ├── base.html          # Base template of the project
│   ├── delete_template.html 
│   ├── navbar.html        # Template for the navigation bar
│   └── pagination.html    # Template for pagination
├── users/templates/users
│   ├── account.html       # Template for the account page
│   ├── inbox.html         # Template for the inbox page
│   ├── login_register.html # Template for the login and registration page
│   ├── message.html       # Template for viewing a message
│   ├── message_form.html  # Template for the form to send a message
│   ├── profile_form.html  # Template for the form to edit a profile
│   ├── profiles.html      # Template to display list of profiles
│   ├── skill_form.html    # Template for the form to add a skill
│   └── user_profile.html  # Template to display a user profile
└── static
    ├── css                # Stylesheets for the project
    ├── js                 # Javascript files for the project
    └── images             # Static images for the project
```

## Apps

- The users app is responsible for managing user accounts, including creating new accounts, logging in, viewing profiles, and sending messages.
- The projects app is responsible for managing the projects that are showcased on the site.

## Templates

- Templates for the site are located in the templates directory and the users/templates/users directory.
- The base.html template is the main template for the site, including the site's navbar and main layout.

## Getting Started

- To get started with the DevFinder project, you'll need to first clone the repository to your local machine. After that, you can install the necessary Python dependencies and set up the Django project.


### Clone the repository
```
git clone https://github.com/username/devfinder.git
```

### Navigate into the project directory
```
cd devfinder
```
### Install Python dependencies
```
pip install -r requirements.txt
```
### Run database migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Start the Django development server
```
python manage.py runserver
```

## Contributing
If you're interested in contributing to the DevFinder project, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
