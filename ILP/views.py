# importing django render shortcut
from django.shortcuts import render

# importing login required decorator
from django.contrib.auth.decorators import login_required as auth


from Users.models import Participant

@auth
def HomePageView(request):
	
	context = {"participant_profile" : Participant.objects.get(participant_id = request.user), }
	return render(request, "home.html", context)
