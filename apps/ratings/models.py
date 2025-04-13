from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile
from real_estate.settings.base import AUTH_USER_MODEL


class Rating(TimeStampedUUIDModel):

    class Range(models.IntegerChoices):
        RANGE_1 = 1, _("RUIM")
        RANGE_2 = 2, _("REGULAR")
        RANGE_3 = 3, _("BOM")
        RANGE_4 = 4, _("MUITO BOM")
        RANGE_5 = 5, _("EXCELENTE")

    rater = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name=_("Votante"), on_delete=models.SET_NULL, null=True
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Corretor"),
        related_name="agent_review",
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        verbose_name=_("Avaliação"),
        choices=Range.choices,
        help_text="1=Ruim, 2=Regular, 3=Bom, 4=Muito Bom, 5=Excelente",
        default=0,
    )
    comment = models.TextField(verbose_name=_("Comentário"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"Avaliação de {self.rater} para {self.agent}"
