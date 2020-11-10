import unittest
import regex


class TestRegex(unittest.TestCase):

    def test_char_regex(self):
        self.assertTrue(regex.char_regex('a', 'a'))
        self.assertTrue(regex.char_regex('.', 'a'))
        self.assertTrue(regex.char_regex('', 'a'))
        self.assertTrue(regex.char_regex('', ''))
        self.assertFalse(regex.char_regex('a', ''))

    def test_string_regex(self):
        self.assertTrue(regex.string_regex('apple', 'apple'))
        self.assertTrue(regex.string_regex('.pple', 'apple'))
        self.assertTrue(regex.string_regex('appl.', 'apple'))
        self.assertTrue(regex.string_regex('.....', 'apple'))
        self.assertFalse(regex.string_regex('peach', 'apple'))

    def test_partial_regex(self):
        self.assertTrue(regex.partial_regex('apple', 'apple'))
        self.assertTrue(regex.partial_regex('ap', 'apple'))
        self.assertTrue(regex.partial_regex('le', 'apple'))
        self.assertTrue(regex.partial_regex('a', 'apple'))
        self.assertTrue(regex.partial_regex('.', 'apple'))
        self.assertFalse(regex.partial_regex('apwle', 'apple'))
        self.assertFalse(regex.partial_regex('peach', 'apple'))

    def test_extended_regex(self):
        self.assertTrue(regex.extended_regex('^app', 'apple'))
        self.assertTrue(regex.extended_regex('le$', 'apple'))
        self.assertTrue(regex.extended_regex('^a', 'apple'))
        self.assertTrue(regex.extended_regex('.$', 'apple'))
        self.assertTrue(regex.extended_regex('apple$', 'tasty apple'))
        self.assertTrue(regex.extended_regex('^apple', 'apple pie'))
        self.assertTrue(regex.extended_regex('^apple$', 'apple'))
        self.assertFalse(regex.extended_regex('^apple$', 'tasty apple'))
        self.assertFalse(regex.extended_regex('^apple$', 'apple pie'))
        self.assertFalse(regex.extended_regex('app$', 'apple'))
        self.assertFalse(regex.extended_regex('^le', 'apple'))
        self.assertTrue(regex.extended_regex('colou?r', 'color'))
        self.assertTrue(regex.extended_regex('colou?r', 'colour'))
        self.assertFalse(regex.extended_regex('colou?r', 'colouur'))
        self.assertTrue(regex.extended_regex('colou*r', 'color'))
        self.assertTrue(regex.extended_regex('colou*r', 'colour'))
        self.assertTrue(regex.extended_regex('colou*r', 'colouur'))
        self.assertTrue(regex.extended_regex('col.*r', 'color'))
        self.assertTrue(regex.extended_regex('col.*r', 'colour'))
        self.assertTrue(regex.extended_regex('col.*r', 'colr'))
        self.assertTrue(regex.extended_regex('col.*r', 'collar'))
        self.assertFalse(regex.extended_regex('col.*r$', 'colors'))

    def test_extended_regex_question(self):
        self.assertTrue(regex.extended_regex('colou?r', 'color'))
        self.assertTrue(regex.extended_regex('colou?r', 'colour'))
        self.assertFalse(regex.extended_regex('colou?r', 'colouur'))
        self.assertTrue(regex.extended_regex('.?.?l+.?.?', 'clr'))

    def test_extended_regex_asterisk(self):
        self.assertTrue(regex.extended_regex('^co*lo.*r$', 'colouur'))
        self.assertTrue(regex.extended_regex('^colo.*r$', 'colouur'))
        self.assertFalse(regex.extended_regex('col.*r$', 'colors'))
        self.assertFalse(regex.extended_regex('^col.*r$', 'colors'))
        self.assertTrue(regex.extended_regex('colou*r', 'color'))
        self.assertTrue(regex.extended_regex('colou*r', 'colour'))
        self.assertTrue(regex.extended_regex('colou*r', 'colouur'))

    def test_extended_regex_one_or_more(self):
        self.assertTrue(regex.extended_regex('^co+lo.+r$', 'colouur'))
        self.assertTrue(regex.extended_regex('^colo.+r$', 'colouur'))
        self.assertFalse(regex.extended_regex('col.+r$', 'colors'))
        self.assertFalse(regex.extended_regex('^col.+r$', 'colors'))
        self.assertFalse(regex.extended_regex('colou+r', 'color'))
        self.assertTrue(regex.extended_regex('co*lou+r', 'colour'))
        self.assertTrue(regex.extended_regex('c.*lou+r', 'colouur'))

    def test_extended_regex_metacharacters(self):
        self.assertTrue(regex.extended_regex('\\.$', 'end.'))
        self.assertTrue(regex.extended_regex('3\\+3', '3+3=6'))
        self.assertTrue(regex.extended_regex('\\?', 'Is this working?'))
        self.assertTrue(regex.extended_regex('\\\\', '\\'))
        self.assertFalse(regex.extended_regex('colou\?r', 'color'))
        self.assertFalse(regex.extended_regex('colou\?r', 'colour'))
