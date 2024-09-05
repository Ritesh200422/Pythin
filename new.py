import re

def validate_usn(usn):
    pattern = re.compile(r'^[1-4][A-Z]{2}\d{2}[A-Z]{2}\d{3}$')

    if pattern.match(usn):
        print(f"The USN '{usn}' is valid.")
    else:
        print(f"The USN '{usn}' is not valid. Please check the format.")

# Example usage:
usn_to_validate = input("Enter the UG VTU student USN: ")
validate_usn(usn_to_validate)
