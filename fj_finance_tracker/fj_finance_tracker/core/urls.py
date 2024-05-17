from django.urls import path
from rest_framework.routers import DefaultRouter

from fj_finance_tracker.core.views.tracking import TransactionViewSet, CreateViewCategoryView, BudgetViewSet

urlpatterns = [
    path("categories/", CreateViewCategoryView.as_view(), name="create-view-category"),
]

#Transaction urls
transaction_router = DefaultRouter()
transaction_router.register(r"transactions", TransactionViewSet, basename="transactions")
urlpatterns += transaction_router.urls

#Budget urls
budget_router = DefaultRouter()
budget_router.register(r"budgets", BudgetViewSet, basename="budgets")
urlpatterns += budget_router.urls
