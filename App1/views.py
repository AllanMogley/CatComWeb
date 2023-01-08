from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemberSerializer

from .models import Member
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/member-list/',
		'Detail View':'/member-detail/<str:pk>/',
		'Create':'/member-create/',
		'Update':'/member-update/<str:pk>/',
		'Delete':'/member-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def memberList(request):
	members = Member.objects.all().order_by('-id')
	serializer = TaskSerializer(members, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def memberDetail(request, pk):
	members = member.objects.get(id=pk)
	serializer = MemberSerializer(members, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def memberCreate(request):
	serializer = MemberSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def memberUpdate(request, pk):
	member = member.objects.get(id=pk)
	serializer = MemberSerializer(instance=member, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def memberDelete(request, pk):
	member = member.objects.get(id=pk)
	member.delete()

	return Response('Item succsesfully delete!')



