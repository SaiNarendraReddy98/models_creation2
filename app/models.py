from django.db import models

# Create your models here.
class Department(models.Model):
    D_name=models.CharField(max_length=100,unique=True)
    E_deptno=models.IntegerField(primary_key=True)
    D_Loc=models.CharField(max_length=100)
    def __str__(self):
        return self.D_name
    
class Employee(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    E_name=models.CharField(max_length=100,unique=True)
    E_job=models.CharField(max_length=100)
    E_Hiredate=models.DateField()
    E_sal=models.IntegerField()
    E_deptno=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.E_name
    
class SalGrade(models.Model):
    Grade=models.IntegerField(primary_key=True)
    Lowsal=models.IntegerField()
    Hisal=models.IntegerField()
    def __str__(self):
        return self.Grade
    
class Bonus(models.Model):
    Emp_no=models.ForeignKey(Employee,on_delete=models.CASCADE)
    E_sal=models.IntegerField()
    E_comm=models.IntegerField()
    def __str__(self):
        return self.Emp_no
    



