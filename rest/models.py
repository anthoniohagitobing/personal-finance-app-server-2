from django.db import models

# Create your models here.
class User(models.Model):
    # class Meta:
    #     # this allows you to  give setting to the tables
    #     ordering = ('email',)
    #     verbose_name_plural = 'app_user'
    #         # this allows you to give alios to your class

    def __str__(self):
        return self.email
        # this will select name the record with email

    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Account(models.Model):
    def __str__(self):
        return self.account_name
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200)
    currency = models.CharField(max_length=5)
    account_type = models.CharField(max_length=25)
    note = models.CharField(max_length=200, blank=True)

class RecordIncomeExpense(models.Model):
    def __str__(self):
        return self.transaction_type
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    category = models.CharField(max_length=50)
    input_type = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=19, decimal_places=10)