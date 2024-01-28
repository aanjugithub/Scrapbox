from django import forms

from django.contrib.auth.models import User  #import User model

from scrapbox.models import Scrapbox,BasketItem,WishList
from scrapbox.models import UserProfile,Posts

from django.contrib.auth.forms import UserCreationForm






#signin /reg
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"] 


        
class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

#create view

#scrapbox view

class ScrapboxForm(forms.ModelForm):
    class Meta:
        model=Scrapbox
        # fields="__all__"
        exclude=("owner",)
        
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "phone_no":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
        }


class BasketForm(forms.ModelForm):
    class Meta:
        model=WishList 
        fields="__all__"

class BasketItemForm(forms.ModelForm):
    class Meta:
        model=BasketItem
        fields="__all__"



class UserProfileForm(forms.ModelForm):
    class Meta:
        
        model=UserProfile
        fields="__all__"

        
      


     

       
   

  

