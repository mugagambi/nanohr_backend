from rest_framework import generics
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *
#TODO change views name to userdetailList 

class GeneralDetail(generics.ListCreateAPIView):
    '''
        get:
        get details for user with id pk

    '''
    def get_queryset(self):
        queryset = User.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = UserSerializer

class AccountList(generics.ListCreateAPIView):
    '''
        get:
        get account detail for account with id <pk>
    '''

    def get_queryset(self):
        queryset = Account.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = AccountSerializer

class SalaryAdditionList(generics.ListCreateAPIView):
    '''
    get:
    get salary addition detail for account with id <pk>
    '''
    def get_queryset(self):
        queryset = SalaryAddition.objects.filter(account_id = self.kwargs["pk"])
        return queryset
    serializer_class = SalaryAdditionSerializer

class InternalDeductionList(generics.ListCreateAPIView):
    '''
        get:
        get internal deduction detail for account with id <pk>
    '''
    def get_queryset(self):
        queryset = InternalDeduction.objects.filter(account_id = self.kwargs["pk"])
        return queryset
    serializer_class = InternalDeductionSerializer



class PaymentStatusList(generics.ListCreateAPIView):
    '''
        get:
        get summary detail for account with id <pk>
    '''
    def get_queryset(self):
        queryset = PaymentStatus.objects.filter(account_id = self.kwargs["pk"])
        return queryset
    serializer_class = PaymentStatusSerializer


class SalaryTypeList(generics.ListCreateAPIView):
    '''
        get:
        get salary type detail for user with id <pk>
    '''
    def get_queryset(self):
        queryset = SalaryType.objects.filter(username_id = self.kwargs["pk"])
        return queryset
    serializer_class = SalaryTypeSerializer

class EducationList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Education.objects.filter(username_id = self.kwargs["pk"])
        return queryset
    serializer_class = EducationSerializer

