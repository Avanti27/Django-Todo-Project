from django.contrib import admin
from app.models import Course

#from .models import Course
#changing Django adminstration Heading

admin.site.site_header="Course Admin Panel"
#changing title in the tab
admin.site.site_title="Course"
class CourseAdmin(admin.ModelAdmin):

    list_display=('id','cname','cdur','cprice')
    list_filter=['cname','cdur']

# Register your models here.
#admin.site.register(Course)
admin.site.register(Course,CourseAdmin)