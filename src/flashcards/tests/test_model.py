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

    def test_correct_answer(self):
        """
        Flashcards can be updated using user feedback.
        """

        grade = 4
        flashcard = Flashcard(
                question="What's the universal answer ?",
                answer="It's 42 !",
        )

        # Feedback is from 1-5 if over 3 => success
        flashcard.update(grade)

        # Test consequences
        self.assertEqual(flashcard.repetitions, 1)
        self.assertGreaterEqual(flashcard.easiness_factor, 1.3)
        self.assertEqual(flashcard.interval.days, 1)

        flashcard.update(grade) # Second update

        # Test consequences
        self.assertEqual(flashcard.repetitions, 2)
        self.assertGreaterEqual(flashcard.easiness_factor, 1.3)
        self.assertEqual(flashcard.interval.days, 6)

        # Computes next interval 
        interval = flashcard.easiness_factor * flashcard.interval

        flashcard.update(grade) # Third update

        # Test consequences
        self.assertEqual(flashcard.repetitions, 3)
        self.assertGreaterEqual(flashcard.easiness_factor, 1.3)
        self.assertEqual(flashcard.interval, interval)

    def test_wrong_answer(self):
        """
        Flashcards can be updated using user feedback.
        """

        grade = 2
        flashcard = Flashcard(
                question="What's the universal answer ?",
                answer="It's 42 !",
        )

        # Feedback is from 1-5 if under 3 => failure
        flashcard.update(grade)

        # Test consequences
        self.assertEqual(flashcard.repetitions, 0)
        self.assertGreaterEqual(flashcard.easiness_factor, 1.3)
        self.assertEqual(flashcard.interval.days, 1)

