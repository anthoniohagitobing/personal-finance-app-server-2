from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("user/<str:email>/", views.get_user, name="get_user"),
    path("user/", views.create_user, name="create_user"),
    # path("user-sign-in/", views.sign_in_user, name="sign_in_user"),
    path("account/", views.create_account, name="create_account"),
    path("accounts/<int:user_id>/", views.get_all_accounts, name="get_all_accounts"),
    path("account/<int:account_id>/", views.get_account, name="get_account"),
    path('record-income-expense/', views.create_record_income_expense, name="create_record_income_expense"),
    path('all-records/<int:account_id>/', views.get_all_records, name="get_all_records"),
]  