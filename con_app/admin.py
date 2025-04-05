from django.contrib import admin
from .models import Construction,Seller,EnvironmentalCondition
from import_export.admin import  ImportExportModelAdmin
from import_export import resources
class Con(admin.ModelAdmin):
    list_display = ["ConstructionType"	,"ConstructionName" ,
                    "CementQuality"	,"CementPrice",
                    "BrickQuality"	,"BrickPrice",
                    "SandQuality",	"SandPrice" , "Seller"]
class ConstructionResource(resources.ModelResource):
    class Meta:
        model = Construction


@admin.register(Construction)
class ConstructionAdmin(ImportExportModelAdmin,Con):
    resource_class = ConstructionResource


admin.site.register(Seller)
admin.site.register(EnvironmentalCondition)