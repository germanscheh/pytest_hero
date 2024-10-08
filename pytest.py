import unittest

class TestGetHighestSuperhero(unittest.TestCase):
    def test_male_with_job(self):
        highest_superhero = get_highest_superhero('Male', True)
        self.assertIsNotNone(highest_superhero)
        self.assertEqual(highest_superhero['appearance']['gender'], 'Male')
        self.assertIn('work', highest_superhero)
        self.assertNotEqual(highest_superhero['work']['occupation'], '')

    def test_female_without_job(self):
        highest_superhero = get_highest_superhero('Female', False)
        self.assertIsNotNone(highest_superhero)
        self.assertEqual(highest_superhero['appearance']['gender'], 'Female')
        self.assertNotIn('work', highest_superhero) or highest_superhero['work']['occupation'] == ''

    def test_no_superheroes_found(self):
        highest_superhero = get_highest_superhero('Other', True)
        self.assertIsNone(highest_superhero)