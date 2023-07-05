from Battery.BatteryTypes.NubbinBattery import NubbinBattery
from Battery.BatteryTypes.SpindlerBattery import SpindlerBattery

import unittest
from datetime import date

class BatteryTestCase(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = date(2023, 7, 5)
        last_service_date = date(2019, 7, 5)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        current_date = date(2023, 7, 5)
        last_service_date = date(2022, 7, 5)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

    def test_spindler_battery_needs_service(self):
        current_date = date(2023, 7, 5)
        last_service_date = date(2018, 7, 5)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        current_date = date(2023, 7, 5)
        last_service_date = date(2022, 7, 5)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())