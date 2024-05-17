from rest_framework import serializers

from fj_finance_tracker.core.models import Transaction, Budget, Category


class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'description', 'category', 'date', 'transaction_type', 'category_name']
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ['user']
        
class BudgetSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Budget
            fields = ['id', 'category', 'max_amount', 'current_amount', 'remaining_amount']