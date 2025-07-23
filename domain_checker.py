import re
import requests
from urllib.parse import urlparse

def is_suspicious_url(url):
    # Common phishing patterns
    suspicious_patterns = ["-", "login-", "secure-", "account-", "verify-", "update-"]

    # Extract domain
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Check for suspicious keywords
    for pattern in suspicious_patterns:
        if pattern in domain:
            return True

    return False


# Example Usage
if __name__ == "__main__":
    url = input("Enter URL to check: ")
    if is_suspicious_url(url):
        print("Warning: This URL looks suspicious!")
    else:
        print("URL seems safe.")
