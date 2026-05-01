from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}... - {self.author}"

    @property
    def likes_count(self):
        return self.likes.count()


class Like(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='likes')
    session_id = models.CharField(max_length=100)  # Basé sur la session du navigateur
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('quote', 'session_id')

    def __str__(self):
        return f"Like on {self.quote.id} by {self.session_id[:10]}"
