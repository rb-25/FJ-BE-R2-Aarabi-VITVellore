import csv
from datetime import datetime
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from fj_finance_tracker.core.models import Transaction, Budget, Category
from fj_finance_tracker.core.serializers import TransactionSerializer

class ReportView(APIView):
    
    """To generate report(csv file) of transactions"""
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get (self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        if not start_date or not end_date:
            start_date = datetime.now().strftime("%Y-%m-01")
            end_date = datetime.now().strftime("%Y-%m-%d")
            
        transactions = Transaction.objects.filter(
            date__gte=start_date, date__lte=end_date, user=request.user
        )
        transactions_serializer = TransactionSerializer(transactions, many=True)

        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="export.csv"'},
        )

        #csv file with the data
        writer = csv.writer(response)
        writer.writerow(["Date", "Category", "Amount", "Description,Type"])
        for transaction in transactions_serializer.data:
            writer.writerow(
                [
                    transaction["date"],
                    #transaction["category_name"],
                    transaction["amount"],
                    transaction["description"],
                    transaction["transaction_type"],
                ]
            )
        
        #return csv file 
        return response
        