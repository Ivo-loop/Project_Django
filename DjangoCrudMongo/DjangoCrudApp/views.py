from bson import ObjectId
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from DjangoCrudApp.models import Produto


@csrf_exempt
def add_produto(request):
    produto = Produto(nome=request.POST.get("nome"),
                      descricao=request.POST.get("descricao"),
                      preco=request.POST.get("preco"))
    produto.save()
    return HttpResponse("Inserido")


def update_produto(request, _id):
    produto = Produto.object.get(_id=ObjectId(_id))
    produto.nome = request.POST.get("nome")
    produto.descricao = request.POST.get("descricao")
    produto.preco = request.POST.get("preco")
    produto.save()

    return HttpResponse("update")


def delete_produto(request, _id):
    produto = Produto.object.get(_id=ObjectId(_id))
    produto.delete()


def read_produto(request, _id):
    produto = Produto.object.get(_id=ObjectId(_id))
    retorno = "nome: " + produto.nome + ",\ndescrição: " + produto.descricao + ",\npreço: " + produto.preco
    return HttpResponse(retorno)


def read_produto_all(request):
    produtos = Produto.object.all()
    retorno = ""
    for produto in produtos:
        retorno += "\nnome: " + produto.nome + ",\ndescrição: " + produto.descricao + ",\npreço: " + produto.preco

    return HttpResponse(retorno)
