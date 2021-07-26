from datetime import timedelta
from django.db import models

SM2_DEFAULT_INTERVAL = timedelta(days=1)

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
    interval = models.DurationField(default=SM2_DEFAULT_INTERVAL)

    def __str__(self):
        return f'{self.question}'

    def update(self, feedback):
        """
        Updates current flashcard's infos using user feedback 
        and SM2 algorithm.
        """

        # Is given answer correct ?
        if feedback >= 3:

            # Interval
            if self.repetitions == 0:
                self.interval = SM2_DEFAULT_INTERVAL
            elif self.repetitions == 1:
                self.interval = timedelta(days=6)
            else:
                self.interval *= self.easiness_factor

            # Easiness factor
            self.easiness_factor += 0.1 - (5 - feedback) * \
                    (0.08 + (5 - feedback) * 0.02)

            if self.easiness_factor <= 1.3: # SM2 specification
                self.easiness_factor = 1.3

            # Repetitions
            self.repetitions += 1

        else:

            # Reset everything
            self.repetitions = 0
            self.interval = SM2_DEFAULT_INTERVAL
