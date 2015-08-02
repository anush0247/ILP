# importing django render shortcut
from django.shortcuts import render

# importing login required decorator
from django.contrib.auth.decorators import login_required as auth


from Users.models import Participant

import django
from django.conf import settings
from django.core.mail import send_mail



@auth
def HomePageView(request):

	#send_mail('Django Email Testing', 'Here is the message Demo message.', settings.EMAIL_HOST_USER, [settings.DEFAULT_TO_EMAIL,'anushkumar247@gmail.com'] , fail_silently=False)
	
	context = {"participant_profile" : Participant.objects.get(participant_id = request.user), }
	return render(request, "home.html", context)
