from django.db import models

# Create your models here.


class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class Emoji(models.Model):
    value = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', related_name='emojis')

    def __str__(self):
        return self.value


class EmojiSequence(models.Model):
    emoji = models.ManyToManyField('Emoji', related_name='sequences')
    tags = models.ManyToManyField('Tag', related_name='sequences')

    def __str__(self):
        return f'{",".join(self.emoji)} ({",".join(self.tags)})'
