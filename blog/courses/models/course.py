from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    qualification = models.CharField(max_length=100)
    bio = models.TextField()
    picture = models.ImageField(upload_to = "media")
    facebook = models.URLField(max_length=500, default = "https://facebook.com/")
    instagram = models.URLField(max_length=500, default = "https://instagram.com/")
    gmail = models.URLField(max_length=500, default = "https://gmail.com/")
    twitter = models.URLField(max_length=500, default = "https://twitter.com/")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 50 , null = False)
    instructor = models.ForeignKey(Teacher,  on_delete=models.CASCADE, blank=True, null=True)
    slug = models.CharField(max_length = 50 , null = False , unique = True)
    description = models.CharField(max_length = 200 , null = True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "thumbnail") 
    date = models.DateTimeField(auto_now_add= True) 
    resource = models.FileField(upload_to = "resource")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    class Meta : 
        abstract = True


class Tag(CourseProperty):
    pass
    
class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


