import os
import unittest

from helpers import generate_private_key, generate_public_key, generate_root_CA, generate_CSR, sign_CSR, sign_payroll, \
    verify_CER, verify_payroll_signature


class MyTestCase(unittest.TestCase):
    def test_SecurityBankSystem(self):
        print(" A demo for building a security bank system")
        print("From team 5: Annafatia Golbazkhanipor,Shiyan Fu,Ashraf Rady")


#Part C: PKI  BEGIN
    def test_PKI_Generate_Private_key_step1(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_private_key('CyB@ter123','pki/','CApKey-T5.key')
        print(command )
        os.system(command);

    def test_PKI_Extract_Public_key_from_private_key_step2(name):
        # Use a breakpoint in the code line below to debug your script.
        command =generate_public_key('pki/CApKey-T5.key', 'pki/CApubKey-T5.key','CyB@ter123')
        print(command)
        os.system(command);

    def test_PKI_Create_root_CA_CERTIFICATE_step3(name):
        # Use a breakpoint in the code line below to debug your script.
        command =  generate_root_CA('pki/CApKey-T5.key','CyB@ter123','pki/CArootCert-T5.cer')
        print(command )
        os.system(command);

    def test_PKI_Sign_Client_CSR_step7(name):
        # Use a breakpoint in the code line below to debug your script.
        command = sign_CSR('pki/controller1-T5.csr', 'pki/CArootCert-T5.cer','pki/CApKey-T5.key', 'CyB@ter123','pki/myext1-T5.txt','pki/controller1-T5.cer')
        print(command)
        os.system(command);

    def test_PKI_Sign_Bank_CSR_step10(name):
        # Use a breakpoint in the code line below to debug your script.
        command = sign_CSR('pki/controller2-T5.csr', 'pki/CArootCert-T5.cer','pki/CApKey-T5.key', 'CyB@ter123','pki/myext2-T5.txt','pki/controller2-T5.cer')
        print(command)
        os.system(command);


    # Part C: PKI  END

# Part A: CLIENT BEGIN
    def test_CLIENT_Generate_Private_key_step4(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_private_key('CyB@ter123', 'client/', 'WCpKey-T5.key')
        print(command)
        os.system(command);

    def test_CLIENT_Extract_Public_key_from_private_key_step5(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_public_key('client/WCpKey-T5.key', 'client/WCpubKey-T5.key', 'CyB@ter123')
        print(command)
        os.system(command);
    def test_CLIENT_Generate_CSR_step6(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_CSR('client/WCpKey-T5.key', 'pki/controller1-T5.csr', 'CyB@ter123')
        print(command)
        os.system(command);
#################Go to step 7 on PKI#######################

    def test_CLIENT_Sign_Payroll_stepX(name):
        # Use a breakpoint in the code line below to debug your script.
        command = sign_payroll('client/WCpKey-T5.key', 'CyB@ter123','client/DigSigPayroll.bin','client/Payroll-T5.xlsx')
        print(command)
        os.system(command);
##############Step X: use www.csa.ca website to send payroll signed to Bank.###########################

# Part B: BANK BEGIN
    def test_BANK_Generate_Private_key__step7(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_private_key('CyB@ter123', 'bank/', 'WSpKey-T5.key')
        print(command)
        os.system(command);

    def test_BANK_Extract_Public_key_from_private_key_step8(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_public_key('bank/WSpKey-T5.key', 'bank/WSpubKey-T5.key', 'CyB@ter123')
        print(command)
        os.system(command);
    def test_BANK_Generate_CSR_step9(name):
        # Use a breakpoint in the code line below to debug your script.
        command = generate_CSR('bank/WSpKey-T5.key', 'pki/controller2-T5.csr', 'CyB@ter123')
        print(command)
        os.system(command);

#################Go to step 10 on PKI#######################

###########################Signature verifcation################################
    def test_client_Singed_CER(name):
        # Use a breakpoint in the code line below to debug your script.
        command = verify_CER('pki/CArootCert-T5.cer', 'client/controller1-T5.cer')
        print(command)
        os.system(command);

    def test_bank_Singed_CER(name):
        # Use a breakpoint in the code line below to debug your script.
        command = verify_CER('pki/CArootCert-T5.cer', 'bank/controller2-T5.cer')
        print(command)
        os.system(command);

    def test_payroll_Signature_verify(name):
        # Use a breakpoint in the code line below to debug your script.
        command = verify_payroll_signature('bank/WCpubKey-T5.key', 'bank/DigSigPayroll.bin', "bank/Payroll-T5.xlsx")
        print(command)
        os.system(command);

if __name__ == '__main__':
    unittest.main()
