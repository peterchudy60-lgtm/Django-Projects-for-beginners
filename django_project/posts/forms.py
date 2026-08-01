from django import forms
from posts.models import Post

class StatusForm(forms.Form):

    def __init__(self, *args, current_question=None):
        super().__init__(*args)
#        if current_question and current_question in self.QUESTIONS:
#            question_data = self.QUESTIONS[current_question]
#        self.fields[f'q{current_question}'] = forms.ChoiceField(
        self.fields[f'{current_question}'] = forms.ChoiceField(
            label=Post.objects.values_list('title', flat=True).get(pk=current_question),
            choices=Post.objects.values_list('choices_title', flat=True).get(pk=current_question),
            widget=forms.RadioSelect,
            )