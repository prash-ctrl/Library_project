from django.shortcuts import render, redirect
from . forms import CreateUserForm
# Create your views here.
def register(request):
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form':form})