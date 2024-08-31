from django.shortcuts import render
from . import models
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.


class indexView(View):
    def get(self,request):
        produtos = models.Produto.objects.all()
        return render(request, "index.html", context={"produtos":produtos})
    
    def post(self,request):
        print(request.POST)
        if request.POST.get("method") == 'create':
            models.Produto.objects.create(
                nome=request.POST.get("nome"),
                descricao=request.POST.get("descricao"),
                preco=request.POST.get("preco"),
                codigo=request.POST.get("codigo")
            )
        if request.POST.get("method") == 'delete':
            models.Produto.objects.get(id= request.POST.get("id")).delete()
        
        if request.POST.get("method") == 'update':
            obj = models.Produto.objects.get(id= request.POST.get("id"))
            obj.nome = request.POST.get("nome")
            obj.descricao = request.POST.get("descricao")
            obj.preco = request.POST.get("preco")
            obj.codigo = request.POST.get("codigo")
            obj.save()
        return HttpResponseRedirect("/")
