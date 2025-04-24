name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""

with open("contact.vcf", "w") as file:
    file.write(vcard)
