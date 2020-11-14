# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.CharField(db_column='areaID', primary_key=True, max_length=10)  # Field name made lowercase.
    area_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'area'


class Bulletin(models.Model):
    bulletinid = models.CharField(db_column='bulletinID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulletin'


class Contains(models.Model):
    bulletinid = models.CharField(db_column='bulletinID', primary_key=True, max_length=10)  # Field name made lowercase.
    sessionid = models.CharField(db_column='sessionID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contains'
        unique_together = (('bulletinid', 'sessionid'),)


class Creates(models.Model):
    computingid = models.CharField(db_column='computingID', primary_key=True, max_length=10)  # Field name made lowercase.
    sessionid = models.CharField(db_column='sessionID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'creates'
        unique_together = (('computingid', 'sessionid'),)


class DescribedBy(models.Model):
    areaid = models.CharField(db_column='areaID', primary_key=True, max_length=10)  # Field name made lowercase.
    bulletinid = models.CharField(db_column='bulletinID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'described_by'
        unique_together = (('areaid', 'bulletinid'),)


class Has(models.Model):
    areaid = models.CharField(db_column='areaID', primary_key=True, max_length=10)  # Field name made lowercase.
    computingid = models.CharField(db_column='computingID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'has'
        unique_together = (('areaid', 'computingid'),)


class Participants(models.Model):
    computingid = models.CharField(db_column='computingID', primary_key=True, max_length=10)  # Field name made lowercase.
    sessionid = models.CharField(db_column='sessionID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participants'
        unique_together = (('computingid', 'sessionid'),)


class Session(models.Model):
    sessionid = models.CharField(db_column='sessionID', primary_key=True, max_length=10)  # Field name made lowercase.
    study_area = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'session'

    def __str__(self):
        return self.sessionid


class SessionRating(models.Model):
    sessionid = models.CharField(db_column='sessionID', primary_key=True, max_length=10)  # Field name made lowercase.
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'session_rating'
        unique_together = (('sessionid', 'rating'),)


class User(models.Model):
    computingid = models.CharField(db_column='computingID', primary_key=True, max_length=10)  # Field name made lowercase.
    name_first = models.CharField(max_length=50)
    name_last = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'


class UserPhone(models.Model):
    computingid = models.CharField(db_column='computingID', primary_key=True, max_length=10)  # Field name made lowercase.
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'user_phone'
        unique_together = (('computingid', 'phone'),)
