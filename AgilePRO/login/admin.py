from django.contrib import admin
from django.contrib.auth.models import Permission

"""Se agrega el ABM de Permisos en el sitio Admin."""
admin.site.register(Permission)
