from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *

from datetime import datetime
#update views for models related to a specific user
class CheckOutUserPK(APIView):
    '''
        patch:
        mark user with id <user_id> as checked out for the current day  

    '''

    def patch(self, request):
        user_id = request.data.get("user_id")
        userAttendance = UserAttendance.objects.get(user_id = user_id ,date=datetime.now())
        
        serializer = UserAttendanceSerializer(userAttendance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
class UpdateAccountForUserPK(APIView):
    '''
        patch:
        update account information for account holder with username id <username_id> 

    '''

    def patch(self, request, pk):
        account = Account.objects.get(username_id = pk)

        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateDeductionsForUserPK(APIView):
    '''
    patch:
    update deduction information for account holder with username id <username_id> 

    '''

    def patch(self, request, pk):
        deductions = InternalDeduction.objects.get(username_id = pk)

        serializer = InternalDeductionSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdatePaymentStatusForUserPK(APIView):
    '''
    patch:
    update summary information for account holder with username id <username_id> 

    '''

    def patch(self, request, pk):
        account = PaymentStatus.objects.get(username_id = pk)

        serializer = PaymentStatusSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

#update views for the other models
class UpdateGovernmentRateNamedSLUG(APIView):
    '''
        patch:
        update account information for account holder with username id <username_id> 

    '''

    def patch(self, request, slug):
        account = GovernmentRate.objects.get(rateName = pk)

        serializer = GovernmentRateSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateGovernmentDeductionNamedSLUG(APIView):

    def patch(self, request, slug):
        account = GovernmentDeduction.objects.get(deductionName = slug)

        serializer = GovernmentDeductionSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateInternalDeductionTypeNamedSLUG(APIView):

    def patch(self, request, slug):
        account = InternalDeductionType.objects.get( deductionName = slug)

        serializer = InternalDeductionTypeSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateCommisionNamedSLUG(APIView):

    def patch(self, request, slug):
        account = Commision.objects.get(rateName = slug)

        serializer = CommisionSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
