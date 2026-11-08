import sys
import re
from pathlib import Path
from collections import Counter

if len(sys.argv) != 2:
    sys.exit("Usage: python3 parser.py <log_file>")

log_file = Path(sys.argv[1]).expanduser()
failed_attempts = 0
ip_counts = Counter()

try:
    with log_file.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            if "Failed password" in line:
                failed_attempts += 1

                match = re.search(
                    r"from (\d{1,3}(?:\.\d{1,3}){3}) port",
                    line
                )

                if match:
                    ip = match.group(1)
                    ip_counts[ip] += 1

except OSError as error:
    sys.exit(f"Error reading log file: {error}")

print(f"Total failed attempts: {failed_attempts}")

print("\nFailed attempts by IP:")
for ip, count in ip_counts.most_common():
    word = "attempt" if count == 1 else "attempts"
    print(f"{ip}: {count} {word}")
