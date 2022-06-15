from django.contrib import admin
from . models import Assignment, Submission

# Register your models here.
class SubmissionAdmin(admin.TabularInline):
    model = Submission

class AssignmentAdmin(admin.ModelAdmin):
    inlines = [SubmissionAdmin]
    list_display = ["course" , 'topic' , 'questions']

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission)