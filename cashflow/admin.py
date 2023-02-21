from django.contrib import admin
from django import forms

from . import models


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "name",
        "created",
        "type",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "created",
        "type",
        "last_updated",
    ]


class AccountAdminForm(forms.ModelForm):

    class Meta:
        model = models.Account
        fields = "__all__"


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    list_display = [
        "name",
        "balance",
        "last_updated",
        "created",
        "description",
    ]
    readonly_fields = [
        "name",
        "balance",
        "last_updated",
        "created",
        "description",
    ]


class TransactionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Transaction
        fields = "__all__"


class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = [
        "category",
        "type",
        "status",
        "created",
        "value",
        "description",
        "last_updated",
        "get_accounts",
    ]
    readonly_fields = [
        "category",
        "type",
        "status",
        "created",
        "value",
        "description",
        "last_updated",
        "accounts",
    ]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
