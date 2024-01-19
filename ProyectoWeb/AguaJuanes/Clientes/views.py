from django.shortcuts import render
from Clientes.models import Cliente
from django.http import HttpResponse
from Clientes.models import *
from Clientes.forms import * 
from Clientes.models import *
# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def ver_cliente(request):
    mis_clientes=Cliente.objects.all() #obtengo todos los datos de mi tabla cliente 
    info={"clientes":mis_clientes}
    return render(request,"ver_clientes.html",info)

def agregarCliente(request):
    if request.method== "POST":
        addclient=FormularioCliente(request.POST)
        if addclient.is_valid(): #ver si la informacion cargada es valida 
            info1=addclient.cleaned_data #convertir en un diccionario 
            cliente1=Cliente(nombre=info1["nombre"],apellido=info1["apellido"],direccion=info1["direccion"],telefono=info1["telefono"])
            cliente1.save()
            return render(request,"inicio.html")
    else:
        addclient=FormularioCliente()
    return render (request,"agregarCliente.html",{"formcliente":addclient})

def agregarProveedor(request):
    if request.method== "POST":
        addproveedor=FormularioProveedor(request.POST)
        if addproveedor.is_valid(): #ver si la informacion cargada es valida 
            info=addproveedor.cleaned_data #convertir en un diccionario 
            proveedor1=Proveedores(nombre=info["nombre"],direccion=info["direccion"],condicion_iva=info["condicion_iva"],cuil_cuit=info["cuil_cuit"],telefono=info["telefono"])
            proveedor1.save()
            return render(request,"inicio.html")
    else:
        addproveedor=FormularioProveedor()
    return render (request,"agregarProveedor.html",{"formproveedor":addproveedor})


def agregarProducto(request):
    if request.method== "POST":
        addproduct=addproductform(request.POST)
        if addproduct.is_valid(): #ver si la informacion cargada es valida 
            info=addproduct.cleaned_data #convertir en un diccionario 
            producto1=Productos(nombre_producto=info["nombre"],descripcion_producto=info["descripcion"],numero_producto=info["numero"])
            producto1.save()
            return render(request,"inicio.html")
    else:
        addproduct=addproductform()
    return render (request,"agregarproducto.html",{"formprod":addproduct})

def busquedaProducto(request):
    return render(request,"busquedaProducto.html")

def resultados(request):
    if request.method=="GET":
        numero_producto_pedido=request.GET["numero"]
        resultados_productos=Productos.objects.filter(numero_producto__icontains=numero_producto_pedido)
        return render (request,"resultados.html",{"productos":resultados_productos})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)