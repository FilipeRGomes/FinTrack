from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "type",
        ]


class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = [
            "name",
            "balance",
            "description",
        ]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = [
            "type",
            "status",
            "value",
            "description",
            "accounts",
            "category"
        ]
