from rest_framework import serializers
from .models import Accounts, Transactions, Users

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['accountid', 'accountnumber', 'accounttype', 'balance', 'status', 'createdate']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userid', 'name', 'email', 'phone', 'status', 'createdate']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['transactionid', 'fromaccountid', 'toaccountid', 'amount', 'transactiontype', 'statusid', 'createdate']