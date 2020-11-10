import unittest

class validate:

    def ValidPassword(self, passwd):
        """
        >>> password = validate()
        >>> password.ValidPassword("Abcdefgh123!")
        'True'
        >>> password.ValidPassword("12312Abdvfsd^")
        'True'
        >>> password.ValidPassword("Abcdefghjiklmn")
        'False'
        >>> password.ValidPassword("123!!!!!!!!!!!!!!!!aaaa")
        'False'
        >>> password.ValidPassword(15)
        Traceback (most recent call last):
            ...
        ValueError: Haslo nie jest stringiem
        >>> password.ValidPassword("Abc12!")
        Traceback (most recent call last):
            ...
        ValueError: Haslo jest za krotkie
        """

        if(type(passwd) != str):
            raise ValueError("Haslo nie jest stringiem")
        else:
            if (len(passwd) < 8):
                raise ValueError("Haslo jest za krotkie")
            else:
                specials = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
                up, special, number = False, False, False
                for char in passwd:
                    if char.isupper():
                        up = True
                    if char in specials:
                        special = True
                    if char.isnumeric():
                        number = True

                if(up and special and number):
                    return 'True'
                else:
                    return 'False'

class validateTest(unittest.TestCase):

    def setUp(self):
        self.temp = validate()

    def test_true_password_1(self):
        self.assertEqual("True", self.temp.ValidPassword("*abcdefhgjI123"))

    def test_true_password_2(self):
        self.assertEqual("True", self.temp.ValidPassword("Aaaaaaaaaaa*@&$*@&$99"))

    def test_false_password_1(self):
        self.assertEqual("False", self.temp.ValidPassword("Aaaaaaaaaaa*@&$*@&$"))

    def test_false_password_2(self):
        self.assertEqual("False", self.temp.ValidPassword("!!!!!!!!!!!!!!!!!!!!!1"))

    def test_too_short_1(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "sds")

    def test_too_short_2(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, "As1d%")

    def test_not_string_1(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, 1234)

    def test_not_string_2(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, False)

    def test_not_string_3(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, [{}])

    def test_not_string_4(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, None)

    def tearDown(self):
        self.temp = None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    unittest.main()
