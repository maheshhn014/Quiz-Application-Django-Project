from django.db import models

# Create your models here.


'''Created class QuizName for type of quiz'''

class QuizName(models.Model):
    quiz_name = models.CharField(max_length=200, blank=False)

    
    def __str__(self):
        return self.quiz_name
    
    class Meta:
        db_table = "QuizName"
        

'''Created class QuestionModel for quiz questions and answers and hint'''

class QuestionModel(models.Model):
    question = models.CharField(max_length=200, blank=False)
    option1 = models.CharField(max_length=200, blank=False)
    option2 = models.CharField(max_length=200, blank=False)
    option3 = models.CharField(max_length=200, blank=False)
    option4 = models.CharField(max_length=200, blank=False)
    answer = models.CharField(max_length=200, blank=False)
    category = models.ForeignKey(QuizName, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "QuestionModel"
        
    def __str__(self):
        return str(self.category) + " " + self.question
   
   
'''Created class Leaderboard to display all quiz results'''

class Leaderboard(models.Model):
    name = models.CharField(max_length=200, blank=False)
    quiz_name = models.CharField(max_length=200, blank=False)
    total = models.CharField(max_length=200, blank=False)
    correct = models.CharField(max_length=200, blank=False)
    incorrect = models.CharField(max_length=200, blank=False)
    percentage = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Quiz_Leaderboard"
      