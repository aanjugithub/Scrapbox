from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from django.views import View

from .models import Scrapbox, WishList
from scrapbox.models import Scrapbox,UserProfile,WishList,BasketItem,CartItem

from django.views.generic import View,CreateView,UpdateView,DetailView
from scrapbox.forms import UserForm,LoginForm,ScrapboxForm,UserProfileForm,BasketForm,BasketItemForm
from scrapbox.forms import UserCreationForm #UserProfile
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
           return render(request,"register.html",{"form":form})
        

#login view
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        print("login form..........")
        if form.is_valid():
            print("start login session....")
            username1=form.cleaned_data.get("username")
            password1=form.cleaned_data.get("password")
            print("user details....",username1,password1)
            user_object=authenticate(request,username=username1,password=password1)
            if user_object:
                print("valid credentilas..........")
                login(request,user_object)
                return redirect("index")
            
        print("invalid credentials..........")
        return render(request,"login.html",{"form":form})
    
#index view
#http://127.0.0.1:8000/scrap/create
class ScrapCreateView(View):
    def get(self,request,*args,**kwargs):
        form=ScrapboxForm()
        return render(request,"scrapbox_add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=ScrapboxForm(request.POST,files=request.FILES)
        if form.is_valid():
                form.save()
                return redirect('index')
        else:
               
                return render(request,"login.html",{"form":form})


# scrap update view
#http://127.0.0.1:8000/scrap/{id}/update
        
class ScrapUpdateView(View):
  
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        obj=Scrapbox.objects.get(id=id)
        form=ScrapboxForm(instance=obj)
        return render(request,"scrapupdate.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Scrapbox.objects.get(id=id)
        form=ScrapboxForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            if form.instance.user == request.user:
                form.save()
                return redirect("list-all")
            else:
                messages.error(request,"You are not authorized to update the product")
                return render(request, "scrapupdate.html", {"form": form})
        else:
            print("can't update .......")
            messages.error(request," data updation failed....")
            return render(request,"scrapupdate.html",{"form":form})


#list view
class ScrapboxListView(View):
    def get(self,request,*args,**kwargs):
        qs=Scrapbox.objects.all()
        return render(request,"scrapboxlist.html",{"data":qs})
                                



#signout

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
#item view -retrive
class ItemView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Scrapbox.objects.get(id=id)
        return render(request,"scrapboxitem_view.html",{"data":qs})
    
    

#user profile view
# 
class ProfileDetailView(DetailView):
        template_name="profile_detail.html"
        model=UserProfile
        context_object_name="data"
        
    
class ProfileUpdateView(UpdateView):
    template_name="profile_add.html"
    form_class=UserProfileForm
    model=UserProfile

    def get_success_url(self) -> str:
        return reverse("index")
  

# add to cart from scraplist
#  url:http://127.0.0.1:8000/scrapbox/{id}/add_to_basket/
# http://127.0.0.1:8000/cart/view
    

# add to wishlist
    # http://127.0.0.1:8000/scrapbox/4/addtocart

class AddToWishList(View):
  
    def post(self, request, *args, **kwargs):
        scrapbox_id = kwargs.get("pk")
        print(scrapbox_id)
        # scrapbox_object=Scrapbox.objects.get(id=id)
        scrapbox_object = get_object_or_404(Scrapbox, id=scrapbox_id)
        print(scrapbox_object)
        action = request.POST.get("action")
        print("++++++", action)

        cart, created = WishList.objects.get_or_create(user=request.user)

        if action == "addtocart":
            
            cart.scrap.add(scrapbox_object)
            print("added......")

        return redirect("index")

           

#cart -view cart list  
# http://127.0.0.1:8000/cart/view  --cart list view


class CartListView(View):
    def get(self, request, *args, **kwargs):
        user_wishlist = WishList.objects.filter(user=request.user).first()

        return render(request, "cartlist.html", {"user_wishlist": user_wishlist})

# remove from cart 
# http://127.0.0.1:8000/cart/removve--cart delete
    
class RemoveCartItemView(View):
    def get(self, request, *args, **kwargs):
        wishlist_item_id = kwargs.get("pk")
        wishlist_item = get_object_or_404(WishList, id=wishlist_item_id, user=request.user)
        wishlist_item.delete()
        return redirect("cartlist-view")


#item add view

class IndexView(CreateView):
    template_name="index.html"
    form_class=ScrapboxForm
    
    
    def get_success_url(self) -> str:
        return reverse("index")


#
@login_required
def add_to_cart(request, product_id):
    product = Scrapbox.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
   



    
