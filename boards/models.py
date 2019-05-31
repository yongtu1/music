from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    file= models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards')
    
    def __str__(self):
        return f'{self.id}번글 - {self.title}:{self.content}'
        
class Comment(models.Model):
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id})>'