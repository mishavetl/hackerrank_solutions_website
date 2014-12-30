from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from index.models import Solution
from index.forms import SolutionForm

def index(request):
	solutions = Solution.objects.all().order_by("-created_at")[:5]
	return render(request, 'index/index.html', {
		'solutions': solutions,
	})

def solution(request, id):
	solution = Solution.objects.get(id=id)

	return render(request, 'index/solution.html', {
		'solution': solution
	})

@login_required
def add_solution(request):
	if request.method == 'POST':
		form = SolutionForm(request.POST)
		if form.is_valid():

			solution = form.save(commit=False)
			solution.moderator = request.user
			try:
				Solution.objects.get(title=solution.title)
			except Solution.DoesNotExist:
				solution.save()

				return HttpResponseRedirect('/')
			else:
				form = SolutionForm()
				args = {'form': form, 'error': 'Solution Already exist'}
	else:
		form = SolutionForm()
		args = {'form': form}

	return render(request, 'index/add_solution.html', args)
