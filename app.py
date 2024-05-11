from flask import Flask
from flask import render_template_string
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)

def get_certificate_info(cert_file):
    with open(cert_file, 'rb') as f:
        cert_data = f.read()
    
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    not_before = cert.not_valid_before_utc
    not_after = cert.not_valid_after_utc

    return not_before, not_after

def get_kube_certificates():
    cert_dir = '/etc/kubernetes/pki'
    cert_files = {}
    for root, dirs, files in os.walk(cert_dir):
        for file in files:
            if file.endswith(".crt"):  # Sadece .crt uzantılı dosyaları al
                cert_files[file] = os.path.join(root, file)
    return cert_files

@app.route('/')
def index():
    certificates = get_kube_certificates()
    output = ""
    for cert_name, cert_file in certificates.items():
        not_before, not_after = get_certificate_info(cert_file)
        output += f"{cert_name}:\n"
        output += f"{' '*35}Not Before: {not_before}\n"
        output += f"{' '*35}Not After   : {not_after}\n\n"
    return render_template_string("<pre>{{ output }}</pre>", output=output)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
