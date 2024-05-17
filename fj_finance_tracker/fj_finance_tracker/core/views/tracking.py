from django.utils import timezone
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from fj_finance_tracker.core.models import Transaction, Budget, Category

from fj_finance_tracker.core.serializers import  TransactionSerializer, BudgetSerializer, CategorySerializer

class CreateViewCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    @staticmethod
    def post(request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save(user=request.user)
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
    
    @staticmethod
    def get(request):
        categories = Category.objects.filter(user=request.user)
        type = request.query_params.get('type')
        if type:
            categories = categories.filter(type=type)
        return Response(CategorySerializer(categories, many=True).data, status=status.HTTP_200_OK)
    
class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class BudgetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    
    def perform_create(self, serializer):
        Budget.objects.update_or_create(user=self.request.user, category=serializer.validated_data['category'], defaults={'max_amount': serializer.validated_data['max_amount']})
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    

    