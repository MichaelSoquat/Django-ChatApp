from django.db import models
from datetime import date, datetime
from django.conf import settings

# chat class
class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=128, unique=True, default = None)
    def __str__(self):
        return "{0}".format(self.name)


#message class
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    time_created_at = models.DateTimeField(default=datetime.now())
    # chat = Chat Klasse verknüpfen
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name ='chat_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ='receiver_message_set')

    def __str__(self):
        return "{0}".format(self.text)


