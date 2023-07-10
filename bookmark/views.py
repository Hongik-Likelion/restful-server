import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


def bookmark_list_viewer(request):
    data = [{'shopName': '얼스어스', 'description':'따뜻한 감성의 리필스테이션', 'distance':426, 'reviewCount':14, 'tag':['리필스테이션', '할인이벤트', '앤틱'], 'open':True},
    {'shopName': '그리너리', 'description':'원두 커피가 맛있는 제로 카페', 'distance':312, 'reviewCount':12, 'tag':['제로카페', '할인이벤트', '앤틱'], 'open':True},
    {'shopName': '지구카페', 'description':'홍대에서 제일가는 제로카페', 'distance':482, 'reviewCount':21, 'tag':['제로카페', '할인이벤트', '앤틱'], 'open':True},
    {'shopName': '카페나무', 'description':'보리차 맛이 나는 아아', 'distance':516, 'reviewCount':23, 'tag':['리필스테이션', '할인이벤트', '모던'], 'open':True},
    {'shopName': '메가커피', 'description':'홍대제일 가성비 카페', 'distance':527, 'reviewCount':11, 'tag':['가성비', '할인이벤트', '붐비는'], 'open':True},
    {'shopName': '가비아', 'description':'24시간 카페', 'distance':654, 'reviewCount':15, 'tag':['가성비', '할인이벤트', '24시간'], 'open':True}
    ]

    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
