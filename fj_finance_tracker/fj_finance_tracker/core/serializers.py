from rest_framework import serializers

from fj_finance_tracker.core.models import Transaction, Budget, Category, SplitExpense, RecurringTransaction


class TransactionSerializer(serializers.ModelSerializer):
    receipt = serializers.ImageField(allow_empty_file=True, required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'description', 'category', 'date', 'transaction_type', 'category_name','receipt']
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ['user']
        
class BudgetSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Budget
            fields = ['id', 'category', 'max_amount', 'current_amount', 'remaining_amount']

class SplitExpenseSerializer(serializers.ModelSerializer):
    
    user_email=serializers.EmailField(source='users.email', read_only=True)
    paid_by_email=serializers.EmailField(source='paid_by.email', read_only=True)
    
    class Meta:
        model = SplitExpense
        fields = ['id', 'user_email', 'amount', 'paid_by_email', 'settled']

class RecurringTransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=RecurringTransaction
        fields="__all__"