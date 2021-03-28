from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):

    if request.method == 'POST':
        # validate data 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('articles:list')

    else:

        form = UserCreationForm()
        
    data = {"form": form}
    return render(request, 'accounts/signup.html', data)


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            
            return redirect('articles:list')       
    else:
        form = AuthenticationForm()

    data = {"form": form}
    return render(request, 'accounts/login.html', data)


def logout_view(request):

    # logging out using a POST request
    if request.method == 'POST':
        logout(request)

        return redirect('articles:list')