from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import UserPreferences


admin.site.register(UserPreferences)
