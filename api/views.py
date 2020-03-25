from rest_framework.response import Response
from .serializers import PostsSerializer
from rest_framework.decorators import api_view
from blog.models import Posts
from django.http import Http404


@api_view(['GET'])
def posts_list(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def posts_detail(request, pk):
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        raise Http404
    serializer = PostsSerializer(post, many=False)
    return Response(serializer.data)