from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Category", api.CategoryViewSet)
router.register("Account", api.AccountViewSet)
router.register("Transaction", api.TransactionViewSet)

app_name = 'cashflow' #Used to specify what app the url belongs in template

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Category/", views.CategoryListView.as_view(), name="Category_list"),
    path("Category/create/", views.CategoryCreateView.as_view(), name="Category_create"),
    path("Category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="Category_detail"),
    path("Category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="Category_update"),
    path("Category/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="Category_delete"),
    path("Account/", views.AccountListView.as_view(), name="Account_list"),
    path("Account/create/", views.AccountCreateView.as_view(), name="Account_create"),
    path("Account/detail/<int:pk>/", views.AccountDetailView.as_view(), name="Account_detail"),
    path("Account/update/<int:pk>/", views.AccountUpdateView.as_view(), name="Account_update"),
    path("Account/delete/<int:pk>/", views.AccountDeleteView.as_view(), name="Account_delete"),
    path("Transaction/", views.TransactionListView.as_view(), name="Transaction_list"),
    path("Transaction/create/", views.TransactionCreateView.as_view(), name="Transaction_create"),
    path("Transaction/detail/<int:pk>/", views.TransactionDetailView.as_view(), name="Transaction_detail"),
    path("Transaction/update/<int:pk>/", views.TransactionUpdateView.as_view(), name="Transaction_update"),
    path("Transaction/delete/<int:pk>/", views.TransactionDeleteView.as_view(), name="Transaction_delete"),
)
