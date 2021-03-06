from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'row': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length for the text is 4000'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
