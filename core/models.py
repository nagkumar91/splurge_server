from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Recipient(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email_id = models.EmailField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Recipients"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Sender(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name


class GiftCard(TimeStampedModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    amount = models.BigIntegerField()
    expiry_date = models.DateField()
    used = models.BooleanField(default=False)
    recipient = models.ForeignKey(Recipient, related_name="giftcards", null=True)
    category = models.ForeignKey(Category, related_name="giftcards", null=True)
    sender = models.ForeignKey(Sender, related_name="giftcards")

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.amount

    class Meta:
        verbose_name_plural = "Gift Cards"