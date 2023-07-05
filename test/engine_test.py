from Engine.EngineTypes.CapuletEngine import CapuletEngine
from Engine.EngineTypes.SternmanEngine import SternmanEngine
from Engine.EngineTypes.WilloughbyEngine import WilloughbyEngine

import unittest

class EngineTestCase(unittest.TestCase):
    def test_willoughby_engine_needs_service(self):
        current_mileage = 70000
        last_service_mileage = 5000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_does_not_need_service(self):
        current_mileage = 55000
        last_service_mileage = 50000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())

    def test_sternman_engine_needs_service(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())

    def test_capulet_engine_needs_service(self):
        current_mileage = 35000
        last_service_mileage = 15000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        current_mileage = 28000
        last_service_mileage = 25000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())