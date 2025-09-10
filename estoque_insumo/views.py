from django.shortcuts import render

def estoque_insumo_view(request):

    return render(request, 'home.html')

def cadastrar_novo_material(request):

    return render(request, 'new_item.html')