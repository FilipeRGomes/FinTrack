import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from cashflow import models as cashflow_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_cashflow_Category(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["type"] = ""
    defaults.update(**kwargs)
    return cashflow_models.Category.objects.create(**defaults)
def create_cashflow_Account(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["balance"] = ""
    defaults["description"] = ""
    defaults.update(**kwargs)
    return cashflow_models.Account.objects.create(**defaults)
def create_cashflow_Transaction(**kwargs):
    defaults = {}
    defaults["type"] = ""
    defaults["status"] = ""
    defaults["value"] = ""
    defaults["description"] = ""
    defaults["name"] = "text"
    defaults["balance"] = 1.0
    defaults["last_updated"] = datetime.now()
    defaults["created"] = datetime.now()
    defaults["description"] = "text"
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["type"] = "text"
    defaults["last_updated"] = datetime.now()
    defaults.update(**kwargs)
    return cashflow_models.Transaction.objects.create(**defaults)
