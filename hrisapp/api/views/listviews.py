from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *

#list views.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AvailablePaymentMethodList(generics.ListCreateAPIView):
    queryset = AvailablePaymentMethod.objects.all()
    serializer_class = AvailablePaymentMethodSerializer

class SalaryTypeList(generics.ListCreateAPIView):
    queryset = SalaryType.objects.all()
    serializer_class = SalaryTypeSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class SalaryAdditionTypeList(generics.ListCreateAPIView):
    queryset = SalaryAdditionType.objects.all()
    serializer_class = SalaryAdditionTypeSerializer

class SalaryAdditionList(generics.ListCreateAPIView):
    queryset = SalaryAddition.objects.all()
    serializer_class = SalaryAdditionSerializer

class GovernmentRateList(generics.ListCreateAPIView):
    queryset = GovernmentRate.objects.all()
    serializer_class = GovernmentRateSerializer

class InternalDeductionTypeList(generics.ListCreateAPIView):
    queryset = InternalDeductionType.objects.all()
    serializer_class = InternalDeductionTypeSerializer

class InternalDeductionList(generics.ListCreateAPIView):
    queryset = InternalDeduction.objects.all()
    serializer_class = InternalDeductionSerializer


class CommisionList(generics.ListCreateAPIView):
    queryset = Commision.objects.all()
    serializer_class = CommisionSerializer

class PaymentStatusList(generics.ListCreateAPIView):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer

class SalesList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

