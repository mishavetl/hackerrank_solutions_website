from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.http import HttpResponseRedirect
import random

from django.contrib.auth.models import User

def check_register_form(username, passw, passw2, args, captcha, captcha_answer):
	if len(captcha) == 0:
		args['error_captcha'] = "This field is required"

	elif captcha != captcha_answer:
		args['error_captcha'] = "Invalid answer"

	if len(username) == 0:
		args['error_user'] = "This field is required"

	elif username.find(" ") > 0:
		args['error_user'] = "Username mustn't contain spaces"

	if len(passw) == 0:
		args['error_passw'] = "This field is required"

	if len(passw2) == 0:
		args['error_passw2'] = "This field is required"

	elif passw != passw2:
		args['error_passw2'] = "Passwords don't match"

	try:
		args['error_user']
	except KeyError:
		try:
			user = User.objects.get(username=username)

		except User.DoesNotExist:
			foo = ""
		else:
			args['error_user'] = "User with this username already exists"

	return args

def register(request):
	# print request.user.is_authenticated()
	if request.user.is_authenticated() == False:
		captcha_texts = {"1 + 1": "2", "5 + 3": "8"}
		captcha_text_ = random.choice(captcha_texts.keys())

		if request.method == 'POST':
			username = request.POST['username']
			passw = request.POST['passw']
			passw2 = request.POST['passw2']
			captcha_text = request.POST['captcha_text']
			captcha_answer = captcha_texts[captcha_text]
			captcha = request.POST['captcha']
			args = {'captcha_text': captcha_text_}

			args = check_register_form(username, passw, passw2, args, captcha, captcha_answer)

			if len(args) > 1:
				return render(request, 'auth/register.html', args)

			else:
				user = User.objects.create_user(username, '', passw)
				user.save()
				user = authenticate(username=username, password=passw)
				login(request, user)
				return HttpResponseRedirect('/')
		else:
			return render(request, 'auth/register.html', {'captcha_text': captcha_text_})
	else:
		return HttpResponseRedirect('/')
