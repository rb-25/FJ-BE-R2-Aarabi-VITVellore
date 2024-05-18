from django.utils import timezone
from django.core.mail import send_mail
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from fj_finance_tracker.core.models import Transaction, SplitExpense
from fj_finance_tracker.users.models import User

from fj_finance_tracker.core.serializers import  SplitExpenseSerializer

class CreateSplitExpenseView(APIView):
        
        """To split expenses among users"""
        
        def post(self, request):
            amount = request.data.get('amount')
            user_emails = request.data.get('user_emails')
            paid_by = request.data.get('paid_by')
            split_amount = amount/len(user_emails)
            paid_by_user = User.objects.get(email=paid_by)
            split_expense = SplitExpense.objects.create(paid_by=paid_by_user, amount=split_amount)

            # Add users to the split_expense
            for email in user_emails:
                user = User.objects.get(email=email)
                split_expense.users.add(user)
                if paid_by_user == user:
                    split_expense.settled = True

            # Save the split_expense instance
            split_expense.save()
            return Response({"message": f"Expense {split_amount} split successfully"}, status=status.HTTP_201_CREATED)

class SettleSplitExpenseView(APIView):
    
    """To settle split expenses"""
    
    def post(self, request):
        split_expense_id = request.data.get('split_expense_id')
        split_expense = SplitExpense.objects.get(id=split_expense_id)
        split_expense.settled = True
        split_expense.save()
        Transaction.objects.create(users=split_expense.user, transaction_type='Expense', amount=split_expense.amount, description=f"Settled split expense {split_expense_id}")
        return Response({"message": f"Split expense {split_expense_id} settled successfully"}, status=status.HTTP_200_OK)

class SplitExpenseViewSet(ReadOnlyModelViewSet):
    
    perimission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    #To view split expenses
    queryset=SplitExpense.objects.all()
    serializer_class = SplitExpenseSerializer
    
    def get_queryset(self):
        return SplitExpense.objects.filter(users=self.request.user)
    
    
    