from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def Home(request):
    return render(request, 'mysite/dashboard.html')

def about(request):
    return render(request, 'mysite/about.html')

def services(request):
	return render(request, 'mysite/services.html')

def contactus(request):
	if request.method == 'POST':
		print('REQUEST DATA:', request.POST)
		name = request.POST.get('your-name')
		email = request.POST.get('your-email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		data = {
		'name': name,
		'email': email,
		'subject': subject,
		'message': message
		}
		message = '''
		New message: {}

		FROM: {}
		'''.format(data['message'], data['email'])
		send_mail(data['subject'], message, '', ['christinenjeri162@gmail.com'])
		return render(request, 'mysite/dashboard.html')
	return render(request, 'mysite/contact.html')