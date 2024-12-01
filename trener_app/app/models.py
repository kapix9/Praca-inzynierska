from django.contrib.auth.models import User
from django.db import models


class Cwiczenie(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.TextField()
    video_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name = "Edytuj swoja baze cwiczen"
        verbose_name_plural = "Baza cwiczen"

class Seria(models.Model):
    cwiczenie = models.ForeignKey(Cwiczenie, on_delete=models.CASCADE)
    ilosc_powtorzen = models.IntegerField(default=0)
    ilosc_serii = models.IntegerField(default=0)
    obciazenie = models.DecimalField(default=0, max_digits=500, decimal_places=1)
    uwagi = models.TextField(null=True, blank=True)
    tempo = models.CharField(max_length=10)
    nagraj = models.BooleanField(default=False)
    podopieczny = models.ForeignKey(User, on_delete=models.CASCADE)
    class DayTypes(models.TextChoices):
        PONIEDZIALEK = ("Poniedzialek", "poniedzialek")
        WTOREK = ("Wtorek", "wtorek")
        SRODA = ("Sroda", "sroda")
        CZWARTEK = ("Czwartek", "czwartek")
        PIATEK = ("Piatek", "piatek")
        SOBOTA = ("Sobota", "sobota")
        NIEDZIELA = ("Niedziela", "niedziela")

    dzien_tygodnia = models.CharField(max_length=64, choices=DayTypes.choices, blank=True, null=True)

    def __str__(self):
        return f"{self.cwiczenie} - {self.podopieczny}"
    class Meta:
        verbose_name = "Edytuj plan treningowy"
        verbose_name_plural = "Plany treningowe"
