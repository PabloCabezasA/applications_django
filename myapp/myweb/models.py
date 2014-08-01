from django.db import models

# Create your models here.
class AccountAccount(models.Model):    
    Account_type = (
        ('view', 'Small'),
        ('other', 'Medium'),
        ('receivable', 'Medium'),
        ('payable', 'Medium'),
        ('liquidity', 'Medium'),
        ('consolifation', 'Medium'),
        ('closed', 'Medium')
    )
    Currency_Mode =(
            ('current', 'En Fecha'),
            ('average', 'Tasa Promedio')
        )
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', db_column='write_uid', blank=True, null=True)
    code = models.CharField(max_length=64)
    reconcile = models.NullBooleanField()
    currency = models.ForeignKey('ResCurrency', blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', db_column='user_type')
    active = models.NullBooleanField()
    name = models.CharField(max_length=256)
    level = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany')
    shortcut = models.CharField(max_length=12, blank=True)
    note = models.TextField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)    
    currency_mode = models.CharField(max_length=50,choices=Currency_Mode)
    type_related = models.CharField(max_length=50, choices=Account_type,db_column='type')
    
    class Meta:
        managed = False
        db_table = 'account_account'

class ResUsers(models.Model):    
    active = models.NullBooleanField()
    login = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64, blank=True)
    company = models.ForeignKey('ResCompany')
    partner = models.ForeignKey('ResPartner')
    create_uid = models.ForeignKey('self', db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('self', db_column='write_uid', blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)
    login_date = models.DateField(blank=True, null=True)
    signature = models.TextField(blank=True)
    action_id = models.IntegerField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias')
    share = models.NullBooleanField()
    pos_config = models.IntegerField(blank=True, null=True)
    ean13 = models.CharField(max_length=13, blank=True)
    
    class Meta:
        managed = False
        db_table = 'res_users'

class AccountAccountType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_uid = models.ForeignKey('ResUsers', db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', db_column='write_uid', blank=True, null=True)
    #close_method = models.CharField(max_length=-1)
    note = models.TextField(blank=True)
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    #report_type = models.CharField(max_length=-1)
    class Meta:
        managed = False
        db_table = 'account_account_type'

class ResCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    parent = models.ForeignKey('self', blank=True, null=True)
    partner = models.ForeignKey('ResPartner')
    currency = models.ForeignKey('ResCurrency')
    create_uid = models.ForeignKey('ResUsers', db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', db_column='write_uid', blank=True, null=True)
    rml_footer = models.TextField(blank=True)
    rml_header = models.TextField()
    #paper_format = models.CharField(max_length=-1)
    logo_web = models.BinaryField(blank=True, null=True)
    rml_header2 = models.TextField()
    rml_header3 = models.TextField()
    rml_header1 = models.CharField(max_length=200, blank=True)
    account_no = models.CharField(max_length=64, blank=True)
    company_registry = models.CharField(max_length=64, blank=True)
    custom_footer = models.NullBooleanField()
    expects_chart_of_accounts = models.NullBooleanField()
    paypal_account = models.CharField(max_length=128, blank=True)
    overdue_msg = models.TextField(blank=True)
    #tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True)
    expense_currency_exchange_account = models.ForeignKey('AccountAccount', blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey('AccountAccount', blank=True, null=True)
    vat_check_vies = models.NullBooleanField()
    project_time_mode_id = models.IntegerField(blank=True, null=True)
    schedule_range = models.FloatField()
    security_lead = models.FloatField()
    po_lead = models.FloatField()
    manufacturing_lead = models.ForeignKey('ProductUom', db_column='manufacturing_lead')
    is_group_invoice_line = models.NullBooleanField()
    autosplit_is_active = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'res_company'        

class ResCurrency(models.Model):
    name = models.CharField(max_length=32)
    create_uid = models.ForeignKey('ResUsers', db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', db_column='write_uid', blank=True, null=True)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    symbol = models.CharField(max_length=4, blank=True)
    company = models.ForeignKey('ResCompany', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    base = models.NullBooleanField()
    active = models.NullBooleanField()
    #position = models.CharField(max_length=-1, blank=True)
    accuracy = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'res_currency'        