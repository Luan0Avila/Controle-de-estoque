from django.shortcuts import render, redirect
from django.urls import reverse
from .forms.register_form import RegisterForm
from django.http import Http404
from django.contrib import messages

def register_user(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'user/pages/register.html', {
        'form': form,
        'form_action': reverse('user:register_create')
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado com sucesso. Agora faça seu login.')


    return redirect('user:register')
