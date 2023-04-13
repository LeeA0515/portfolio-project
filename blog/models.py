from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    def preview(self):
        return self.body[:100]+ ' ...'
    def formatDate(self):
        return self.date.strftime('%d %b %Y' + ', ' + '%a')