import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import utc
# from django.contrib.auth.decorators import login_required

from index.models import Solution
# from stories.forms import solutionForm

def index(request):
	solutions = Solution.objects.all().order_by("-created_at")[:5]
	# print solutions
	# if request.user.is_authenticated():
		# liked_solutions = request.user.liked_solutions.filter(id__in=[solution.id for solution in solutions])
	# else:
	# 	liked_solutions = []
	return render(request, 'index/index.html', {
		'solutions': solutions,
		# 'user': request.user,
		# 'liked_solutions': liked_solutions
	})

def solution(request, id):
	solution = Solution.objects.get(id=id)

	return render(request, 'index/solution.html', {
		'solution': solution
	})
