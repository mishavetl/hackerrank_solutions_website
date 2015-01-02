from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from index.models import Solution
from index.forms import SolutionForm


def index(request):
	query = ''

	if request.method == 'POST':

		if ('query' in request.POST):
			query = request.POST['query']

			solutions = Solution.objects.filter(Q(title__icontains=query)).order_by('created_at')
	else:
		solutions = Solution.objects.all().order_by("-created_at")[:5]

	return render(request, 'index/archive.html', {
		'solutions': solutions,
		'query': query
	})

@login_required
def solution(request, id):
	user = User.objects.get(username=request.user)
	solution = Solution.objects.get(id=id)

	return render(request, 'index/solution.html', {
		'solution': solution,
		'user': user
	})

def about(request):
	return render(request, 'index/index.html', {})

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
