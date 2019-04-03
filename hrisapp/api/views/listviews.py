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
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AttendanceList(APIView):
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
        def get(self,request,date):
            attendanceList = UserAttendance.objects.filter(date=date)  
            data = UserAttendanceSerializer(attendanceList,many=True).data
            return Response(data)

class departmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LeaveTypeList(generics.ListCreateAPIView):
    queryset = LeavesAndHoliDays.objects.all()
    serializer_class = LeavesAndHolidaySerializer

class UserLeaveList(generics.ListCreateAPIView):
    queryset = UserLeavesAndHolidays.objects.all()
    serializer_class = UserLeavesAndHolidaySerializer

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

