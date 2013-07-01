from django.db import models

class message(models.Model) :
        body_message = models.TextField(max_length=80)

        def __str__(self) :
              return (self.body_message)
