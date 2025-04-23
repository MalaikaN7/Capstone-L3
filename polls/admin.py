# Imports Django's admin module for registering models to the admin site.
from django.contrib import admin
# Imports the Question and Choice models from the current app's models.
from .models import Question, Choice

# Registers the Question model with the admin site, allowing it to be managed through the admin interface.
admin.site.register(Question)
# Registers the Choice model with the admin site, allowing it to be managed through the admin interface.
admin.site.register(Choice)
