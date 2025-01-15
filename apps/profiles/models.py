from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE= "Male", _("Male")
    FEMALE= "Female", _("Female")
    OTHER= "Other", _("Other")

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"),
                                     max_length = 30, default="+5561999999999")
    about_me = models.TextField(verbose_name=_("About Me"), default="Diga algo sobre você")
    license = models.CharField(verbose_name=_("Número do CRECI"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"),
                                      default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="BR", blank=False, null=False)
    city = models.CharField(verbose_name=_("Cidade"), max_length=18, default="Brasília", blank=False, null=False)
    is_Buyer= models.BooleanField(verbose_name=_("Comprador"), default=False, help_text=_("Você está procurando comprar um imóvel?"))
    is_Seller= models.BooleanField(verbose_name=_("Vendedor"), default=False, help_text=_("Você está procurando vender um imóvel?"))
    is_Agent= models.BooleanField(verbose_name=_("Corretor"), default=False, help_text=_("Você é um corretor de imóveis?"))
    top_agent= models.BooleanField(verbose_name=_("Corretor Ranqueado"), default=False)
    rating= models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    num_reviews= models.IntegerField(verbose_name=_("Número de Avaliações"), default=0, null=True, blank=True)

    def __str__(self):
        return f"Perfil {self.user.username}"