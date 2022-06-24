
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import details,Login

# Model , ImportExport Regisration  
@admin.register(details)
@admin.register(Login)
class PersonAdmin(ImportExportModelAdmin):
    pass