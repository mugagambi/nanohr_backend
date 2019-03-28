from rest_framework import generics
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *


class DepartmentWithIdPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Department.objects.filter(id = self.kwargs["pk"])
        return queryset
    serializer_class = DepartmentSerializer

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
    def get_queryset(self):
        queryset = InternalDeduction.objects.filter(internalDeductionType_id = self.kwargs["pk"])
        return queryset
    serializer_class = InternalDeductionSerializer

class AccountsWithSalaryAdditionPK(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SalaryAddition.objects.filter(salaryAdditionType_id = self.kwargs["pk"])
        return queryset
    serializer_class = SalaryAdditionSerializer