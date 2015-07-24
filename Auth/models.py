from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, EmpNo, password, FirstName, LastName, Email, Mobile, DoB, Gender, Profile):

        if not FirstName :
            raise ValueError('Users must have a first name')

        

        user = self.model(
            EmpNo = EmpNo,
            FirstName = FirstName,
            LastName = LastName,
            DoB = DoB,
            Email = Email,
            Mobile = Mobile,
            Gender = Gender,
            Profile = Profile
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, EmpNo, password, FirstName, LastName, Email, Mobile,  DoB, Gender, Profile):

        if not FirstName :
            raise ValueError('Users must have a first name')

        
        user = self.model(
            EmpNo = EmpNo,
            FirstName = FirstName,
            LastName = LastName,
            DoB = DoB,
            Email = Email,
            Mobile = Mobile,
            Gender = Gender,
            Profile = Profile
        )

        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class ILPUser(AbstractBaseUser):
    
    EmpNo = models.IntegerField(
        verbose_name = "TCS Employee ID",
        unique = True,
    )
    
    FirstName = models.CharField(
        max_length=100,
        verbose_name = "First Name",
    )
    
    LastName = models.CharField(
        max_length=100,
        verbose_name = "Last Name",
    ) 
    
    
    
    Email = models.EmailField(
        verbose_name = "Employee Email Id",
        max_length = 100,
    )
    
    DoB = models.DateField(
        verbose_name = "Date of Birth",
    )
    

    gender_labels = (
        ("M", "Male"),
        ("F", "Female"),
    )
    
    Gender = models.CharField(
        max_length=1,
        choices=gender_labels,
        verbose_name = "Gender",
    )
    
    profile_labels = (
        ("Participant", "Participant"),
        ("Lead", "Lead"),
        ("Support", "Support")
    )
    
    Profile = models.CharField(
        max_length=11,
        choices=profile_labels,
        verbose_name = "Employee Profile",
    )

    Mobile = models.CharField(
        max_length=11,
        null = True,
        verbose_name = "Employee Mobile No",
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name = "Is Active User",
    )
    
    is_admin = models.BooleanField(
        default=False,
        verbose_name = "Is Admin",
    )
    
    
    objects = UserManager()

    USERNAME_FIELD = 'EmpNo'
    REQUIRED_FIELDS = ['FirstName', 'LastName', 'Email', 'DoB', 'Gender', 'Profile']

    def __unicode__(self):
        return unicode(self.EmpNo)

    def get_full_name(self):
        return "%s %s" %(self.FirstName, self.LastName)

    def get_short_name(self):
        return self.FirstName

    def __str__(self):              # __unicode__ on Python 2
        return self.EmpNo

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user an admin"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    

