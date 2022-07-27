import unittest

from digital_certificate.cert import Certificate

pfx_file = "./tests/files/cert.pfx"
pfx_file_not_found = "pfx_file_not_found.pfx"
password_ok = b"root"
password_fail = b"123"

p12_file = "./tests/files/cert.p12"
p12_file_not_found = "p12_file_not_found.p12"
password_ok = b"root"
password_fail = b"123"


class test_certificado_p12(unittest.TestCase):

    def test_p12_file_not_found(self):
        _cert = Certificate(
            pfx_file=p12_file_not_found,
            password=password_ok
        )

        with self.assertRaises(FileNotFoundError):
            _cert.read_pfx_file()

    def test_p12_file_binary(self):
        with open(p12_file, "rb") as file:
            p12_binary = file.read()

        _cert = Certificate(
            pfx_file=p12_binary,
            password=password_ok
        )
        _cert.read_pfx_file()

    def test_p12_file_binary_invalid(self):
        with open(p12_file, "rb") as file:
            p12_binary = file.read()
        p12_binary = p12_binary[:-100]
        _cert = Certificate(
            pfx_file=p12_binary,
            password=password_ok
        )
        with self.assertRaises(Exception):
            _cert.read_pfx_file()

    def test_p12_senha_invalida(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_fail
        )

        with self.assertRaises(Exception):
            _cert.read_pfx_file()

    def test_p12_subject(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.subject()), "<Name(CN=myRSAdemoserver)>")

    def test_p12_not_valid_before(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_before()), "2022-01-25 15:20:15")

    def test_p12_not_valid_after(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_after()), "2024-10-20 15:20:15")

    def test_p12_serial_number(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.serial_number()), "128805826665071774012132547883470073087342988157")

    def test_p12_issuer(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.issuer()), "<Name(CN=myRSAdemoserver)>")

    def test_p12_common_name(self):
        _cert = Certificate(
            pfx_file=p12_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.common_name()), "myRSAdemoserver")


class test_certificado_pfx(unittest.TestCase):

    def test_pfx_file_not_found(self):
        _cert = Certificate(
            pfx_file=pfx_file_not_found,
            password=password_ok
        )

        with self.assertRaises(FileNotFoundError):
            _cert.read_pfx_file()

    def test_pfx_file_binary(self):
        with open(pfx_file, "rb") as file:
            pfx_binary = file.read()

        _cert = Certificate(
            pfx_file=pfx_binary,
            password=password_ok
        )
        _cert.read_pfx_file()

    def test_pfx_file_binary_invalid(self):
        with open(pfx_file, "rb") as file:
            pfx_binary = file.read()

        pfx_binary = pfx_binary[:-100]
        _cert = Certificate(
            pfx_file=pfx_binary,
            password=password_ok
        )
        with self.assertRaises(Exception):
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
        self.assertEqual(str(_cert.subject()), "<Name(CN=myRSAdemoserver)>")

    def test_not_valid_before(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_before()), "2022-01-25 15:20:15")

    def test_not_valid_after(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.not_valid_after()), "2024-10-20 15:20:15")

    def test_serial_number(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.serial_number()), "128805826665071774012132547883470073087342988157")

    def test_issuer(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.issuer()), "<Name(CN=myRSAdemoserver)>")

    def test_common_name(self):
        _cert = Certificate(
            pfx_file=pfx_file,
            password=password_ok
        )
        _cert.read_pfx_file()
        self.assertEqual(str(_cert.common_name()), "myRSAdemoserver")
