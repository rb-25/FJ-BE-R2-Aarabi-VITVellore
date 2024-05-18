from django.urls import path
from rest_framework.routers import DefaultRouter

from fj_finance_tracker.core.views.tracking import TransactionViewSet, CreateViewCategoryView, BudgetViewSet
from fj_finance_tracker.core.views.dashboard import TotalTransactionView, CategoryBudgetView, CategoryTransactionView
from fj_finance_tracker.core.views.report import ReportView

urlpatterns = [
    path("categories/", CreateViewCategoryView.as_view(), name="create-view-category"),
    path("dashboard/total-transaction/", TotalTransactionView.as_view(), name="income-expense"),
    path("dashboard/category-budget/", CategoryBudgetView.as_view(), name="category-budget"),
    path("dashboard/category-transaction/", CategoryTransactionView.as_view(), name="category-income-expense"),
    path("report/", ReportView.as_view(), name="report"),
]

#Transaction urls
transaction_router = DefaultRouter()
transaction_router.register(r"transactions", TransactionViewSet, basename="transactions")
urlpatterns += transaction_router.urls

#Budget urls
budget_router = DefaultRouter()
budget_router.register(r"budgets", BudgetViewSet, basename="budgets")
urlpatterns += budget_router.urls
