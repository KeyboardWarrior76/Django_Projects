from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post


def posts_index(request):
    posts = list(Post.objects.all().values())

    return JsonResponse({ "posts": posts})

