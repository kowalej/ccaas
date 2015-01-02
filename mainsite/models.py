
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.galleries.models import *
from mezzanine.blog.models import BlogCategory
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField


class LocalSchoolSet(Page, RichText):

	class Meta:
		verbose_name = _("Canadian school group")
		verbose_name_plural = _("Canadian school groups")

class ForeignSchoolSet(Page, RichText):

	class Meta:
		verbose_name = _("Kenyan school group")
		verbose_name_plural = _("Kenyan school groups")

class ProgramSet(Page, RichText):

	class Meta:
		verbose_name = _("Program group")
		verbose_name_plural = _("Program groups")

class EventSet(Page, RichText):

	class Meta:
		verbose_name = _("Event group")
		verbose_name_plural = _("Event groups")

class Program(Page, RichText):
	gallery = models.ForeignKey(Gallery, blank=True, null=True)
	blog_category = models.ForeignKey(BlogCategory, blank=True, null=True)

	class Meta:
		verbose_name = _("Program")
		verbose_name_plural = _("Programs")

class Event(Page, RichText):

	class Meta:
		verbose_name = _("Event")
		verbose_name_plural = _("Events")

class LocalSchool(Page):
	country = models.CharField("Country", max_length=60)
	address = models.CharField("Address", max_length=300, blank=True)
	city = models.CharField("City/Region", max_length=200, blank=True)
	state = models.CharField("Province/State", max_length=100, blank=True)
	zipcode = models.CharField("Postal/Zip Code", max_length=10, blank=True)
	telephone = models.CharField("Telephone", max_length=20, blank=True)
	website = models.CharField("Website", max_length=200, blank=True)
	programs = models.ManyToManyField("Program", blank=True, null=True)
	logo = FileField(verbose_name=_("Logo"), null=True,
                               upload_to="school_logos", max_length=255, blank=True)
	gallery = models.ForeignKey(Gallery, blank=True, null=True)
	blog_category = models.ForeignKey(BlogCategory, blank=True, null=True)

	class Meta:
		verbose_name = _("Canadian school")
		verbose_name_plural = _("Canadian schools")

class ForeignSchool(Page, RichText):
	country = models.CharField("Country", max_length=60)
	address = models.CharField("Address", max_length=300, blank=True)
	city = models.CharField("City/Region", max_length=200, blank=True)
	state = models.CharField("Province/State", max_length=100, blank=True)
	zipcode = models.CharField("Postal/Zip Code", max_length=10, blank=True)
	headteacher = models.CharField("Head Teacher", max_length=300, blank=True)
	students = models.DecimalField("Number of Students", max_digits=6, decimal_places=0, blank=True, null=True)
	teachers = models.DecimalField("Number of Teachers", max_digits=5, decimal_places=0, blank=True, null=True)
	programs = models.ManyToManyField("Program", blank=True, null=True)
	gallery = models.ForeignKey(Gallery, blank=True, null=True)
	blog_category = models.ForeignKey(BlogCategory, blank=True, null=True)

	class Meta:
		verbose_name = _("Kenyan school")
		verbose_name_plural = _("Kenyan schools")

class PageCategory(Page, RichText):

	class Meta:
		verbose_name = _("Page category")
		verbose_name_plural = _("Page categories")

class Slide(Page, RichText):
	slide_link = models.CharField("Slide Link", blank=True, max_length=300)
	caption = models.CharField("Caption", blank=True, max_length=500)

	class Meta:
		verbose_name = _("Front Page Slide")
		verbose_name_plural = _("Front Page Slides")

class ExtraFact(Page, RichText):

	class Meta:
		verbose_name = _("Extra fact")
		verbose_name_plural = _("Extra facts")

