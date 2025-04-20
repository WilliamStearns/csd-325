#William Stearns
#4-20-25
#Module 7.2
#This file is for testing.

import unittest
from city_functions import city_function

class TestCityFunction(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_function("tokyo", "japan"), "Tokyo, Japan") 
    def test_city_country_pop(self):
        self.assertEqual(city_function("tokyo", "japan", 500), "Tokyo, Japan - population 500.")
    def test_city_country_language(self):
        self.assertEqual(city_function("washington d.c.", "united states", 678972, "English"), "Washington D.C., United States - population 678972, English.")

if __name__ == '__main__':
    unittest.main()
