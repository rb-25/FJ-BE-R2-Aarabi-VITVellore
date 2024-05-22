from django.utils import timezone
from django.core.mail import send_mail
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from fj_finance_tracker.core.models import Transaction,RecurringTransaction

from fj_finance_tracker.core.serializers import  RecurringTransactionSerializer

class RecurringTransactionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    queryset = RecurringTransaction.objects.all()
    serializer_class = RecurringTransactionSerializer
    