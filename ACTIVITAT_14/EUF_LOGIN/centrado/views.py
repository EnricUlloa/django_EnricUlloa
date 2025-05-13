from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .forms import createUserForm
from .models import Usuario

def index(request):
    return render(request,'index.html')

def page_home(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects.filter(id=usuario_id).first()
    if not usuario:
        return redirect('iniciar-sesion')
    return render(request, 'paginaLogin.html', {'usuario': usuario})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.password):
                request.session['usuario_id'] = user.id
                return redirect('pagina-principal')
            else:
                error = 'Contraseña errónea'
        except Usuario.DoesNotExist:
            error = 'User Not Found'

        return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def log_out(request):
    request.session.flush()
    return redirect('iniciar-sesion')

def create_user(request):
    success = False
    if request.method == 'POST':
        form = createUserForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])
            usuario.save()
            success = True
    else:
        form = createUserForm()

    return render(request, 'createUser.html', {'form': form, 'success': success})