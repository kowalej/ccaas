from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from mainsite.models import *
from mezzanine.pages.models import Page
from mezzanine.utils.views import paginate

settings.use_editable()

@processor_for(ForeignSchoolSet)
def foreign_schools(request, page):
    schools = paginate(ForeignSchool.objects.all().filter(parent=page.id), request.GET.get("page", 1), settings.SCHOOLS_FOREIGN_SCHOOLS_PER_PAGE, settings.MAX_PAGING_LINKS)
    return {"schools": schools}

@processor_for(LocalSchoolSet)
def foreign_schools(request, page):
    schools = paginate(LocalSchool.objects.all().filter(parent=page.id), request.GET.get("page", 1), settings.SCHOOLS_LOCAL_SCHOOLS_PER_PAGE, settings.MAX_PAGING_LINKS)
    return {"schools": schools}

