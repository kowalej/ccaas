
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mainsite.models import *
from mezzanine.pages.models import RichTextPage
from mezzanine.core.admin import DisplayableAdmin


local_school_extra_fieldsets = ("country", "address", "city", "state", "zipcode", "telephone", "website", "programs", "logo", "gallery", "blog_category",)
foreign_school_extra_fieldsets = ("country", "address", "city", "state", "zipcode", "headteacher", "students", "teachers", "programs", "gallery", "blog_category",)
program_extra_fieldsets = ("gallery", "blog_category")
slide_extra_fieldsets = ("caption", "slide_link",)
featured_image_fieldset = ("featured_image_cc",)
rt_page_fieldsets = ("content", "in_menus", "login_required")

class LocalSchoolAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)
    fieldsets[0][1]["fields"] += local_school_extra_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class ForeignSchoolAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += foreign_school_extra_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class ProgramAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += program_extra_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class EventAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += featured_image_fieldset

class LocalSchoolSetAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class ForeignSchoolSetAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += featured_image_fieldset

class ProgramSetAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += featured_image_fieldset

class EventSetAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class PageCategoryAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets 
    fieldsets[0][1]["fields"] += featured_image_fieldset

class MRichTextPageAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class SlideAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets
    fieldsets[0][1]["fields"] += slide_extra_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

class ExtraFactAdmin(PageAdmin):
    fieldsets = deepcopy(DisplayableAdmin.fieldsets)
    fieldsets[0][1]["fields"] += rt_page_fieldsets
    fieldsets[0][1]["fields"] += featured_image_fieldset

admin.site.register(LocalSchoolSet, LocalSchoolSetAdmin)
admin.site.register(ForeignSchoolSet, ForeignSchoolSetAdmin)
admin.site.register(ProgramSet, ProgramSetAdmin)
admin.site.register(EventSet, EventSetAdmin)
admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(LocalSchool, LocalSchoolAdmin)
admin.site.register(ForeignSchool, ForeignSchoolAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(ExtraFact, ExtraFactAdmin)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, MRichTextPageAdmin)

