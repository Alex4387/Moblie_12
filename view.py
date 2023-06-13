#added
from rest_framework import viewsets
from .serializers import PostSerializer
class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer