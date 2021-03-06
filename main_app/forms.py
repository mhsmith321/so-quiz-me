from django.forms import ModelForm, forms
from .models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'correct_answer']
