from django.db import models

# Create your models here.
class MainCourse(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s ' % self.name


class SideDish(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s ' % self.name

class Salad(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s ' % self.name


class Dessert(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s ' % self.name


class Drink(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return u'%s ' % self.name


class Menu(models.Model):
    name = models.CharField(max_length=30)

    mainCourse = models.ForeignKey(MainCourse)
    sideDish = models.ForeignKey(SideDish)
    salad = models.ForeignKey(Salad)
    dessert = models.ForeignKey(Dessert)
    drink = models.ForeignKey(Drink)

    def __str__(self):
        return u'%s %s %s %s %s %s' % (
            self.name, self.mainCourse, self.sideDish, self.salad, self.dessert, self.drink
        )