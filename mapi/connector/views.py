# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from connector.models import UserHierarchy, UserList, ArtList, ArtLikes, ArtCmt, Blog, BlogCmt, BlogLikes
from connector.serializers import UserHierarchySerializer, UserListSerializer, ArtListSerializer, ArtLikesSerializer
from connector.serializers import ArtCmtSerializer, BlogSerializer, BlogCmtSerializer, BlogLikesSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def hierarchyApi(request, id=0):
    if request.method == 'GET':
        hierarchy = UserHierarchy.objects.all()
        hierarchy_serializer = UserHierarchySerializer(hierarchy, many=True)
        return JsonResponse(hierarchy_serializer.data, safe=False)
    elif request.method == 'POST':
        hierarchy_data = JSONParser().parse(request)
        hierarchy_serializer = UserHierarchySerializer(data=hierarchy_data)
        if hierarchy_serializer.is_valid():
            hierarchy_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        hierarchy_data = JSONParser().parse(request)
        hierarchy = UserHierarchy.objects.get(UH_ID=hierarchy_data['UH_ID'])
        hierarchy_serializer = UserHierarchySerializer(hierarchy, data=hierarchy_data)
        if hierarchy_serializer.is_valid():
            hierarchy_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        hierarchy = UserHierarchy.objects.get(UH_ID=id)
        hierarchy.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        user = UserList.objects.all()
        user_serializer = UserListSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserListSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = UserList.objects.get(UL_ID=user_data['UL_ID'])
        user_serializer = UserListSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        user = UserList.objects.get(UL_ID=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# ArtList,
@csrf_exempt
def artsApi(request, id=0):
    if request.method == 'GET':
        arts = ArtList.objects.all()
        arts_serializer = ArtListSerializer(arts, many=True)
        return JsonResponse(arts_serializer.data, safe=False)
    elif request.method == 'POST':
        arts_data = JSONParser().parse(request)
        arts_serializer = ArtListSerializer(data=arts_data)
        if arts_serializer.is_valid():
            arts_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        arts_data = JSONParser().parse(request)
        arts = ArtList.objects.get(AL_ID=arts_data['AL_ID'])
        arts_serializer = ArtListSerializer(arts, data=arts_data)
        if arts_serializer.is_valid():
            arts_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        arts = ArtList.objects.get(AL_ID=id)
        arts.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# ArtLikes,
@csrf_exempt
def artLikesApi(request, id=0):
    if request.method == 'GET':
        artLikes = ArtLikes.objects.all()
        artLikes_serializer = ArtLikesSerializer(artLikes, many=True)
        return JsonResponse(artLikes_serializer.data, safe=False)
    elif request.method == 'POST':
        artLikes_data = JSONParser().parse(request)
        artLikes_serializer = ArtLikesSerializer(data=artLikes_data)
        if artLikes_serializer.is_valid():
            artLikes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        artLikes_data = JSONParser().parse(request)
        artLikes = ArtLikes.objects.get(ALi_ID=artLikes_data['ALi_ID'])
        artLikes_serializer = ArtLikesSerializer(artLikes, data=artLikes_data)
        if artLikes_serializer.is_valid():
            artLikes_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        artLikes = ArtLikes.objects.get(ALi_ID=id)
        artLikes.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# ArtCmt,
@csrf_exempt
def artCmtApi(request, id=0):
    if request.method == 'GET':
        artCmt = ArtCmt.objects.all()
        artCmt_serializer = ArtCmtSerializer(artCmt, many=True)
        return JsonResponse(artCmt_serializer.data, safe=False)
    elif request.method == 'POST':
        artCmt_data = JSONParser().parse(request)
        artCmt_serializer = ArtCmtSerializer(data=artCmt_data)
        if artCmt_serializer.is_valid():
            artCmt_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        artCmt_data = JSONParser().parse(request)
        artCmt = ArtCmt.objects.get(AC_ID=artCmt_data['AC_ID'])
        artCmt_serializer = ArtCmtSerializer(artCmt, data=artCmt_data)
        if artCmt_serializer.is_valid():
            artCmt_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        artCmt = UserList.objects.get(AC_ID=id)
        artCmt.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# Blog,
@csrf_exempt
def blogApi(request, id=0):
    if request.method == 'GET':
        blog = Blog.objects.all()
        blog_serializer = BlogSerializer(blog, many=True)
        return JsonResponse(blog_serializer.data, safe=False)
    elif request.method == 'POST':
        blog_data = JSONParser().parse(request)
        blog_serializer = BlogSerializer(data=blog_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        blog_data = JSONParser().parse(request)
        blog = Blog.objects.get(B_ID=blog_data['B_ID'])
        blog_serializer = BlogSerializer(blog, data=blog_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        blog = Blog.objects.get(B_ID=id)
        print(id)
        blog.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# BlogCmt,
@csrf_exempt
def blogCmtApi(request, id=0):
    if request.method == 'GET':
        blogCmt = BlogCmt.objects.all()
        blogCmt_serializer = BlogCmtSerializer(blogCmt, many=True)
        return JsonResponse(blogCmt_serializer.data, safe=False)
    elif request.method == 'POST':
        blogCmt_data = JSONParser().parse(request)
        blogCmt_serializer = BlogCmtSerializer(data=blogCmt_data)
        if blogCmt_serializer.is_valid():
            blogCmt_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        blogCmt_data = JSONParser().parse(request)
        blogCmt = BlogCmt.objects.get(BC_ID=blogCmt_data['BC_ID'])
        blogCmt_serializer = BlogCmtSerializer(blogCmt, data=blogCmt_data)
        if blogCmt_serializer.is_valid():
            blogCmt_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        blogCmt = BlogCmt.objects.get(BC_ID=id)
        blogCmt.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


# BlogLikes
@csrf_exempt
def blogLikesApi(request, id=0):
    if request.method == 'GET':
        blogLikes = BlogLikes.objects.all()
        blogLikes_serializer = BlogLikesSerializer(blogLikes, many=True)
        return JsonResponse(blogLikes_serializer.data, safe=False)
    elif request.method == 'POST':
        blogLikes_data = JSONParser().parse(request)
        blogLikes_serializer = BlogLikesSerializer(data=blogLikes_data)
        if blogLikes_serializer.is_valid():
            blogLikes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        blogLikes_data = JSONParser().parse(request)
        blogLikes = BlogLikes.objects.get(BL_ID=blogLikes_data['BL_ID'])
        blogLikes_serializer = BlogLikesSerializer(blogLikes, data=blogLikes_data)
        if blogLikes_serializer.is_valid():
            blogLikes_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == "DELETE":
        blogLikes = BlogLikes.objects.get(BL_ID=id)
        blogLikes.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Failed: " + request.method)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
