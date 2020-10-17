from django.db import models

# Create your models here.
class BSEdata(models.Model):
    copy_date = models.DateField()
    security_code = models.CharField(max_length=255)
    security_name = models.CharField(max_length=255)
    security_group = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    high = models.CharField(max_length=255)
    low = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    prevclose = models.CharField(max_length=255)
    no_trades = models.CharField(max_length=255)
    no_of_shares = models.CharField(max_length=255)
    net_turnover = models.CharField(max_length=255)
    isin_code = models.CharField(max_length=288)
