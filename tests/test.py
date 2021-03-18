import unittest

from cert import Certificate


pfx_file = "./pfx-files/test_file.pfx"
pfx_file_not_found = "pfx_file_not_found.pfx"
password_ok = b"123456"
password_fail = b"123"


class test_certificado(unittest.TestCase):

    def test_pfx_file_not_found(self):
        _cert = Certificate(
            pfx_file=pfx_file_not_found,
            password=password_ok
        )

        with self.assertRaises(FileNotFoundError):
            _cert.read_pfx_file()

    def test_pfx_senha_invalida(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_fail
        )

        with self.assertRaises(Exception):
            _cert.read_pfx_file()

    def test_subject(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.subject()), "<Name(CN={59F1E461-DDE5-4D2F-A01A-83322A9EB838})>")

    def test_not_valid_before(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_before()), "2015-06-15 05:47:57")

    def test_not_valid_after(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_after()), "2016-06-14 11:47:57")

    def test_serial_number(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.serial_number()), "166837181492823025495081207388598775252")

    def test_issuer(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.issuer()), "<Name(CN={59F1E461-DDE5-4D2F-A01A-83322A9EB838})>")
