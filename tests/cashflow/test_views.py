import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Category_list_view(client):
    instance1 = test_helpers.create_cashflow_Category()
    instance2 = test_helpers.create_cashflow_Category()
    url = reverse("cashflow_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view(client):
    url = reverse("cashflow_Category_create")
    data = {
        "name": "text",
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view(client):
    instance = test_helpers.create_cashflow_Category()
    url = reverse("cashflow_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view(client):
    instance = test_helpers.create_cashflow_Category()
    url = reverse("cashflow_Category_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Account_list_view(client):
    instance1 = test_helpers.create_cashflow_Account()
    instance2 = test_helpers.create_cashflow_Account()
    url = reverse("cashflow_Account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Account_create_view(client):
    url = reverse("cashflow_Account_create")
    data = {
        "name": "text",
        "balance": 1.0,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Account_detail_view(client):
    instance = test_helpers.create_cashflow_Account()
    url = reverse("cashflow_Account_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Account_update_view(client):
    instance = test_helpers.create_cashflow_Account()
    url = reverse("cashflow_Account_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "balance": 1.0,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Transaction_list_view(client):
    instance1 = test_helpers.create_cashflow_Transaction()
    instance2 = test_helpers.create_cashflow_Transaction()
    url = reverse("cashflow_Transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Transaction_create_view(client):
    url = reverse("cashflow_Transaction_create")
    data = {
        "type": "text",
        "status": "text",
        "value": 1.0,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Transaction_detail_view(client):
    instance = test_helpers.create_cashflow_Transaction()
    url = reverse("cashflow_Transaction_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Transaction_update_view(client):
    instance = test_helpers.create_cashflow_Transaction()
    url = reverse("cashflow_Transaction_update", args=[instance.pk, ])
    data = {
        "type": "text",
        "status": "text",
        "value": 1.0,
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
