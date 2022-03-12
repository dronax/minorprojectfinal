from django.db import models

# Create your models here.
class basephyQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class  basemathQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class basechemQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class baseengQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class phyQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class mathQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class chemQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question

class engQuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    qid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    def __str__(self):
        return self.question
class Performance(models.Model):
    USERID = models.CharField(max_length = 50,null = False)
    Physics = models.FloatField(null = True)
    Chemistry = models.FloatField(null = True)
    Maths = models.FloatField(null = True)
    English = models.FloatField(null = True)
    Total = models.FloatField(null = True)
    def __str__(self):
        return self.USERID