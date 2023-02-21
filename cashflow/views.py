from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.views.generic.detail import SingleObjectMixin


from . import models
from . import forms
# CBV Documentation: http://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/CreateView/

class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm    
    template_name = 'list.html'
    context_object_name = 'list' #Returned by queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [field.name for field in self.model._meta.fields]
        context['model_name'] = 'Category'
        context['url'] = 'cashflow:Category_create'
        return context

class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Create'
        context['model_name'] = 'Category'
        context['url'] = 'cashflow:Category_create'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('operation_success.html')) 


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'account_detail.html'
    context_object_name = 'content' # name of object used in context


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    pk_url_kwarg = "pk"
    template_name = 'update_form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Update'
        context['model_name'] = 'Category'
        #context['url'] = 'cashflow:Account_update'
        return context

    # Estudar mais os metodos especiais do django
    def dispatch(self, *args, **kwargs):
        self.category_id = kwargs['pk']
        return super(CategoryUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        account = models.Category.objects.get(id=self.category_id)
        return HttpResponse(render_to_string('operation_success.html', {'account': account}))    



class CategoryDeleteView(generic.DeleteView):
    model = models.Category
    success_url = reverse_lazy("cashflow:Category_list")
    template_name = 'confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Delete'
        context['model_name'] = 'Category'
        context['url'] = 'cashflow:Category_delete'
        return context
    
    def dispatch(self, *args, **kwargs):
        self.category_id = kwargs['pk']
        return super(CategoryDeleteView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        category = models.Category.objects.get(id=self.category_id)
        category.delete()
        return HttpResponse(render_to_string('operation_success.html', {'category': category})) 


class AccountListView(generic.ListView):
    model = models.Account
    form_class = forms.AccountForm
    template_name = 'list.html'
    context_object_name = 'list' #Returned by queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [field.name for field in self.model._meta.fields]
        context['url'] = 'cashflow:Account_create'
        return context

class AccountCreateView(generic.CreateView):
    model = models.Account
    form_class = forms.AccountForm
    template_name = 'form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Create'
        context['model_name'] = 'Account'
        context['url'] = 'cashflow:Account_create'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super(AccountCreateView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('operation_success.html')) 


class AccountDetailView(generic.DetailView):
    model = models.Account
    form_class = forms.AccountForm
    template_name = 'account_detail.html'
    context_object_name = 'content' # name of object used in context


class AccountUpdateView(generic.UpdateView):
    model = models.Account
    form_class = forms.AccountForm
    pk_url_kwarg = "pk"
    template_name = 'update_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Update'
        context['model_name'] = 'Account'
        #context['url'] = 'cashflow:Account_update'
        return context

    # Estudar mais os metodos especiais do django
    def dispatch(self, *args, **kwargs):
        self.account_id = kwargs['pk']
        return super(AccountUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        account = models.Account.objects.get(id=self.account_id)
        return HttpResponse(render_to_string('operation_success.html', {'account': account}))    


class AccountDeleteView(generic.DeleteView):
    model = models.Account
    success_url = reverse_lazy("cashflow:Account_list")
    template_name = 'confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Delete'
        context['model_name'] = 'Account'
        context['url'] = 'cashflow:Account_delete'
        return context
    
    def dispatch(self, *args, **kwargs):
        self.account_id = kwargs['pk']
        return super(AccountDeleteView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        account = models.Account.objects.get(id=self.account_id)
        account.delete()
        return HttpResponse(render_to_string('operation_success.html', {'account': account})) 

class TransactionListView(generic.ListView):
    model = models.Transaction
    form_class = forms.TransactionForm
    template_name = 'list.html'
    context_object_name = 'list' #Returned by queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        #context['operation_type'] = 'Create'
        #context['model_name'] = 'Category'
        #obj = super(SingleObjectMixin, self).get_object()
        #context['fields'] = models.Transaction.objects.
        #context['fields'] = [field.name for field in self.model._meta.fields]
        context['fields'] = ["type", "status", "value", "accounts", "category"]
        context['url'] = 'cashflow:Transaction_create'
        return context


class TransactionCreateView(generic.CreateView):
    model = models.Transaction
    form_class = forms.TransactionForm
    template_name = 'form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add extra informations
        context['operation_type'] = 'Create'
        context['model_name'] = 'Transaction'
        context['url'] = 'cashflow:Transaction_create'
        return context
    
    def dispatch(self, *args, **kwargs):
        return super(TransactionCreateView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('operation_success.html')) 


class TransactionDetailView(generic.DetailView):
    model = models.Transaction
    form_class = forms.TransactionForm


class TransactionUpdateView(generic.UpdateView):
    model = models.Transaction
    form_class = forms.TransactionForm
    pk_url_kwarg = "pk"


class TransactionDeleteView(generic.DeleteView):
    model = models.Transaction
    success_url = reverse_lazy("cashflow:Transaction_list")
