from django.db import models
from django.contrib.auth.models import User


class AbilityScore(models.Model):
    name = models.CharField(max_length=50)
    heart = models.IntegerField(default=0)
    soul = models.IntegerField(default=0)
    body = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MeleeWeapon(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name

class Gear(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class FirstName(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name

class LastName(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class PhysicalDetail(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class Personality(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class Secret(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name


class Background(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name

class Appearance(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return self.name

class PlayerCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.ForeignKey(FirstName, on_delete=models.CASCADE)
    last_name = models.ForeignKey(LastName, on_delete=models.CASCADE)
    combat_class = models.CharField(max_length=50)
    ability_scores = models.ForeignKey(AbilityScore, on_delete=models.CASCADE)
    melee_weapon = models.ForeignKey(MeleeWeapon, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    appearance = models.ForeignKey(Appearance, on_delete=models.CASCADE)
    physical_details = models.ForeignKey(PhysicalDetail, on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE)
    background = models.ForeignKey(Background, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"