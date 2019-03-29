from rest_framework import generics
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *

from datetime import date 


class DepartmentWithIdPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Department.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = DepartmentSerializer

class InternalDeductionTypeWithIdPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = InternalDeductionType.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = InternalDeductionTypeSerializer

class salaryAdditionTypeWithIdPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SalaryAdditionType.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = SalaryAdditionTypeSerializer

class EmployeesInDepartmentPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = UserDepartment.objects.filter(department_id = self.kwargs["pk"])
        return queryset
    serializer_class = UserDepartmentSerializer

class AccountsWithSalaryTypePK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Account.objects.filter(salaryType_id = self.kwargs["pk"])
        return queryset
    serializer_class = AccountSerializer

class AccountsWithSalaryTypePK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Account.objects.filter(salaryType_id = self.kwargs["pk"])
        return queryset
    serializer_class = AccountSerializer

class AccountsWithPrefferedPaymentmethodPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Account.objects.filter(prefferedPaymentMethod_id = self.kwargs["pk"])
        return queryset
    serializer_class = AccountSerializer

class AccountsWithCommisiontypePK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Account.objects.filter(commision_id = self.kwargs["pk"])
        return queryset
    serializer_class = AccountSerializer

class AccountsWithInternalDeductionPK(generics.ListCreateAPIView):
    today = date.today()
    day = today.day
    month = today.month
    year = today.year
    def get_queryset(self):
        queryset = InternalDeduction.objects.filter(internalDeductionType_id = self.kwargs["pk"],date__year=self.year, date__month=self.month)
        return queryset
    serializer_class = InternalDeductionSerializer

class AccountsWithSalaryAdditionPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SalaryAddition.objects.filter(salaryAdditionType_id = self.kwargs["pk"])
        return queryset
    serializer_class = SalaryAdditionSerializer