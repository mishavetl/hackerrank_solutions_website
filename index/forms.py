from django import forms

from index.models import Solution

class SolutionForm(forms.ModelForm):
	class Meta:
	    model = Solution
	    exclude = ('points', 'moderator', 'voters')
