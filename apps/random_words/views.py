from django.shortcuts import render, redirect
import random
import string

def index(request):
	if "key" not in request.session:
		request.session["key"] = 0
	if "string" not in request.session:
		request.session["string"] = ""

	return render(request, 'random_words/index.html', )

def show(request):
	request.session["key"] += 1

	arr = []
	for num in range(1, 15):
		arr.append(random.choice(string.ascii_uppercase+string.digits))
		request.session["string"] = "".join(arr)
	
	return redirect('/')

