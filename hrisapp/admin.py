from django.contrib import admin
#TODO import one by one
from .models import *
# Register your models here.
#admin.site.register(Education)
admin.site.register(AvailablePaymentMethod)
admin.site.register(SalaryType)
admin.site.register(Account)
admin.site.register(SalaryAdditionType)
admin.site.register(SalaryAddition)
admin.site.register(GovernmentRate)
admin.site.register(InternalDeduction)
admin.site.register(Commision)
admin.site.register(PaymentStatus)
admin.site.register(GovernmentDeduction)
admin.site.register(InternalDeductionType)
admin.site.register(Department)
admin.site.register(UserDepartment)
admin.site.register(Sale)
admin.site.register(UserAttendance)
admin.site.register(LeavesAndHoliDays)
admin.site.register(UserLeavesAndHolidays)
admin.site.register(Vacancy)
admin.site.register(Applicants)




