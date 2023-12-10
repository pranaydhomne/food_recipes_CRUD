from django.shortcuts import render , redirect 
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def food(request):
    if request.method =="POST":
        food_name=request.POST.get('food_name')
        food_description=request.POST.get('food_description')
        food_image=request.FILES.get('food_image')

        food = FoodRecipe.objects.create(food_name=food_name,food_description=food_description,food_image=food_image)
        
        messages.success(request,f"{food.food_name} recipe created")

    
        return redirect('/')
    food_recipes = FoodRecipe.objects.all()
    return render(request,"food.html",{'food_recipes':food_recipes})

def recipe(request):
       
    message2='tere jai ho bhai '
    food_recipes = FoodRecipe.objects.all()
    return render(request,"recipe.html",{'food_recipes':food_recipes,'message2':message2} )


def delete_recipe(request,id):
    delete=FoodRecipe.objects.get(id = id)
    delete.delete()
    return redirect('/')
    

def update_recipe(request,id):
    update=FoodRecipe.objects.get(id = id)
    food=FoodRecipe.objects.all()

    if request.method=="POST":
        food_name=request.POST.get('food_name')
        food_description=request.POST.get('food_description')
        food_image=request.FILES.get('food_image')


        update.food_name=food_name
        update.food_description=food_description


        if food_image:
            update.food_image=food_image

        update.save()
        messages.success(request,f"{food_name} update recipe")
        return redirect('/')
    return render(request,'update.html',{'food':update})



def search(request):

    query=request.GET['search']
    query_result=FoodRecipe.objects.filter(food_name__icontains=query).order_by('id')

    
    return render(request,'search.html',{'query_result':query_result})
