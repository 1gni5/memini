from django.test import TestCase
from datetime import timedelta
from flashcards.models import Flashcard

class FlashcardTestCase(TestCase):
    """
    Test every aspect of flashcard model.
    """

    def test_create_flashcard(self):
        """
        Flashcards can be created with only Question
        and Answer texts.
        """

        flashcard = Flashcard(
                question="What's the universal answer ?",
                answer="It's 42 !",
        )

        # Flashcard is created with correct question and answer
        self.assertIsInstance(flashcard, Flashcard)
        self.assertEqual(flashcard.question, "What's the universal answer ?")
        self.assertEqual(flashcard.answer, "It's 42 !")

        # Defaults values are correctly sets
        self.assertEqual(flashcard.repetitions, 0)
        self.assertEqual(flashcard.easiness_factor, 2.5)
        self.assertEqual(flashcard.interval, timedelta(days=1))
