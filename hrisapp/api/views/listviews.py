from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *

from datetime import date 

import json

#list views.
class UserList(generics.ListCreateAPIView):
    '''
        get:
        return list of users 
        post:
        create a new user

    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AttendanceList(APIView):
    '''
        get:
        get list of users attended for either this day, this week or this month depaending on the url filter parameter 
    '''
    def get(self,request,filter):
        today = date.today()
        day = today.day
        month = today.month
        year = today.year

        if filter == "today":
            attendanceList = UserAttendance.objects.filter(date__year=year, date__month=month, date__day=day)  
            data = UserAttendanceSerializer(attendanceList,many=True).data

        elif filter == "week":
            today = today.weekday()
            howFarIsMonday = today+1
            week_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
            for i in range(howFarIsMonday):
                attendanceList = UserAttendance.objects.filter(date__year=year, date__month=month, date__day=day - i)  
                data = UserAttendanceSerializer(attendanceList,many=True).data  
                week_dict[i] = data 
            data = week_dict  

        elif filter == "month":
            howFarIsDate1 = day+1
            month_dict = {new_list: [] for new_list in range(1,howFarIsDate1)}
            for i in range(howFarIsDate1):
                attendanceList = UserAttendance.objects.filter(date__year=year, date__month=month, date__day=day - i)  
                data = UserAttendanceSerializer(attendanceList,many=True).data  
                month_dict[i] = data 
            data = month_dict
        return Response(data)

class attendanceListForSpecificDate(APIView):
        '''
            get:
            gets a list of users attended for the date specified in the url in the format yyyy-mm-dd
        '''
        def get(self,request,date):
            attendanceList = UserAttendance.objects.filter(date=date)  
            data = UserAttendanceSerializer(attendanceList,many=True).data
            return Response(data)

class departmentList(generics.ListCreateAPIView):
    '''
        get:
        return list of department
        post:
        create a new department

    '''
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LeaveTypeList(generics.ListCreateAPIView):
    '''
        get:
        return list of leave types
        post:
        create a new leave type

    '''
    queryset = LeavesAndHoliDays.objects.all()
    serializer_class = LeavesAndHolidaySerializer

class UserLeaveList(generics.ListCreateAPIView):
    '''
        get:
        return list of users with the leaves the applied to or serve

    '''
    queryset = UserLeavesAndHolidays.objects.all()
    serializer_class = UserLeavesAndHolidaySerializer

class AvailablePaymentMethodList(generics.ListCreateAPIView):
    '''
        get:
        return list of available payment method
        post:
        create a new payment method

    '''
    queryset = AvailablePaymentMethod.objects.all()
    serializer_class = AvailablePaymentMethodSerializer

class SalaryTypeList(generics.ListCreateAPIView):
    '''
        get:
        return list of types of salaries 
        post:
        create a new salary type

    '''
    queryset = SalaryType.objects.all()
    serializer_class = SalaryTypeSerializer

class AccountList(generics.ListCreateAPIView):
    '''
        get:
        return list of accounts

    '''
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class SalaryAdditionTypeList(generics.ListCreateAPIView):
    '''
        get:
        return list of allowance types
        post:
        create a new allowance type

    '''
    queryset = SalaryAdditionType.objects.all()
    serializer_class = SalaryAdditionTypeSerializer

class SalaryAdditionList(generics.ListCreateAPIView):
    '''
        get:
        return list of users with the allowances that has been applied to them 

    '''
    queryset = SalaryAddition.objects.all()
    serializer_class = SalaryAdditionSerializer

class GovernmentRateList(generics.ListCreateAPIView):
    '''
        get:
        return list of rates 
        post:
        create a new rate

    '''
    queryset = GovernmentRate.objects.all()
    serializer_class = GovernmentRateSerializer

class InternalDeductionTypeList(generics.ListCreateAPIView):
    '''
        get:
        return list of internal deduction types
        post:
        create a new internal deduction type

    '''
    queryset = InternalDeductionType.objects.all()
    serializer_class = InternalDeductionTypeSerializer

class InternalDeductionList(generics.ListCreateAPIView):
    '''
        get:
        return list of users with internal deductions applied to them

    '''
    queryset = InternalDeduction.objects.all()
    serializer_class = InternalDeductionSerializer


class CommisionList(generics.ListCreateAPIView):
    '''
        get:
        return list of commisions
        post:
        create a new commision

    '''
    queryset = Commision.objects.all()
    serializer_class = CommisionSerializer

class PaymentStatusList(generics.ListCreateAPIView):
    '''
        get:
        return list of accounts that have been drafted

    '''
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer

class SalesList(generics.ListCreateAPIView):
    '''
        get:
        return list of sales
        post:
        create a new sale

    '''
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

