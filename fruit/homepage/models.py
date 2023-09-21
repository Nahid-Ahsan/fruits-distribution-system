from django.db import models


class Banner(models.Model):
    content = models.TextField()

class SystemOverview(models.Model):
    content = models.TextField()

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class TradingSummary(models.Model):
    content = models.TextField()

class SellOffer(models.Model):
    content = models.TextField()

class Management(models.Model):
    content = models.TextField()

class TreatmentInfoSummary(models.Model):
    content = models.TextField()

class Footer(models.Model):
    content = models.TextField()

