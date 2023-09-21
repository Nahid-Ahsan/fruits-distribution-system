from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Banner, SystemOverview, Food, TradingSummary, SellOffer, Management, TreatmentInfoSummary, Footer
from .serializers import BannerSerializer, SystemOverviewSerializer, FoodSerializer, TradingSummarySerializer, SellOfferSerializer, ManagementSerializer, TreatmentInfoSummarySerializer, FooterSerializer

class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer



class SystemOverviewList(generics.ListAPIView):
    queryset = SystemOverview.objects.all()
    serializer_class = SystemOverviewSerializer


class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class TradingSummaryList(generics.ListAPIView):
    queryset = TradingSummary.objects.all()
    serializer_class = TradingSummarySerializer


class SystemOverviewList(generics.ListAPIView):
    queryset = SystemOverview.objects.all()
    serializer_class = SystemOverviewSerializer


class SellOfferList(generics.ListAPIView):
    queryset = SellOffer.objects.all()
    serializer_class = SellOfferSerializer

class ManagementList(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

class TreatmentInfoSummaryList(generics.ListAPIView):
    queryset = TreatmentInfoSummary.objects.all()
    serializer_class = TreatmentInfoSummarySerializer

class FooterList(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


