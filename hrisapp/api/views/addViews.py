from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *

import datetime

class addAccount(APIView):
    def post(self,request):
        
        user_id = request.data.get("user_id")
        queryset = User.objects.filter(id = user_id)
        username = []
        for username in queryset:
            username = username
        serializer = UserSerializer(username)
        username = serializer.data

        prefferedPaymentMethod_id = request.data.get("availablePaymentMethod_id")
        queryset = AvailablePaymentMethod.objects.filter(id=prefferedPaymentMethod_id)
        prefferedPaymentMethod = []
        for prefferedPaymentMethod in queryset:
            prefferedPaymentMethod = prefferedPaymentMethod
        serializer = AvailablePaymentMethodSerializer(prefferedPaymentMethod)
        prefferedPaymentMethod = serializer.data

        salaryType_id = request.data.get("salaryType_id")
        queryset = SalaryType.objects.filter(id = salaryType_id)
        salaryType = []
        for salaryType in queryset:
            salaryType = salaryType
        serializer = SalaryTypeSerializer(salaryType)
        salaryType = serializer.data

       
        bankName = request.data.get("bankName")
        bankAccountNumber = request.data.get("bankAccountNumber")
        phoneNumber = request.data.get("phoneNumber")
    
        data = {'username':username,'prefferedPaymentMethod':prefferedPaymentMethod,
        'salaryType':salaryType,'bankName':bankName,'bankAccountNumber':bankAccountNumber,'phonenumber':phoneNumber}
        serializer = CreateAccountSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addInternalDeduction(APIView):
    def post(self,request):
        
        account_id = request.data.get("account_id")
        queryset = Account.objects.filter(id = account_id)
        account = []
        for account in queryset:
            account = account
        serializer = AccountSerializer(account)
        account = serializer.data

        internalDeduction_id = request.data.get("internalDeduction_id")
        queryset = InternalDeductionType.objects.filter(id=internalDeduction_id)
        internalDeductionType = []
        for internalDeductionType in queryset:
            internalDeductionType = internalDeductionType
        serializer = InternalDeductionTypeSerializer(internalDeductionType)
        internalDeductionType = serializer.data
         
        date = request.data.get("date")
        amount = request.data.get("amount")
        description= request.data.get("description")
    
        data = {'account':account,'internalDeductionType':internalDeductionType,'deductionAmount':amount,'date':date,'description':description}
        serializer = CreateInternalDeductionSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class addAllowance(APIView):
    def post(self,request):
        
        account_id = request.data.get("account_id")
        queryset = Account.objects.filter(id = account_id)
        account = []
        for account in queryset:
            account = account
        serializer = AccountSerializer(account)
        account = serializer.data

        salaryAdditionType_id = request.data.get("salaryAdditionType_id")
        queryset = SalaryAdditionType.objects.filter(id=salaryAdditionType_id)
        salaryAdditionType = []
        for salaryAdditionType in queryset:
            salaryAdditionType = salaryAdditionType
        serializer = SalaryAdditionTypeSerializer(salaryAdditionType)
        salaryAdditionType = serializer.data
       
        amount = request.data.get("amount")
        description= request.data.get("description")
    
        data = {'account':account,'salaryAdditionType':salaryAdditionType,'additionAmount':amount,'description':description}
        serializer = CreateSalaryAdditionSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class addsalaryType(APIView):
    def post(self,request):


        commision_id = request.data.get("commision_id")
        queryset = Commision.objects.filter(id=commision_id)
        commision = []
        for commision in queryset:
            commision = commision
        serializer = CommisionSerializer(commision)
        commision = serializer.data
       
        basicPay = request.data.get("basicPay")
        name = request.data.get("name")
    
        data = {'commision':commision,'basicPay':basicPay,'name':name}
        serializer = CreateSalaryTypeSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateDraft(APIView):
    def post(self,request):

        account_id = request.data.get("account_id")
        queryset = Account.objects.filter(id = account_id)
        account = []
        for account in queryset:
            account = account
        serializer = AccountSerializer(account)
        account = serializer.data
    
        data = {'account':account}
        serializer = CreateDraftSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddUserToDepartment(APIView):
    def post(self,request):

        user_id = request.data.get("user_id")
        queryset = User.objects.filter(id = user_id)
        user = []
        for user in queryset:
            user = user
        serializer = UserSerializer(user)
        user = serializer.data

        department_id = request.data.get("department_id")
        queryset = Department.objects.filter(id = department_id)
        department = []
        for department in queryset:
            department = department
        serializer = DepartmentSerializer(department)
        department = serializer.data

        designation = request.data.get("designation")
    
        data = {'user':user,'department':department,'designation':designation}
        serializer = UserDepartmentSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckIn(APIView):
    def post(self,request):
 
        user_id = request.data.get("user_id")
        queryset = User.objects.filter(id = user_id)
        user = []
        for user in queryset:
            user = user
        serializer = UserSerializer(user)
        user = serializer.data

        now = datetime.datetime.now()
        timeIn = now.strftime("%H:%M:%S")

        data = {'user':user,'timeIn':timeIn}
        serializer = UserAttendanceSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

