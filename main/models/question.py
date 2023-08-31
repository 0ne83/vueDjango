from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Question_DB(models.Model):
    # added question number for help in question paper
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    optionA = models.CharField(default='Yes', max_length=3)
    optionB = models.CharField(default='No', max_length=2)
    # optionC = models.CharField(max_length=100)
    # optionD = models.CharField(max_length=100)
    answer = models.CharField(default='Yes', max_length=3)


    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \n'

# f'C.{self.optionC} \nD.{self.optionD}
class QForm(ModelForm):
    class Meta:
        model = Question_DB
        fields = '__all__'
        exclude = ['qno', 'professor']
