from datetime import timedelta
from django.db import models

# Flashcard model
class Flashcard(models.Model):
    """
    Simple flashcard representation with a pair question/answer.
    And informations for SM2 algorithm (repetition, easiness_factor
    and interval).
    """

    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    # Internal fields
    repetitions = models.PositiveIntegerField(default=0)
    easiness_factor = models.FloatField(default=2.5) # SM2 specification
    interval = models.DurationField(default=timedelta(days=1))

    def __str__(self):
        return f'{self.question}'
