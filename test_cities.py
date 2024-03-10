import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py"""
    santiago_chile = city_country('santiago', 'chile')
    sefl.assertEqual(santiago_chile, 'Santiago Chile')
    
unittest.main()