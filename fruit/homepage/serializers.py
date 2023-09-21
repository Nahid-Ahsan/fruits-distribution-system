from rest_framework import serializers
from .models import Banner, SystemOverview, Food, TradingSummary, SellOffer, Management, TreatmentInfoSummary, Footer

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class SystemOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemOverview
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class TradingSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingSummary
        fields = '__all__'


class SellOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOffer
        fields = '__all__'

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'

class TreatmentInfoSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentInfoSummary
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'