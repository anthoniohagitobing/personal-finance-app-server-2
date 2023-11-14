from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200)
    currency = models.CharField(max_length=5)
    account_type = models.CharField(max_length=25)
    note = models.CharField(max_length=200, blank=True)

class RecordIncomeExpense(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    category = models.CharField(max_length=50)
    input_type = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=19, decimal_places=10)