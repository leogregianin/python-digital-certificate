from OpenSSL import crypto
from cryptography import x509
from cryptography.hazmat.backends import default_backend


class Certificate():
    def __init__(self, pfx_file, password, cert_content=None, cert=None):
        self.pfx_file = pfx_file
        self.password = password
        self.cert_content = cert_content
        self.cert = cert

    def read_pfx_file(self):
        try:
            with open(self.pfx_file, "rb") as cert_file:
                self.cert_content = cert_file.read()

            # Load pkcs12
            pkcs12 = crypto.load_pkcs12(
                self.cert_content,
                self.password
            )

            # PEM formatted private key
            key = crypto.dump_privatekey(
                crypto.FILETYPE_PEM,
                pkcs12.get_privatekey()
            )

            # PEM formatted certificate
            pem_data = crypto.dump_certificate(
                crypto.FILETYPE_PEM,
                pkcs12.get_certificate()
            )

            # Load pen_x509
            self.cert = x509.load_pem_x509_certificate(
                pem_data,
                default_backend()
            )

        except FileNotFoundError as err:
            raise FileNotFoundError(f"File not found. {err}")
        except Exception as err:
            raise Exception(f'Fail to open file. {err}')

    def not_valid_before(self):
        return self.cert.not_valid_before

    def not_valid_after(self):
        return self.cert.not_valid_after

    def subject(self):
        return self.cert.subject

    def serial_number(self):
        return self.cert.serial_number

    def issuer(self):
        return self.cert.issuer
