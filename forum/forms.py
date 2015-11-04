from django import forms
from .models import *

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('content',)


class IdeaForm(forms.ModelForm):

	class Meta:
		model = IdeaPost
		fields = ('title', 'company', 'description')