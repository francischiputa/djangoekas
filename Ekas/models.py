from django.db import models

GENDER = [
    ('Male', 'Male'), ('Female', 'Female')
]

MONTHS = [
    (str(number), str(number)) for number in range(1, 61)
]

GOVERNMENT_MINISTRIES = [
    ('Ministry Of Information and Media', 'Ministry Of Information and Media'),
    ('Ministry Of Education', 'Ministry Of Education'), ('Ministry Of Home Affairs', 'Ministry Of Home Affairs'),
    ('Ministry Of Foreign Affairs', 'Ministry Of Foreign Affairs'), ('Ministry Of Health', 'Ministry Of Health'),
    ('Ministry Of Technology & Science', 'Ministry Of Technology & Science'),
    ('Ministry Of Defence', 'Ministry Of Defence'), ('Green Economy and Environment', 'Green Economy and Environment'),
    ('Ministry Of Mines and Minerals Development', 'Ministry Of Mines and Minerals Development'),
    ('Ministry Of Commerce, Trade and Industry', 'Ministry Of Commerce, Trade and Industry'),
    ('Ministry Of Transport and Logistics', 'Ministry Of Transport and Logistics'),
    ('Ministry Of Agriculture', 'Ministry Of Agriculture'), ('Ministry Of Health', 'Ministry Of'),
    ('Ministry Of Justice', 'Ministry Of Justice'),
    ('Ministry Of  Water Development and Sanitation', 'Ministry Of  Water Development and Sanitation'),
    ('Ministry Of Youth, Sport and Arts', 'Ministry Of Youth, Sport and Arts'),
    ('Ministry Of Lands and Natural Resources', 'Ministry Of Lands and Natural Resources'),
    ('Ministry Of Labour And Social Security', 'Ministry Of Labour And Social Security'),
    ('Ministry Of Tourism', 'Ministry Of Tourism'), ('Ministry Of Local Government and Rural Development', 'Ministry '
                                                                                                           'Of Local '
                                                                                                           'Government and Rural Development'),
    ('Ministry Of Finance and National Planning', 'Ministry Of Finance and National Planning'),
    ('Ministry Of Fisheries and Livestock', 'Ministry Of Fisheries and Livestock'),
    ('Ministry Of Energy', 'Ministry Of Energy'),
    ('Ministry Of Community Development and Social Services', 'Ministry of Community Development and Social Services'),
    ('Ministry Of Infrastructure, Housing Urban and Development', 'Ministry Of Infrastructure, Housing Urban and '
                                                                  'Development'),
    ('Ministry Of Small and Medium Enterprises Development', 'Ministry Of Small and Medium Enterprises Development'),
    ('Other', 'Other'),

]

LOAN_AMOUNTS = [
    (1000, 1000), (2000, 2000), (3000, 3000), (4000, 4000), (5000, 5000), (6000, 6000),
    (7000, 7000), (8000, 8000), (9000, 9000), (10000, 10000),
]


class LoanApplication(models.Model):
    """
    The loan application form.
    """
    date_time_created = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(verbose_name='Is the Application approved?', default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    alt_phone_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='Alternative Phone Number')
    email = models.EmailField(max_length=64)
    man_number = models.CharField(max_length=100, help_text='Check your payslip for your Man Number')
    employee_number = models.CharField(max_length=100, help_text='Check your payslip for Employee Number', blank=True,
                                       null=True, verbose_name='Employee Number (Optional)')
    nrc_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100, help_text='Bank Account Name as it appears at the Bank')
    work_ministry = models.CharField(max_length=100, choices=GOVERNMENT_MINISTRIES, verbose_name='Ministry')
    work_department = models.CharField(max_length=100,
                                       help_text='The department under the selected government ministry',
                                       verbose_name='Department')
    work_address = models.CharField(max_length=100)
    loan_amount = models.FloatField(choices=LOAN_AMOUNTS, help_text='The Amount in Kwacha that you wish to get')
    months_to_repay = models.CharField(max_length=100, choices=MONTHS, default='1',
                                       help_text='Number of Months you wish to repay the borrowed amount')

    payslip_upload = models.FileField(upload_to='payslips',
                                      help_text='Your latest payslip. Supported formats: pdf, JPG, PNG, DOCX, JPEG')
    bank_statement_upload = models.FileField(upload_to='Bank Statements',
                                             verbose_name='Upload Bank Statement. Supported formats: pdf, PNG, JPEG, JPG',
                                             null=True, blank=True)
    nrc_upload = models.FileField(upload_to='nrc',
                                  help_text='Scanned Copy of your NRC. Supported formats: pdf, PNG, JPEG, JPG')
    signature = models.FileField(upload_to='signatures', verbose_name='Upload Your Signature',
                                 help_text='Supported formats: pdf, PNG, JPEG, JPG')

    def __str__(self):
        return f"Loan Application submitted by {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Loan Applications'
        verbose_name = 'Loan Application'
