from import_export import resources
from .models import details

class DetailsResource(resources.ModelResource):
    class Meta:
        model = details