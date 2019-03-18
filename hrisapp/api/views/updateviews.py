from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
#TODO import each componet singly
from hrisapp.models import *
from hrisapp.api.serializers import *
#update views for models related to a specific user
class UpdateAccountForUserPK(APIView):

    def patch(self, request, pk):
        account = Account.objects.get(username_id = pk)

        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateDeductionsForUserPK(APIView):

    def patch(self, request, pk):
        deductions = InternalDeduction.objects.get(username_id = pk)

        serializer = InternalDeductionSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
class UpdatePaymentStatusForUserPK(APIView):

    def patch(self, request, pk):
        account = PaymentStatus.objects.get(username_id = pk)

        serializer = PaymentStatusSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

#update views for the other models
class UpdateGovernmentRateNamedSLUG(APIView):

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
