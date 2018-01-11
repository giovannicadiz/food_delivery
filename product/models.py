from django.db import models

"""
Class in this model : 

MainCourse
SideDish
Salad
Dessert
Drink
Menu
"""


# Create your models here.
class MainCourse(models.Model):
    # Attributes
    name = models.CharField(max_length=30)

    # Add model representation strings
    def __str__(self):
        return u'%s ' % self.name

    # Meta class for the model.
    class Meta:
        verbose_name = 'Main Course'
        verbose_name_plural = 'Main Courses'


class SideDish(models.Model):
    # Attributes
    name = models.CharField(max_length=30)

    # Add model representation strings
    def __str__(self):
        return u'%s ' % self.name

    # Meta class for the model.
    class Meta:
        verbose_name = 'Side Dish'
        verbose_name_plural = 'Side Dish'


class Salad(models.Model):
    # Attributes
    name = models.CharField(max_length=30)

    # Add model representation strings
    def __str__(self):
        return u'%s ' % self.name

    # Meta class for the model.
    class Meta:
        verbose_name = 'Salad'
        verbose_name_plural = 'Salads'


class Dessert(models.Model):
    # Attributes
    name = models.CharField(max_length=30)

    # Add model representation strings
    def __str__(self):
        return u'%s ' % self.name

    # Meta class for the model.
    class Meta:
        verbose_name = 'Dessert'
        verbose_name_plural = 'Desserts'


class Drink(models.Model):
    # Attributes
    name = models.CharField(max_length=30)

    # Add model representation strings
    def __str__(self):
        return u'%s ' % self.name

    # Meta class for the model.
    class Meta:
        verbose_name = 'Drink'
        verbose_name_plural = 'Drinks'


class Menu(models.Model):
    # Attributes
    name = models.CharField(max_length=30)
    # Relations
    mainCourse = models.ForeignKey(MainCourse)
    sideDish = models.ForeignKey(SideDish)
    salad = models.ForeignKey(Salad)
    dessert = models.ForeignKey(Dessert)
    drink = models.ForeignKey(Drink)

    # Add model representation strings
    def __str__(self):
        return u'%s %s %s %s %s %s' % (
            self.name, self.mainCourse, self.sideDish, self.salad, self.dessert, self.drink
        )

    # Meta class for the model.
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'