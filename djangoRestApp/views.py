from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def articlelist(request):
    if request.method == 'GET':
        snippets = Article.objects.all()
        serializer = ArticleSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def articledetails(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        article.delete()
        return JsonResponse(status=204)