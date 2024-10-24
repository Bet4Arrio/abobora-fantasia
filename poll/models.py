from django.db import models
from django.utils.timezone import now
# Create your models here.

class Fantasy(models.Model):
    image = models.ImageField(null=True, upload_to ='fantasias/')
    participant = models.CharField(verbose_name="Participante")
    name = models.TextField(verbose_name="Fantasia", )

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Vote(models.Model):
    fantasy = models.ForeignKey(Fantasy, on_delete=models.CASCADE, related_name="votes")
    make = models.DateTimeField(default=now)
    email = models.EmailField(default=None, null=True, blank=True)