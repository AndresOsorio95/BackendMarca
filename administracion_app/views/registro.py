from django.contrib.auth.forms import PasswordChangeForm
from tienda_app.forms.registro import CustomUserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente.")
            return redirect(to="tienda_inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
