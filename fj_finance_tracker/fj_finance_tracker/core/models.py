from django.utils import timezone
from django.db import models
from fj_finance_tracker.users.models import User

# Create your models here.
class SplitExpense(models.Model):
    
    """To split expenses among users"""
    
    amount = models.FloatField()
    users = models.ManyToManyField(User,related_name='participating_in')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_by')
    settled = models.BooleanField(default=False)
    
class Transaction(models.Model):
    
    """To store transactions made by user"""
    
    TRANSACTION_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    receipt = models.ImageField(upload_to='receipts/',null=True) 
    
    @property
    def category_name(self):
        return self.category.name
    
class Category(models.Model):
        
        """To store categories of income and expenses"""
        
        TRANSACTION_CHOICES = [
            ('Income', 'Income'),
            ('Expense', 'Expense'),
        ]
        
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
        name = models.CharField(max_length=255)

class Budget(models.Model):
    
    """To store budget for each category of expense for a user"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    max_amount = models.FloatField()
    
    @property
    def current_amount(self):
        transactions = Transaction.objects.filter(user=self.user, transaction_type='Expense', category=self.category, date__month=timezone.now().month)
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return total
    
    @property
    def remaining_amount(self):
        return self.max_amount - self.current_amount

class RecurringTransaction (models.Model):
    
    """To store recurring transactions"""
    
    FREQUENCY_CHOICES=(
        ('Yearly','Yearly'),
        ('Monthly','Monthly'),
        ('Weekly','Weekly'),
        ('Daily','Daily')
    )
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    frequency=models.CharField(max_length=100,choices=FREQUENCY_CHOICES)
    start_date=models.DateField()
    end_date=models.DateField(null=True)
    next_transaction=models.DateField()