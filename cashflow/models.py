from django.db import models
from django.urls import reverse
from django import template

register = template.Library()


TRANSACTION_STATUS = (
        ('P', 'Paid'),
        ('U', 'Unpaid'),
    )
TRANSACTION_TYPE = (
        ('E', 'Expense'),
        ('I', 'Incame'),
        ('T', 'Transfer'),
    )

class Category(models.Model):

    # Fields
    name = models.TextField(max_length=40)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.CharField(max_length=30, choices=TRANSACTION_TYPE)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_pk(self):
        return self.pk
        
    def get_absolute_url(self):
        return reverse("cashflow:Category_detail", args=(self.pk,))

    # def get_pk(self):
    #     return reverse("cashflow:Category_create")

    def get_list_url(self):
        return reverse("cashflow:Category_list", args=(self.pk,))

    def get_update_url(self):
        return reverse("cashflow:Category_update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("cashflow:Category_delete", args=(self.pk,))

    # @register.filter(name='getattr')
    # def get_attr(self, attr):
    #     if attr is not None:
    #         return self.get_attr(self, attr)
    #     else:
    #         return self.__str__()

class Account(models.Model):

    # Fields
    name = models.CharField(max_length=80)
    balance = models.DecimalField(max_digits=30, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_pk(self):
        return self.pk
    
    def get_absolute_url(self):
        return reverse("cashflow:Account_detail", args=(self.pk,))

    def get_list_url(self):
        return reverse("cashflow:Account_list", args=(self.pk,))

    def get_update_url(self):
        return reverse("cashflow:Account_update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("cashflow:Account_delete", args=(self.pk,))

    def get_attrs(self):
        return [attr for attr in self.__dict__.keys()]
    
    def register_incame(self, value):
        if value > 0:
            self.balance += value
            return f"New Balance: {self.balance}" # wil return True in future
        else:
            return f'ERRO'
        

    def register_expanse(self, value):
        if value > 0 and value < self.balance:
            self.balance -= value
            return f"New Balance: {self.balance}" # wil return True in future
        elif value > self.balance:
            return f"Insufficient funds"
        else:
            return f'ERRO'

class Transaction(models.Model):

    # Fields
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPE)
    status = models.CharField(max_length=2, choices=TRANSACTION_STATUS)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    value = models.DecimalField(max_digits=30, decimal_places=2)
    description = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    accounts = models.ManyToManyField(Account)

    class Meta:
        pass

    def __str__(self):
        return str(self.description)

    def get_pk(self):
        return self.pk
 
    def get_absolute_url(self):
        return reverse("cashflow:Transaction_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cashflow:Transaction_update", args=(self.pk,))

    def get_list_url(self):
        return reverse("cashflow:Transaction_list", args=(self.pk,))

    def get_delete_url(self):
        return reverse("cashflow:Transaction_delete", args=(self.pk,))
    
    def get_accounts(self):
        return "\n".join([ac.accounts for ac in self.accounts.all()])

    def get_attrs(self):
        return [attr for attr in self.__dict__.keys()]
 