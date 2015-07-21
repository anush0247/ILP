from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from django import forms

from Auth.models import ILPUser

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = ILPUser
		fields = ('EmpNo','FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile')

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = ILPUser
		fields = ('EmpNo','FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile','is_active', 'is_admin')
		
	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]

class ILPUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('EmpNo', 'FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile','is_admin')
	list_filter = ('Profile',)
	ordering = ('EmpNo',)
	filter_horizontal = ()
	fieldsets = (
		("Credentital", {"fields" : ("EmpNo","password")}),
		("Basic Info", {"fields" : ( 'FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile',)}),
		('Permissions', {'fields': ('is_admin','is_active')}),
	)

	add_fieldsets = (
		("Credentital", {"fields" : ("EmpNo","password1", "password2")}),
		("Basic Info", {"fields" : ( 'FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile',)}),
		('Permissions', {'fields': ('is_admin','is_active')}),
	)
	#exclude = ('username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'groups', 'user_permissions', 'email', 'date_joined')

admin.site.register(ILPUser, ILPUserAdmin)
admin.site.unregister(Group)
# Register your models here.

