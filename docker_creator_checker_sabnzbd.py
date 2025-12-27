import os

def detect_docker_creator():
    # Define checks: (file_path, search_string, creator)
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
docker_creator = detect_docker_creator()
print(f"Detected: {docker_creator}")
