import calendar
from config.celery_app import app
from django.utils import timezone

from fj_finance_tracker.core.models import Transaction, RecurringTransaction

#create task
#set next date
#save recurring transaction
#add next date on the schedule for celery

def next_month_days(date):
    """To get the number of days in next month"""
    year = date.year
    month = date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return calendar.monthrange(year, month)[1]


@app.task(name="process_recurring_transaction")
def process_recurring_transaction():
    
    """To process recurring transactions"""
    
    recurring_transactions = RecurringTransaction.objects.filter(next_date=timezone.date.today())
    for recurring_transaction in recurring_transactions:
        transaction=Transaction.objects.fileter(id=transaction)
        Transaction.objects.create(
            user=transaction.user,
            transaction_type=transaction.transaction_type,
            amount=transaction.amount,
            date=recurring_transaction.next_date,
            description=transaction.description,
            category=transaction.category
        )
        frequency_map ={
            'Yearly': 365,
            'Monthly': 30,
            'Weekly': 7,
            'Daily': 1
        }
        recurring_transaction.next_date = recurring_transaction.next_date + timezone.timedelta(days=frequency_map[recurring_transaction.frequency])
        recurring_transaction.save()