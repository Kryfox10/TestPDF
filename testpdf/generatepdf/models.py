from django.db import models

# Create your models here.

class Syllia(models.Model):
  college = models.CharField(max_length=100)
  course_code = models.CharField(max_length=8)
  instructor = models.CharField(max_length=150)

  def __unicode__(self):
    return self.college
    return self.course_code
    return self.instructor
