from django.contrib import admin
from quiz_app.models import QuestionModel, Leaderboard, QuizName


# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(Leaderboard)
admin.site.register(QuizName)