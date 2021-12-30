from django.db import models

class employee_detail(models.Model):
    name     =models.CharField(max_length=100)
    DOB      =models.DateField()
    basic_pay=models.IntegerField()
    position  =models.CharField(max_length=100)
    address  =models.TextField()
    DOJ      =models.DateField()
    class meta:
        db_table="employee_detail"
        
class salary_detail(models.Model):
    Emp_code =models.IntegerField()
    Name     =models.CharField(max_length=100)
    year     =models.CharField(max_length=100)
    month    =models.CharField(max_length=100)
    Number_of_working_days =models.IntegerField()
    Employee_working_days  =models.IntegerField()
    salary   =models.IntegerField()
    
    class meta:
        db_table="salary_detail"