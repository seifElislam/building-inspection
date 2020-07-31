from django.db import models


class Building(models.Model):
    """
    Building Model
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class MetaData(models.Model):
    """
    MetaData Model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):
    """
    Document Model
    """
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

