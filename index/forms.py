from django.forms import ModelForm

from index.models import Solution

class SolutionForm(ModelForm):
	class Meta:
	    model = Solution
	    exclude = ('points', 'moderator', 'voters')
