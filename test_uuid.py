import time
from uuid_extensions import uuid7
from datetime import datetime

# Generate a UUID
test_uuid = uuid7()
print(f"Generated UUID: {test_uuid}")

# Extract timestamp from UUID (first 48 bits)
uuid_hex = str(test_uuid).replace('-', '')
timestamp_hex = uuid_hex[:12]  # First 12 hex chars = 48 bits
timestamp_ms = int(timestamp_hex, 16)

print(f"Timestamp hex: {timestamp_hex}")
print(f"Timestamp ms: {timestamp_ms}")

# Current time in ms since Unix epoch
current_unix_ms = int(time.time() * 1000)
print(f"Current Unix ms: {current_unix_ms}")

# Check if it's Gregorian epoch (1582-10-15)
gregorian_to_unix_offset = 12219292800000  # ms between 1582 and 1970
adjusted_timestamp = timestamp_ms - gregorian_to_unix_offset
print(f"Adjusted timestamp (if Gregorian): {adjusted_timestamp}")
print(f"Difference from current: {adjusted_timestamp - current_unix_ms} ms")

# Convert to datetime
try:
    dt = datetime.fromtimestamp(timestamp_ms / 1000)
    print(f"As datetime (Unix): {dt}")
except:
    print("Can't convert as Unix timestamp")

try:
    dt_adjusted = datetime.fromtimestamp(adjusted_timestamp / 1000)
    print(f"As datetime (Gregorian adjusted): {dt_adjusted}")
except:
    print("Can't convert as Gregorian timestamp")

# Compare with browser UUID
browser_uuid = "019a4d97-52ec-7ca8-9283-f3bfe5b3c32e"
browser_hex = browser_uuid.replace('-', '')[:12]
browser_timestamp_ms = int(browser_hex, 16)
print(f"\nBrowser UUID timestamp hex: {browser_hex}")
print(f"Browser timestamp ms: {browser_timestamp_ms}")
print(f"Browser as datetime: {datetime.fromtimestamp(browser_timestamp_ms / 1000)}")
