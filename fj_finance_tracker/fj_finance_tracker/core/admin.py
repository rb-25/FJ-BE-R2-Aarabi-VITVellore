from django.contrib import admin
from .models import Transaction, Category, Budget,RecurringTransaction,SplitExpense 

# Register your models here.
admin.site.register(Transaction)
admin.site.register(SplitExpense)
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(RecurringTransaction)