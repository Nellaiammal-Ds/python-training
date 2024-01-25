from datetime import datetime

# String representing a date
date_string = "2022-01-11"

# Convert string to date
date_object = datetime.strptime(date_string, "%Y-%m-%d")

print("String to Date:")
print("Original String:", date_string)
print("Converted Date:", date_object)

from datetime import datetime

# Date object
date_object = datetime.now()

# Convert date to string
date_string = date_object.strftime("%Y-%m-%d")

print("\nDate to String:")
print("Original Date:", date_object)
print("Converted String:", date_string)
