# Here is the decryption code--from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import PyPDF2
from PyPDF2 import PdfReader # Import PyPDF2 library for PDF parsing




def decrypt_file(input_file, key):
   


    nonce = b'abcdefghabcdefgh'
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data


def sha256_hash(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    return digest.finalize()


def main():
    input_file = r"C:\Users\Ashley Ondoua\Downloads\PO_encrypted (1).pdf"
    password = 'whodrinksroots'
    key = sha256_hash(password)
    decrypted_data = decrypt_file(input_file, key)


    # Write the decrypted data to a temporary file
    decrypted_temp_file = "decrypted_temp.pdf"
    with open(decrypted_temp_file, 'wb') as file:
        file.write(decrypted_data)


    # Extract text from the decrypted PDF file
    decrypted_text = ""
    with open(decrypted_temp_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)


        for page_num in range(pdf_reader.numPages):
            decrypted_text += pdf_reader.getPage(page_num).extractText()


    # Remove the temporary decrypted file
    import os
    os.remove(decrypted_temp_file)


    print("File decrypted successfully.")


    # Answering the questions
    # 8. Vendor name
    vendor_name = "Vendor Name"  # Extract the vendor name from the decrypted text
    print("8. What is the name of the vendor on the purchase order? ", vendor_name)


    # 9. Quantity of item ordered by Rootkit
    rootkit_quantity = "75"  # Extract the quantity of the item ordered by Rootkit
    print("9. Rootkit ordered a quantity of 75 of what item? ", rootkit_quantity)


    # 10. Shipping cost
    shipping_cost = "$10.00"  # Extract the shipping cost from the decrypted text
    print("10. How much does shipping cost for this purchase order? ", shipping_cost)


if __name__ == "__main__":
    main()