from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import User, Account, RecordIncomeExpense
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
from django.db.models import Sum

# Create your views here.
def home(request):
    return HttpResponse('Test backend server')

def get_user(request, email):
    if request.method == 'GET':
        # print(email)
        data = User.objects.filter(email=email).values()

        # Change name to JavaScript syntax
        new_data = {}
        new_data['id'] = data[0]['id']
        new_data['email'] = data[0]['email']
        new_data['firstName'] = data[0]['first_name']
        new_data['lastName'] = data[0]['last_name']

        json_data = json.dumps(new_data)
        # print(json_data)
        return HttpResponse(json_data, status=200)
    else:
        return HttpResponse('Invalid URL', status=404)

@csrf_exempt
    # with post method, you need cookies
    # this is a temporary solution as authentication has not been built yet
def create_user(request):
    if request.method == 'POST':
        # Processing incoming data
        data = json.loads(request.body)
            # json.loads already convert JSON string into python object 
        User.objects.create(
            email = data['email'],
            first_name = data['firstName'],
            last_name = data['lastName'],
        )
        return HttpResponse('User created in backend database', status=201)
    else:
        return HttpResponse('Invalid URL', status=404)

@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        Account.objects.create(
            user_id = data['userId'],
            account_name = data['accountName'],
            currency = data['currency'],
            account_type = data['accountType'],
            note = data['note'],
        )
        return HttpResponse('Account created', status=201)
    else:
        return HttpResponse('Invalid URL', status=404)

def get_account(request, account_id):
    if request.method == 'GET':
        # print(account_id)
        account = Account.objects.filter(id = account_id).values_list('id', 'account_name', 'currency', 'account_type')
        # print(account)
        reloaded_account = Account.objects.all()
        reloaded_account.query = pickle.loads(pickle.dumps(account.query))
        # print(reloaded_account)

        # Change name to JavaScript syntax
        new_account = {}
        new_account['id'] = reloaded_account[0]['id']
        new_account['accountName'] = reloaded_account[0]['account_name']
        new_account['currency'] = reloaded_account[0]['currency']
        new_account['accountType'] = reloaded_account[0]['account_type']
        # print(new_account)

        json_account = json.dumps(new_account)
        # print(json_account)
        return HttpResponse(json_account, status=200)
    else:
        return HttpResponse('Invalid URL', status=404)
    
def get_all_accounts(request, user_id):
    if request.method == 'GET':
        # print(user_id)
        accounts = Account.objects.filter(user_id = user_id).values_list('id', 'account_name', 'currency', 'account_type')
        reloaded_accounts = Account.objects.all()
        reloaded_accounts.query = pickle.loads(pickle.dumps(accounts.query))
            # values_list create a tuple, so it should be reconverted to list by doing the above
            # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.query.QuerySet.create

        # Getting net balance
        

        # Renaming into JavaScript Syntax
        new_accounts = []
        for account in reloaded_accounts:
            balance = RecordIncomeExpense.objects.filter(account_id = account['id']).values('account_id').annotate(total=Sum('amount'))
            print(balance[0]['total'])
            new_account = {}
            new_account['id'] = account['id']
            new_account['accountName'] = account['account_name']
            new_account['currency'] = account['currency']
            new_account['accountType'] = account['account_type']
            new_account['balance'] = float(balance[0]['total'])
            new_accounts.append(new_account)
        json_data = json.dumps(new_accounts)

        # print(accounts)
        # print(reloaded_accounts)
        print(json_data)
        return HttpResponse(json_data, status=200)
    else:
        return HttpResponse('Invalid URL', status=404)

@csrf_exempt
def create_record_income_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        RecordIncomeExpense.objects.create(
            account_id = data['accountId'],
            transaction_type = data['transactionType'],
            title = data['title'],
            date_time = data['dateTime'],
            category = data['category'],
            input_type = data['inputType'],
            amount = data['amount'],
        )
        return HttpResponse('Record created', status=201)
    else:
        return HttpResponse('Invalid URL', status=404)
    
def get_all_records(request, account_id):
    if request.method == 'GET':
        # print(account_id)
        records = RecordIncomeExpense.objects.filter(account_id = account_id).order_by('-date_time').values_list('id', 'transaction_type', 'title', 'date_time', 'category', 'input_type', 'amount')
        # print(records)
        reloaded_records = RecordIncomeExpense.objects.all()
        reloaded_records.query = pickle.loads(pickle.dumps(records.query))

        # Renaming into JavaScript Syntax
        new_records = []
        for record in reloaded_records:
            new_record = {}
            new_record['id'] = record['id']
            new_record['transactionType'] = record['transaction_type']
            new_record['title'] = record['title']
            new_record['dateTime'] = record['date_time'].isoformat()
            new_record['category'] = record['category']
            new_record['inputType'] = record['input_type']
            # new_record['amount'] = json.dumps(record['amount'], default=str)
            new_record['amount'] = float(record['amount'])
            new_records.append(new_record)
        # print(new_records)
        json_data = json.dumps(new_records)

        return HttpResponse(json_data, status=200)
    else:
        return HttpResponse('Invalid URL', status=404)