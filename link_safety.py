import re
from urllib.parse import urlparse
import ssl
import socket

MALICIOUS_DOMAINS = ['evil.com', 'malware.com', 'phishing.net']

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def check_ssl(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cert = secure_sock.getpeercert()
        return True
    except:
        return False

def check_link_safety(url):
    results = {
        'valid_url': False,
        'not_malicious': False,
        'has_ssl': False
    }
    
    # Check URL validity
    results['valid_url'] = is_valid_url(url)
    if not results['valid_url']:
        return False, "Invalid URL format", results

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Check against malicious domains
    results['not_malicious'] = domain not in MALICIOUS_DOMAINS
    if not results['not_malicious']:
        return False, "Domain is in the list of known malicious websites", results

    # Check SSL certificate
    results['has_ssl'] = check_ssl(url)
    if not results['has_ssl']:
        return False, "Invalid or missing SSL certificate", results

    return True, "The link appears to be safe", results
