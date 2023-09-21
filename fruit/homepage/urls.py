from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.BannerList.as_view(), name='banner-list'),
    path('SystemOverview/', views.SystemOverviewList.as_view(), name='SystemOverview-list'),
    path('Food/', views.FoodList.as_view(), name='Food-list'),
    path('TradingSummary/', views.TradingSummaryList.as_view(), name='TradingSummary-list'),
    path('SellOffer/', views.SellOfferList.as_view(), name='SellOffer-list'),
    path('Management/', views.ManagementList.as_view(), name='Management-list'),
    path('TreatmentInfoSummary/', views.TreatmentInfoSummaryList.as_view(), name='TreatmentInfoSummary-list'),
    path('Footer/', views.FooterList.as_view(), name='Footer-list'),    
]


"""
-------------- API of Homepage -------------------

{base-url}/homepage/banner/
{base-url}/homepage/SystemOverview/
{base-url}/homepage/Food/
{base-url}/homepage/TradingSummary/
{base-url}/homepage/SellOffer/
{base-url}/homepage/Management/
{base-url}/homepage/TreatmentInfoSummary/
{base-url}/homepage/Footer/



"""