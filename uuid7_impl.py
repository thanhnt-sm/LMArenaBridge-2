import time
import random
import secrets

def uuid7():
    """
    Generate a UUIDv7 using Unix epoch (milliseconds since 1970-01-01)
    matching the browser's implementation.
    """
    # Get current timestamp in milliseconds (48 bits)
    timestamp_ms = int(time.time() * 1000)
    
    # Generate random bits
    rand_a = secrets.randbits(12)  # 12 bits for sub-millisecond precision
    rand_b = secrets.randbits(62)  # 62 bits of randomness (2 bits used for variant)
    
    # Build the UUID according to UUIDv7 spec
    # Timestamp (48 bits) + version (4 bits) + rand_a (12 bits) + variant (2 bits) + rand_b (62 bits)
    
    # First 6 bytes: timestamp
    uuid_int = timestamp_ms << 80
    
    # Next 2 bytes: version (0111 = 7) + rand_a (12 bits)
    uuid_int |= (0x7000 | rand_a) << 64
    
    # Last 8 bytes: variant (10) + rand_b (62 bits)
    uuid_int |= (0x8000000000000000 | rand_b)
    
    # Convert to hex string with dashes
    hex_str = f"{uuid_int:032x}"
    return f"{hex_str[0:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:32]}"

# Test it
if __name__ == "__main__":
    test_uuid = uuid7()
    print(f"Generated UUID: {test_uuid}")
    
    # Verify timestamp
    uuid_hex = test_uuid.replace('-', '')
    timestamp_hex = uuid_hex[:12]
    timestamp_ms = int(timestamp_hex, 16)
    
    from datetime import datetime
    print(f"Timestamp: {datetime.fromtimestamp(timestamp_ms / 1000)}")
    print(f"Current time: {datetime.now()}")
    
    # Generate multiple to show they're sequential
    print("\nGenerating 5 UUIDs in sequence:")
    for i in range(5):
        print(uuid7())
