from django.shortcuts import render
from django.core.mail import send_mail
from . models import Song, Contact


def home(request):
	return render(request, 'band/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'band/about.html', {'title': 'About'})

def gallery(request):
	return render(request, 'band/gallery.html', {'title': 'Gallery'})	

def download(request):
	songs = Song.objects.all()
	context = {
	'title': 'Download',
	'songs': songs
	}
	return render(request, 'band/download.html', context)

def blog(request):
	return render(request, 'band/blog.html', {'title': 'Blog'})	

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phno']
		message = request.POST['msg']

		contact = Contact(name=name, email=email, phone=phone, message=message)
		contact.save()

		try:
			# sending an email
			mail_msg = "Name : " + name + "\nEmail : " + email + "\nPhone Number : " + phone + "\nMessage : " + message
			send_mail(
				'You have a new mail from: ' + name, # subject
				mail_msg, # message
				email, # from mail
				['<email-id1>','<email-id2>'], # to mail
				)
		except Exception:		
			return render(request, 'band/contact.html', {'title': 'Contact', 'error': "Mail not sent, but your data has been saved in database and our team will contact you soon."})

	else:	
		return render(request, 'band/contact.html', {'title': 'Contact'})
	#return render(request, 'band/contact.html', {'title': 'Contact'})

def booking(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		# sending an email
		msg = "Name : " + your_name + "\nPhone Number : " + your_phone + "\nEmail ID : " + your_email + "\nAddress : " + your_address + "\nRequested Time : " + your_schedule + "\nDate : " + your_date + "\nMessage/Reason of visit : " + your_message
			
		param = {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message,
		}								
		return render(request, 'band/booking.html', param)
	else:	
		return render(request, 'band/home.html', {'title': 'Home'})		