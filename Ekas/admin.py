from django.contrib import admin
from .models import *


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'nrc_number', 'loan_amount', 'amount_to_repay',
        'monthly_payment'

    ]
    list_display_links = ['first_name', 'last_name', 'loan_amount', 'nrc_number']
    list_filter = [
        'date_time_created'
    ]
    search_fields = [
        'first_name', 'last_name', 'nrc_number'
    ]
    search_help_text = "Search Loan Applications by applicant's name or NRC number."

    def amount_to_repay(self, loan_application: LoanApplication):
        return round(float(loan_application.loan_amount) + 0.06 * float(loan_application.loan_amount) * int(loan_application.months_to_repay), 2)

    def monthly_payment(self, loan_application: LoanApplication):
        return round(float(self.amount_to_repay(loan_application) / int(loan_application.months_to_repay)), 2)