# domain_checker
🚀 Project Overview
The Domain Checker is a cybersecurity tool that analyzes and verifies a domain's authenticity to detect potential threats. It helps determine whether a domain is safe, suspicious, or potentially used for phishing by checking:

✅ Domain existence & validity (DNS & WHOIS records)
✅ Mail Exchange (MX) records (Is the domain capable of sending emails?)
✅ Domain registration age (Newly registered domains are riskier)
✅ Disposable or temporary email domains (Often used for fraud)
✅ Blacklist check (Is the domain flagged as malicious?)

🛠 How It Works (Step-by-Step Guide)
Step 1: User Inputs a URL
📌 The user enters a URL (e.g., https://secure-login-example.com).

Step 2: Extract the Domain Name
🔍 The code extracts only the domain part of the URL using urlparse().

Example:
🔹 Input URL: https://secure-login-example.com/page?user=123
🔹 Extracted domain: secure-login-example.com

Step 3: Check for Suspicious Keywords
⚠️ The program checks if the domain name contains common phishing-related words:

"login-" → Often used in fake login pages.
"secure-" → Attackers use it to pretend the site is secure.
"account-" → Phishing sites trick users into entering account credentials.
"verify-" → Fake email or identity verification pages.
"update-" → Used in fraudulent security updates.
Step 4: Detect Suspicious Domains
✅ If any of these patterns appear in the domain, the URL is flagged as suspicious.
✅ Otherwise, it is considered safe.
