
# Is This Link Safe? Link Safety Checker

This Python repository provides a simple utility to check the safety of a given URL. The script validates the URL format, checks for a valid SSL certificate, and verifies that the domain is not included in a list of known malicious websites.

## Features

- **URL Validation**: Ensures the given URL follows a proper format.
- **Malicious Domain Detection**: Checks if the domain is present in a predefined list of malicious websites.
- **SSL Certificate Check**: Verifies if the website has a valid SSL certificate for secure communication.

## How It Works

1. **Validate URL**: 
   The `is_valid_url(url)` function checks if the given URL follows a proper URL structure.

2. **Check Malicious Domain**: 
   The script checks the URL’s domain against a list of known malicious domains (`MALICIOUS_DOMAINS`).

3. **SSL Check**: 
   The `check_ssl(url)` function verifies if the website has a valid SSL certificate by attempting to establish a secure connection to the server.

4. **Summary**: 
   The `check_link_safety(url)` function combines the above checks and returns the overall safety status of the URL.

## Installation

Clone the repository:

\`\`\`bash
git clone https://github.com/your-repo/link-safety-checker.git
cd link-safety-checker
\`\`\`

Install the required libraries (if not already installed):

\`\`\`bash
pip install urllib3
\`\`\`

## Usage

\`\`\`python
from link_checker import check_link_safety

url = 'https://example.com'
is_safe, message, results = check_link_safety(url)

if is_safe:
    print(f"The URL is safe: {message}")
else:
    print(f"URL check failed: {message}")
print(results)
\`\`\`

### Example

\`\`\`python
url = 'https://evil.com'
is_safe, message, results = check_link_safety(url)
# Output: False, "Domain is in the list of known malicious websites"
\`\`\`

## Malicious Domains

The script currently checks against these domains:
- `evil.com`
- `malware.com`
- `phishing.net`

You can modify the `MALICIOUS_DOMAINS` list to include more domains.

## Related Projects

Check out these related projects:
- [Website SEO Scanner](https://www.website-seo-scanner.com/)
- [Keyword Converter](https://www.mix-convert-keyword.com/)
- [Is This Link Safe](https://www.isthislinksafe.net/)

## License

This project is licensed under the MIT License.
