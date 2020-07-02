from django.contrib import admin
from banks.models import Bank, Branch
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BankResource(resources.ModelResource):
    class Meta:
        model = Bank


class BranchResource(resources.ModelResource):
    class Meta:
        model = Branch
        exclude = ("id",)
        import_id_fields = ("ifsc",)


class BankAdmin(ImportExportModelAdmin):
    resource_class = BankResource


class BranchAdmin(ImportExportModelAdmin):
    resource_class = BranchResource


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
