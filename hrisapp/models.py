from django.db import models
from django.contrib.auth.models import User
from json import JSONEncoder
from uuid import UUID

JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault

class Department(models.Model):
    '''
        the available departments on the company
    '''
    id = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=20)

class UserDepartment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,related_name="educations",on_delete=models.CASCADE)
    elementaryEducation = models.CharField(max_length=50)
    secondaryEducation = models.CharField(max_length=50)
    HigherEducation = models.CharField(max_length=50)
    professionalQualification = models.CharField(max_length=50)
    postGradEducation = models.CharField(max_length=50)
    def __str__(self):
        return self.username

   # TODO grades/certificates
   # TODO add file uploads

class UserAttendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    timeIn = models.TimeField(blank=True,null=True)
    timeOut = models.TimeField(blank=True,null=True)
    
    @property
    def weekday(self):
        today = self.date.weekday()

        return today

class LeavesAndHoliDays(models.Model):
    leaveType = models.CharField(max_length=50)

class UserLeavesAndHolidays(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    leaveType = models.ForeignKey(LeavesAndHoliDays,on_delete=models.CASCADE)
    startDate = models.DateField(blank=True) 
    endDate = models.DateField(blank=True)
    description = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

class Vacancy(models.Model):
    vacantPost = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Applicants(models.Model):
    vacancyAppliedTo = models.ForeignKey(Vacancy,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    cv = models.FileField()

class AvailablePaymentMethod(models.Model):
    '''
        stores the available payment methods mpesa ..paypal etc
    '''
    id = models.AutoField(primary_key=True)
    paymentMethod = models.CharField(max_length=20)
    addedDate = models.DateTimeField(auto_now_add=True)

class SalaryAdditionType(models.Model):
    '''
        different types of allowances available to the company.
    '''
    id = models.AutoField(primary_key=True)
    additionTypeName = models.CharField(max_length=20)
    description = models.CharField(max_length=20,default="")
    taxable = models.BooleanField(default=False)

class GovernmentRate(models.Model):
    ''' 
        stores such data as nssf tax nhif etc
    '''
    rateName = models.CharField(max_length=10)
    rateBasicAmount = models.FloatField(default=0.00)
    ratePercentage = models.FloatField(default=0.00)
#TODO review more about this
class GovernmentDeduction(models.Model):
    id = models.AutoField(primary_key=True)
    deductionName = models.CharField(max_length=20)
    deductionAmount = models.FloatField(default=0.00)
    

class Commision(models.Model):
    '''
        names of the available commisions the company has..on sale of items etc 
    '''
    id = models.AutoField(primary_key=True)
    commisionName = models.CharField(max_length=20)
    description = models.CharField(max_length=20,default="no description") 
    commisionPercentageRate = models.FloatField(default=0.00)
    taxable = models.BooleanField(default=False)
#TODO many to many
class SalaryType(models.Model):
    '''
        the types of salaries and the commisions on them
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="",max_length=20)
    basicPay = models.FloatField(default = 00.00)
    commision = models.ForeignKey(Commision,related_name="salarytypes",on_delete=models.CASCADE)


#TODO add bank model mapping bank to accont number *not sure ho this works
class InternalDeductionType(models.Model):
    '''
        what is deducted from the users pay at the end of the month
    '''
    id = models.AutoField(primary_key=True)
    deductionName = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    taxable = models.BooleanField(default=False)

#TODO change username to user 
class Account(models.Model):
    '''
        links the user to the entire HR
    '''
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,related_name="accounts",on_delete=models.CASCADE)
    prefferedPaymentMethod = models.ForeignKey(AvailablePaymentMethod,related_name="accounts",on_delete=models.CASCADE)
    salaryType = models.ForeignKey(SalaryType,related_name="accounts",on_delete=models.CASCADE)
    department = models.ForeignKey(Department,related_name="accounts",on_delete=models.CASCADE)
    bankName = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    internalDeductions = models.ManyToManyField(InternalDeductionType,through='InternalDeduction')
    salaryAdditions = models.ManyToManyField(SalaryAdditionType,through='SalaryAddition')

#TODO add receipt ids
class Sale(models.Model):
    '''
        A sale the employee makes in that month
    '''
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    salesWorth = models.FloatField(default=0.00)

class InternalDeduction(models.Model):
    '''
        what deductions have been made to the specific account... how much and whether or not it 
        was settled 
    '''
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20,default="no description")
    account = models.ForeignKey(Account,related_name='internaldeductions',on_delete=models.CASCADE)
    internalDeductionType = models.ForeignKey(InternalDeductionType,related_name="internaldeductions",on_delete=models.CASCADE)
    deductionAmount= models.FloatField(default=0.00)
    settled = models.BooleanField(default=False)

    #TODO remove these
    @property
    def deductionThisMonth(self):
        deductionThisMonth = self.deductionAmount / self.numberOfInstallments
        return deductionThisMonth

    @property 
    def draftCounter(self):
        draftCounter = 0
        return draftCounter

   
   #TODO add phone number validation module *this is very ineffective
   #TODO check if we need a zip code
class SalaryAddition(models.Model):
    '''
        allowances for this account ..how much and whether or not it was settled
    '''
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)
    account = models.ForeignKey(Account,related_name='SalaryAdditions',on_delete=models.CASCADE)
    salaryAdditionType = models.ForeignKey(SalaryAdditionType,related_name="salaryadditions",on_delete=models.CASCADE)
    additionAmount = models.FloatField(default=0.00)
    settled = models.BooleanField(default=False)


#TODO change to payment summary     
class PaymentStatus(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,related_name='paymentStatuses',on_delete=models.CASCADE)
    paymentDate = models.DateField(auto_now_add=True)
    status = models.BooleanField(default='False')

    @property
    def basicpay(self):
        '''
            basic pay
        '''
        account = self.account
        basicpay = account.salaryType.basicPay
        return basicpay

    @property
    def commision(self):
        '''
            commision
        '''
        account = self.account
        commision = account.salaryType.commision.commisionPercentageRate 
        return commision

    @property
    def salesTotalWorth(self):
        '''
            sales
        '''
        account_id = self.account_id
        queryset = Sale.objects.filter(account_id=account_id)
        salesTotalWorth = 0
        for sale in queryset:
            salesTotalWorth += sale.salesWorth
        return salesTotalWorth

    @property
    def deductionTotal(self):
        account_id = self.account.id
        queryset = InternalDeduction.objects.filter(account_id = account_id)
        deductionTotal = 0
        for internalDeduction in queryset:
            if internalDeduction.settled == False:
                deductionTotal += internalDeduction.deductionThisMonth
        return deductionTotal

    @property
    def allowanceTotal(self):
        account_id = self.account.id
        queryset = SalaryAddition.objects.filter(account_id = account_id)
        allowanceTotal = 0
        for allowance in queryset:
            if allowance.settled == False:
                allowanceTotal += allowance.additionAmount
        return allowanceTotal

    @property
    def totalPay(self):
        
        totalPay = ( self.basicpay + ((self.commision/100)*self.salesTotalWorth)+ self.allowanceTotal) - self.deductionTotal
        return totalPay