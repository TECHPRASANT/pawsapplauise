""" 
    Author: Prashant Bhandari
    Project Name: PawsApplause
    Date: 8/6/2022

"""

from .forms import SignUpForm,ResetForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
# Create your views here.

def password_email(request):
	return render(request,'users/password_email_message.html')

def sign_up_done(request):
    return render(request, 'users/sign_up_done.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('users-sign-up-done')
    else:
        form = SignUpForm()
    return render(request, 'users/sign_up.html', {'form': form})



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = ResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = " PawsApplause Password Reset Request"
					email_template_name = "users/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'pawsapplause',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, '' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid URLs.')
					return redirect ("password_reset_done")
	password_reset_form = ResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})


def index(request):
   return render(request, 'blog/index.html')

def reportincident(request):
   return render(request, 'blog/reportincident.html')




""" from django.shortcuts import render, redirect,get_object_or_404
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm

from django.contrib import messages """
# Create your views here.

