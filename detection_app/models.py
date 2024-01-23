from django.db import models

class ObjectDetection(models.Model):
    bounding_box_origin_x = models.FloatField()
    bounding_box_origin_y = models.FloatField()
    bounding_box_width = models.FloatField()
    bounding_box_height = models.FloatField()

    categories_index = models.IntegerField()
    categories_score = models.FloatField()
    categories_display = models.CharField(max_length=255)
    categories_category_name = models.CharField(max_length=255)

    def __str__(self):
        return f'ObjectDetection: {self.id}'

class PoseDetection(models.Model):
    for i in range(32):
        locals()[f'pl{i}x'] = models.FloatField()
        locals()[f'pl{i}y'] = models.FloatField()
        locals()[f'pl{i}z'] = models.FloatField()
        locals()[f'pl{i}visibility'] = models.FloatField()
        locals()[f'pl{i}presence'] = models.FloatField()
        locals()[f'pwl{i}x'] = models.FloatField()
        locals()[f'pwl{i}y'] = models.FloatField()
        locals()[f'pwl{i}z'] = models.FloatField()
        locals()[f'pwl{i}visibility'] = models.FloatField()
        locals()[f'pwl{i}presence'] = models.FloatField()

    def __str__(self):
        return f'PoseDetection: {self.id}'