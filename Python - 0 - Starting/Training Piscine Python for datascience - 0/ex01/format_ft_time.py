import time
from datetime import datetime

# Get current time in seconds since epoch
seconds_since_epoch = time.time()
# float

# Format with commas and scientific notation
formatted_seconds = f"{seconds_since_epoch:,.4f}"
scientific_notation = f"{seconds_since_epoch:.2e}"
# f-strings for string formatting
# {value:format_spec}
# {value:.2e} for scientific notation
# {value:,.4f} for float with commas and 4 decimal places


# Get current date in required format
# datetime.now() returns the current local date and time
# strftime formats the date as a string
current_date = datetime.now().strftime("%b %d %Y")
# string
# Print the formatted output
print(f"Seconds since January 1, 1970: {formatted_seconds} \
or {scientific_notation} in scientific notation")
print(current_date)
