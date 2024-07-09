from django.shortcuts import render
from app.models import *
from app.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response



class Productcurd(APIView):
    def get(self,request,pk):
        APO=Product.objects.all()
        PSO=ProductMS(APO,many=True)
        return Response(PSO.data)

    def post(self,request,pk):
        RJD=request.data
        PMSD=ProductMS(data=RJD)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'submitted successfully'})
        else:
            return Response({'FAILED'})
    

    def put(self,request,pk):
        pk=request.data['pk']
        PO=Product.objects.get(pk=pk)
        LPO=ProductMS(PO,data=request.data)
        if LPO.is_valid():
            LPO.save()
            return Response({'UPDATED successfully'})
        return Response({'FAILED'})
    
    def patch(self,request,pk):
        pk=request.data['pk']
        PO=Product.objects.get(pk=pk)
        LPO=ProductMS(PO,data=request.data,partial=True)
        if LPO.is_valid():
            LPO.save()
            return Response({'UPDATED successfully'})
        return Response({'FAILED'})
    
    def delete(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'deleted'})