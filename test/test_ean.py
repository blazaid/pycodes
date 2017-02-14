from unittest import TestCase

from pycodes.ean import Ean13
from pycodes.exceptions import EmptyCode, CharacterNotAllowed, BadCodeLength, \
    WrongChecksum


class Ean13TestCase(TestCase):
    def setUp(self):
        self.valid_codes = (
            '0000000000000',
            '1111111111116',
            '2222222222222',
            '3333333333338',
            '4444444444444',
            '5555555555550',
            '6666666666666',
            '7777777777772',
            '8888888888888',
            '9999999999994',
        )

    def test_null_or_empty_code_raises_error(self):
        """ Checks if it's pickeable by writing it into a temporary file. """
        for code in (None, ''):
            for checksum in (True, False):
                with self.assertRaises(EmptyCode):
                    Ean13(code, checksum)

    def test_at_least_one_no_digit_raises_error(self):
        no_digits = 'agz_¿?`.<´ñ*'
        for item in no_digits:
            for checksum in (True, False):
                for code in self.valid_codes:
                    for i in range(1, len(code)):
                        wrong_code = code[i:] + item + code[i + 1:]
                        with self.assertRaises(CharacterNotAllowed):
                            Ean13(wrong_code, checksum)

    def test_wrong_length_raises_error(self):
        # Smaller
        for i in range(1, 12):
            for checksum in (True, False):
                with self.assertRaises(BadCodeLength):
                    Ean13('0' * i, checksum)
        # Smaller when checksum is True
        with self.assertRaises(BadCodeLength):
            Ean13('0' * 12, True)
        # Greater when checksum is False
        with self.assertRaises(BadCodeLength):
            Ean13('0' * 13, False)
        # Greater
        for i in range(14, 100, 10):
            for checksum in (True, False):
                with self.assertRaises(BadCodeLength):
                    Ean13('0' * i, checksum)

    def test_wrong_checksum_raises_error(self):
        for valid_code in self.valid_codes:
            code_12, checksum = valid_code[:-1], valid_code[-1:]
            for i in range(10):
                if str(i) != checksum:
                    with self.assertRaises(WrongChecksum):
                        Ean13(code_12 + str(i))

    def test_checksums_are_computed_correctly(self):
        for valid_code in self.valid_codes:
            code_12, valid_checksum = valid_code[:-1], valid_code[-1:]
            computed_code = Ean13(code_12, checksum=False)
            self.assertEqual(str(computed_code), valid_code)

    def test_valid_codes_create_a_correct_object(self):
        for valid_code in self.valid_codes:
            computed_code = Ean13(valid_code)
            self.assertEqual(str(computed_code), valid_code)
