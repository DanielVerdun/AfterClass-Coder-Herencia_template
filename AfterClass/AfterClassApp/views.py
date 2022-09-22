from django.shortcuts import render

# Create your views here.

def layout(request):
    return render(request, 'Prueba/layou.html')

def template1(request):
    return render(request, 'Prueba/template1.html')

def template2(request):
    return render(request, 'Prueba/template2.html')

def template3(request):
    return render(request, 'Prueba/template3.html')

#-----------------------------------------------//-------------------------------------
#Vistas que  trabajan con bootstrap
def servicios(request):
    return render(request, "Prueba/servicios.html")

def nosotros(request):
    return render(request, "Prueba/nosotros.html")

def contacto(request):
    return render(request, "Prueba/contacto.html")