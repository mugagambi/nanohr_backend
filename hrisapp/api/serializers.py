from rest_framework import serializers
#TODO import a single at a time
from hrisapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

import datetime

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email',)
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class UserAttendanceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserAttendance
        fields = ('id','user','date','timeIn','timeOut','weekday')
    def create(self,validated_data):

        user_data = validated_data.pop('user')
        user = {}
        user = User.objects.get(**user_data)
    
        userAttendance = UserAttendance.objects.create(user=user,**validated_data)
        return userAttendance
    def update(self,instance,validated_data):

        now = datetime.datetime.now()
        timeOut = now.strftime("%H:%M:%S")
    
        userAttendance = instance
        userAttendance.timeOut = timeOut
        userAttendance.save()

        return userAttendance 

class LeavesAndHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeavesAndHoliDays
        fields = ('id','leaveType',)

class UserLeavesAndHolidaySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    leaveType = LeavesAndHolidaySerializer()
    class Meta:
        model = UserLeavesAndHolidays
        fields = ('id','user','leaveType','startDate','endDate','description','approved',)

class EducationSerializer(serializers.ModelSerializer):
    username =  UserSerializer()
    class Meta:
        model = Education
        fields = ('id','username', 'elementaryEducation', 'secondaryEducation', 'HigherEducation',
                  'professionalQualification', 'postGradEducation', )

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','departmentName',)
        read_only_fields = ('id',)
        extra_kwargs = {'id': {'read_only': False}}

class UserDepartmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = UserDepartment
        fields = ('id','user','department','designation')

    def create(self,validated_data):

        user_data = validated_data.pop('user')
        user = {}
        user = User.objects.get(**user_data)

        department_data = validated_data.pop('department')
        department = {}
        department = Department.objects.get(**department_data)
    
        userDepartment = UserDepartment.objects.create(user=user,department=department,**validated_data)
        return userDepartment

class AvailablePaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailablePaymentMethod
        fields = ('id','paymentMethod', 'addedDate', )

class CommisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commision
        fields = ('id','commisionName', 'commisionPercentageRate',)
        extra_kwargs = {'id': {'read_only': False}}

class SalaryTypeSerializer(serializers.ModelSerializer):
    commision = CommisionSerializer()
    class Meta:
        model = SalaryType
        fields = ('id','name','basicPay','commision')
        extra_kwargs = {'id': {'read_only': False}}

class CreateSalaryTypeSerializer(serializers.ModelSerializer):
 
    commision = CommisionSerializer()
    class Meta:
        model = SalaryType
        fields = ('id','name','basicPay','commision')  
    def create(self,validated_data):

        commision_data = validated_data.pop('commision')
        commision = {}
        commision = Commision.objects.get(**commision_data)
    
        salaryType = SalaryType.objects.create(commision=commision,**validated_data)
        return salaryType



class SalaryAdditionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalaryAdditionType
        fields = ( 'id','additionTypeName','description' )


class GovernmentRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GovernmentRate
        fields = ('id','rateName', 'rateBasicAmount', 'ratePercentage',)

class governmentDeduction(serializers.ModelSerializer):

    class Meta:
        model = GovernmentDeduction
        fields = ('id','deductionName', 'deductionAmount',)

class InternalDeductionTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InternalDeductionType
        fields = ('id','deductionName','description',)
        read_only_fields = ('id',)
        extra_kwargs = {'id': {'read_only': False}}

        

class CommisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commision
        fields = ('id','commisionName', 'commisionPercentageRate',)

