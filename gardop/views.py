from django.shortcuts import render, get_object_or_404

def start(request):
	if request.user.is_authenticated():
		return render(request,'index.html',{})
	else:    
		return render(request, 'sign/signin.html', {})