from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "name",
            "created",
            "type",
            "last_updated",
        ]

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = [
            "name",
            "balance",
            "last_updated",
            "created",
            "description",
        ]

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = [
            "category",
            "type",
            "status",
            "created",
            "value",
            "description",
            "last_updated",
            "accounts",
        ]
