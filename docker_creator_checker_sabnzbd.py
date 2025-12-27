import os

def detect_provider():
    # Define checks: (file_path, search_string, return_value)
    checks = [
        ("/build_version", "linuxserver", "linuxserver"),
        ("/bin/init.sh", "binhex", "binhex"),
        ("/etc/passwd", "hotio", "hotio")
    ]

    for path, search_str, result in checks:
        if os.path.isfile(path):
            try:
                with open(path, 'r', errors='ignore') as f:
                    # Case-insensitive check
                    if search_str.lower() in f.read().lower():
                        return result
            except (PermissionError, OSError):
                # Skip if file can't be accessed
                continue

    return "unknown"  # Return a fallback value if no matches are found

# Execution
provider = detect_provider()
print(f"Detected: {provider}")
