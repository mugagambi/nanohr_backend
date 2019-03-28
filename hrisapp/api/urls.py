from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import listviews,userdetailviews,detailviews,updateviews,addViews
#TODO add delete views 
urlpatterns = [
   #listing without details
    path('userlist/', listviews.UserList.as_view()),
    path('attendance-list/<slug:filter>/', listviews.AttendanceList.as_view()),
    path('attendance-list-full/<slug:month>/<slug:day>/<slug:year>/', listviews.attendanceListForSpecificDate.as_view()),
    path('department-list/',listviews.departmentList.as_view()),
    path('leave-types/', listviews.LeaveTypeList.as_view()),
    path('user-leaves-list/', listviews.UserLeaveList.as_view()),
    path('available-payment-methods-list/', listviews.AvailablePaymentMethodList.as_view()),
    path('salary-type-list/', listviews.SalaryTypeList.as_view()),
    path('accounts-list/', listviews.AccountList.as_view()),
    path('payment-status-list/', listviews.PaymentStatusList.as_view()),
    path('salary-addition-types-list/', listviews.SalaryAdditionTypeList.as_view()),
    path('salary-addition-list/', listviews.SalaryAdditionList.as_view()),
    path('government-rate-list/', listviews.GovernmentRateList.as_view()),
    path('internal-deduction-type-list/', listviews.InternalDeductionTypeList.as_view()),
    path('internal-deduction-list/', listviews.InternalDeductionList.as_view()),
    path('commision-list/', listviews.CommisionList.as_view()),
    path('sales-list/', listviews.SalesList.as_view()),

   #urls to post data .

    path('check-in/',addViews.CheckIn.as_view()),
    path('addUserToDepartment/',addViews.AddUserToDepartment.as_view()),
    path('addAccount/',addViews.addAccount.as_view()),
    path('addInternalDeduction/', addViews.addInternalDeduction.as_view()),
    path('addAllowance/',addViews.addAllowance.as_view()),
    path('addSalaryType/',addViews.addsalaryType.as_view()),
    path('draft/',addViews.CreateDraft.as_view()),


   #detail views for specific users
    path('user-account-detail/<int:pk>/', userdetailviews.AccountList.as_view()),
    path('user-education-detail/<int:pk>/', userdetailviews.EducationList.as_view()),
    path('user-salary-type-detail/<int:pk>/', userdetailviews.SalaryTypeList.as_view()),
    path('user-payment-status-detail/<int:pk>/', userdetailviews.PaymentStatusList.as_view()),
    path('user-salary-addition-detail/<int:pk>/', userdetailviews.SalaryAdditionList.as_view()),
    path('user-salary-deduction-detail/<int:pk>/', userdetailviews.InternalDeductionList.as_view()),
    path('user-general-detail/<int:pk>/', userdetailviews.GeneralDetail.as_view()),

   #detail view for the other models with primary keys
    path('department/<int:pk>/', detailviews.DepartmentWithIdPK.as_view()),
    path('internal-deduction-type/<int:pk>/', detailviews.InternalDeductionTypeWithIdPK.as_view()),
    path('employees-in-department/<int:pk>/', detailviews.EmployeesInDepartmentPK.as_view()),
    path('salary-type-accounts/<int:pk>/', detailviews.AccountsWithSalaryTypePK.as_view()),
    path('preffered-payment-method-accounts/<int:pk>/', detailviews.AccountsWithPrefferedPaymentmethodPK.as_view()),
    path('salary-addition-accounts/<int:pk>/', detailviews.AccountsWithSalaryAdditionPK.as_view()),
    path('commision-type-accounts/<int:pk>/', detailviews.AccountsWithCommisiontypePK.as_view()),
    path('internal-deduction-accounts/<int:pk>/', detailviews.AccountsWithInternalDeductionPK.as_view()),

   #update urls for user instances
    path('check-out/',updateviews.CheckOutUserPK.as_view()), 
    path('update-account-info/<int:pk>/',updateviews.UpdateAccountForUserPK.as_view()), 
    path('update-deduction-info/<int:pk>/',updateviews.UpdateDeductionsForUserPK.as_view()),
    path('update-payment-status-info/<int:pk>/',updateviews.UpdatePaymentStatusForUserPK.as_view()),
   #update urls for other instances
    path('update-government-rate-info/<slug:slug>/',updateviews.UpdateGovernmentRateNamedSLUG.as_view()),
    path('update-government-deduction-info/<slug:slug>/',updateviews.UpdateGovernmentDeductionNamedSLUG.as_view()),
    path('update-internal-deduction-info/<slug:slug>/',updateviews.UpdateInternalDeductionTypeNamedSLUG.as_view()),
     path('update-commision-info/<slug:slug>/',updateviews.UpdateCommisionNamedSLUG.as_view()),  
]

urlpatterns = format_suffix_patterns(urlpatterns)