from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from fj_finance_tracker.core.models import Transaction, Budget, Category

#total income vs expense overall
#total income vs expense monthwise
#total spent vs budget for category
#total money per category for income and expense

class TotalTransactionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    @staticmethod
    def get(request):
        user = request.user
        month = request.query_params.get('month')
        if month is not None:
            transactions = Transaction.objects.filter(user=user, date__month=month)
        else:
            transactions = Transaction.objects.filter(user=user)
        income = transactions.filter(transaction_type='Income').aggregate(total=Sum('amount'))['total']
        expense = transactions.filter(transaction_type='Expense').aggregate(total=Sum('amount'))['total']
        return Response({'Income': income, 'Expense': expense}, status=status.HTTP_200_OK)

class CategoryBudgetView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    @staticmethod
    def get(request):
        user = request.user
        categories = Category.objects.filter(user=user)
        data = []
        for category in categories:
            budget = Budget.objects.filter(user=user, category=category).first()
            if budget is not None:
                data.append({'category': category.name, 'budget': budget.max_amount, 'spent': budget.current_amount, 'remaining': budget.remaining_amount})
        return Response(data, status=status.HTTP_200_OK)

class CategoryTransactionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    @staticmethod
    def get(request):
        user = request.user
        categories = Category.objects.filter(user=user)
        data = []
        for category in categories:
            transactions = Transaction.objects.filter(user=user, category=category)
            income = transactions.filter(transaction_type='Income').aggregate(total=Sum('amount'))['total']
            expense = transactions.filter(transaction_type='Expense').aggregate(total=Sum('amount'))['total']
            data.append({'category': category.name, 'income': income, 'expense': expense})
        return Response(data, status=status.HTTP_200_OK)