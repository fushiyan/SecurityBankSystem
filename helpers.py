def generate_private_key(password, path, outputkey):
    command = "Openssl genpkey -outform pem -algorithm rsa -pkeyopt rsa_keygen_bits:2048 -aes-128-cbc -pass pass:{0} -out {1}{2}".format(
        password,  path, outputkey)
    return command
def generate_public_key(inprivatekey, outputpublickey, passin):
    command = "openssl rsa -in {0} -pubout -out {1} -passin pass:{2}".format(inprivatekey, outputpublickey, passin)
    return command
def generate_root_CA(privatekey,passin,rootCA):
    command = "openssl req -new -x509 -outform pem -sha256 -set_serial 0x100 -key {0} -passin pass:{1} -days 365 -out {2} ".format(privatekey,passin,rootCA)
    return command
def generate_CSR(clientprivatekey,csr,passin):
    command = "openssl req -new -outform pem -key {0} -out {1} -passin pass:{2}".format(clientprivatekey,csr,passin)
    return command
def sign_CSR(csr, carootCer,caprivatekey, passin,exttext,output):
    command = "openssl x509 -req -in {0} -CA {1} -set_serial 0x200 -sha256 -CAkey {2} -passin pass:{3} -days 365 -extfile {4} -out {5}".format(csr, carootCer,caprivatekey, passin,exttext,output)
    return command
def sign_payroll(clientrivatekey, passin,payrollsign, payroll):
    command = "openssl dgst -sha256 -sign {0} -passin pass:{1} -out {2} {3}".format(clientrivatekey, passin,payrollsign, payroll)
    return command

def verify_CER(rootCA, usersignature):
    command = "openssl verify -verbose -attime 1645736400 -trusted {0} {1}".format(rootCA, usersignature)
    return command

def verify_payroll_signature(wcpubkey, payrollsig, payroll):
    command = "openssl dgst -sha256 -verify {0} -signature {1} {2}".format(wcpubkey, payrollsig, payroll)
    return command