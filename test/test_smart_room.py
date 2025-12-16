import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_true(self, infrared_sensor: Mock):
        self.infrared_sensor = False
        infrared_sensor.return_value = True
        room = SmartRoom()
        outcome = room.check_room_occupancy()
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_false(self, infrared_sensor: Mock):
        self.infrared_sensor = True
        infrared_sensor.return_value = False
        room = SmartRoom()
        outcome = room.check_room_occupancy()
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_false(self, infrared_sensor: Mock):
        self.infrared_sensor = True
        infrared_sensor.return_value = False
        room = SmartRoom()
        outcome = room.check_room_occupancy()
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_enough_light(self, photoresistor: Mock):
        self.photoresistor = False
        photoresistor.return_value = True
        room = SmartRoom()
        outcome = room.check_enough_light()
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_not_check_enough_light(self, photoresistor: Mock):
        self.photoresistor = True
        photoresistor.return_value = False
        room = SmartRoom()
        outcome = room.check_enough_light()
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    @patch.object(GPIO, "input")
    @patch.object(GPIO, "output")
    def test_light_management_person_inside_and_lightbulb_on(self,lightbulb: Mock, photoresistor: Mock, infrared_sensor: Mock):
        photoresistor.return_value = False
        infrared_sensor.return_value = True
        room = SmartRoom()
        room.light_on = False
        room.manage_light_level()
        self.assertTrue(room.light_on)
        lightbulb.assert_called_once_with(room.LED_PIN, True)
