from typing import Union

from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID


class Certificate:
    def __init__(self, pfx_file: Union[str, bytes], password):
        self.pfx_file: Union[str, bytes] = pfx_file
        self.password = password
        self.cert_content = None
        self.cert = None
        self.private_key = None
        self.additional_certificates = None

    def read_pfx_file(self):
        try:
            if isinstance(self.pfx_file, str):
                with open(self.pfx_file, "rb") as cert_file:
                    self.cert_content = cert_file.read()
            elif isinstance(self.pfx_file, bytes):
                self.cert_content = self.pfx_file
            else:
                raise RuntimeError("pfx_file must be str or bytes")

            self.private_key, self.cert, self.additional_certificates = pkcs12.load_key_and_certificates(
                self.cert_content,
                self.password
            )

        except FileNotFoundError as err:
            raise FileNotFoundError(f"File not found. {err}")
        except Exception as err:
            raise Exception(f"Fail to open file. {err}")

    def not_valid_before(self):
        return self.cert.not_valid_before

    def not_valid_after(self):
        return self.cert.not_valid_after

    def subject(self):
        return self.cert.subject

    def common_name(self):
        return self.cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value

    def common_name(self):
        return self.cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value

    def common_name_split_issuer(self):
        """
        Issuer ou "Emitente"
        """
        try:
            cn = self.cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            return cn.split(':')[0]
        except BaseException:
            return ''

    def common_name_split_document(self):
        """
        Document or "CPF or CNPJ"
        """
        try:
            cn = self.cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            return cn.split(':')[1]
        except BaseException:
            return ''

    def serial_number(self):
        return self.cert.serial_number

    def issuer(self):
        return self.cert.issuer
