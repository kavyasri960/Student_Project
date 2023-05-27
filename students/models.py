from django.db import models

# Create your models here.
class Students1(models.Model):
            Student_id = models.TextField();
            Student_Name = models.TextField(max_length=40);
            Student_TotalMarks = models.TextField();
            class Meta:
                db_table = "myfirstdb"