class AccountSerializer(serializers.ModelSerializer):
    username =  UserSerializer()
    prefferedPaymentMethod = AvailablePaymentMethodSerializer()
    salaryType = SalaryTypeSerializer()
    class Meta:
        model = Account
        fields = ('id','username', 'prefferedPaymentMethod','salaryType','bankName','bankAccountName','phonenumber','internalDeductions','salaryAdditions')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class CreateAccountSerializer(serializers.ModelSerializer):
 
    username =  UserSerializer()
    prefferedPaymentMethod = AvailablePaymentMethodSerializer()
    salaryType = SalaryTypeSerializer()
    class Meta:
        model = Account
        fields = fields = ('id','username', 'prefferedPaymentMethod','salaryType','bankName','bankAccountName','phonenumber','internalDeductions','salaryAdditions')   
    def create(self,validated_data):

        user_data = validated_data.pop('username')
        username = {}
        username = User.objects.get(**user_data)
      
        prefferedPaymentMethod_data = validated_data.pop('prefferedPaymentMethod')
        prefferedPaymentMethod = {}
        prefferedPaymentMethod = AvailablePaymentMethod.objects.get(**prefferedPaymentMethod_data)
        salaryType_data = validated_data.pop('salaryType')
        salaryType = {}
        salaryType = SalaryType.objects.get( id = salaryType_data["id"])

        
        account = Account.objects.create(username=username,prefferedPaymentMethod=prefferedPaymentMethod,
                                        salaryType = salaryType,**validated_data)
        return account



class InternalDeductionSerializer(serializers.ModelSerializer):
 
    internalDeductionType = InternalDeductionTypeSerializer()
    account = AccountSerializer()
    class Meta:
        model = InternalDeduction
        fields = ('id','account','internalDeductionType','deductionAmount','repaymentPeriod','date','description')  



class CreateInternalDeductionSerializer(serializers.ModelSerializer):
 
    internalDeductionType = InternalDeductionTypeSerializer()
    account = AccountSerializer()
    class Meta:
        model = InternalDeduction
        fields = ('account','internalDeductionType','deductionAmount','date','description')   
    def create(self,validated_data):

        internalDeductionType_data = validated_data.pop('internalDeductionType')
        internalDeduction = {}
        internalDeductionType = InternalDeductionType.objects.get(**internalDeductionType_data)
      
        account = {}
        account_data = validated_data.pop('account')
        account = Account.objects.get(id = account_data["id"])
    
        internalDeduction = InternalDeduction.objects.create(account=account,internalDeductionType=internalDeductionType,**validated_data)
        return internalDeduction



class SalaryAdditionSerializer(serializers.ModelSerializer):
    account =  AccountSerializer()
    salaryAdditionType = SalaryAdditionTypeSerializer()
    class Meta:
        model = SalaryAddition
        fields = ('id','account', 'date','salaryAdditionType', 'additionAmount','description')

class CreateSalaryAdditionSerializer(serializers.ModelSerializer):
 
    salaryAdditionType = SalaryAdditionTypeSerializer()
    account = AccountSerializer()
    class Meta:
        model = SalaryAddition
        fields = ('account','salaryAdditionType','additionAmount','description')   
    def create(self,validated_data):

        salaryAdditionType_data = validated_data.pop('salaryAdditionType')
        salaryAddition = {}
        salaryAdditionType = SalaryAdditionType.objects.get(**salaryAdditionType_data)
      
        account = {}
        account_data = validated_data.pop('account')
        account = Account.objects.get(id = account_data["id"])
    
        salaryAddition = SalaryAddition.objects.create(account=account,salaryAdditionType=salaryAdditionType,**validated_data)
        return salaryAddition
        
class PaymentStatusSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = PaymentStatus
        fields = ('account','paymentDate','status','basicpay','commision','salesTotalWorth','allowanceTotal','deductionTotal','totalPay')
        extra_kwargs = {'id': {'read_only': False}}


class CreateDraftSerializer(serializers.ModelSerializer):
 
    account = AccountSerializer()
    class Meta:
        model = PaymentStatus
        fields = ('account',)   
    def create(self,validated_data):
      
        account = {}
        account_data = validated_data.pop('account')
        account = Account.objects.get(id = account_data["id"])
    
        draft = PaymentStatus.objects.create(account=account,**validated_data)
        return draft
        

class SaleSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = Sale 
        fields = ('account','salesWorth')
