import requests
import sys

# Standard SQL Injection payloads to test forms
SQLI_PAYLOADS = [
    "'", 
    "\"", 
    "' OR '1'='1", 
    "\" OR \"1\"=\"1", 
    "' OR 1=1 --", 
    '" OR 1=1 --'
]

# Database error signatures that indicate vulnerability
DB_ERRORS = [
    "you have an error in your sql syntax",
    "unclosed quotation mark after the character string",
    "mysql_fetch_array",
    "oracle error",
    "postgreSQL query failed"
]

def check_sql_injection(url):
    """Tests a URL by appending common SQL injection payloads to it."""
    print(f"\n[*] Scanning target URL: {url}")
    print("[*] Testing web parameters for vulnerability...\n")
    
    is_vulnerable = False

    for payload in SQLI_PAYLOADS:
        # Append the payload to the URL (testing GET parameters)
        # Example: http://example.com'
        test_url = f"{url}{payload}"
        print(f"[~] Trying payload: {payload}")
        
        try:
            # Send a request to the modified URL
            response = requests.get(test_url, timeout=5)
            response_text = response.text.lower()
            
            # Check if any standard database error appears in the website source code
            for error in DB_ERRORS:
                if error in response_text:
                    print(f"\n[!] VULNERABILITY DETECTED! Target might be vulnerable to SQLi.")
                    print(f"[!] Found DB Error string: '{error}'")
                    print(f"[!] Vulnerable URL: {test_url}\n")
                    is_vulnerable = True
                    break
            
            if is_vulnerable:
                break
                
        except requests.exceptions.RequestException:
            print("[-] Error connecting to the server. Skipping payload.")
            break

    if not is_vulnerable:
        print("\n[+] Scan complete. No basic SQL Injection vulnerabilities found.")

def main():
    print("=" * 60)
    print("   CODTECH IT SOLUTIONS - SQL INJECTION VULNERABILITY SCANNER   ")
    print("=" * 60)
    
    target_url = input("Enter target URL with parameter (e.g., http://vulnweb.com): ").strip()
    
    if not target_url:
        print("[-] Error: URL cannot be empty.")
        sys.exit()
        
    check_sql_injection(target_url)

if __name__ == "__main__":
    main()
