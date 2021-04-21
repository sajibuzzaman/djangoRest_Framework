from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from djangoRestApp.models import Article
from djangoRestApp.serializers import ArticleSerializer

class ArticleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articleApp/article.html'

    def get(self, request):
        queryset = Article.objects.all()
        return Response({'articles': queryset})
    
class ArticleDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articleApp/article-detail.html'

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response({'serializer': serializer, 'article': article})

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'article': article})
        serializer.save()
        return redirect('ArticleList')