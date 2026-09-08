# CODTECH-Task1: Advanced Multi-Threaded Port Scanner

## 📌 Project Overview
This project is an **Advanced Port Scanner** built using Python during my internship at **CodTech IT Solutions**. The tool is designed to scan a specific target IP address or domain to identify open TCP ports within the standard range (1-1024). 

By leveraging **Multi-threading** via Python's `concurrent.futures` module, the execution speed is significantly optimized, scaling down scan times from several minutes to just a few seconds.

---

## 👤 Intern Information
* **Name:** [Avni Goyal]
* **Intern ID:** [CITS9080]
* **Domain:** Cyber Security & Ethical Hacking / Python Development
* **Duration:** [September 8, 2026 - October 8, 2026]
* **Mentor:** CodTech IT Solutions Evaluation Team

---

## ⚙️ Features
* **Multi-Threaded Execution:** Utilizes a pool of 100 parallel threads to process scans concurrently.
* **DNS Resolution:** Automatically converts domain names (e.g., `google.com`) into accurate target IPv4 addresses.
* **Exception Handling:** Gracefully handles invalid hostnames and network connection timeouts.
* **Clean Visual Feedback:** Displays structured output showcasing open ports directly in the console.

---

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Core Modules:** `socket` (Network Connections), `concurrent.futures` (Multi-threading), `sys` & `datetime` (System metrics).

---

## 🚀 How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com[YourGitHubUsername]/[YourRepositoryName].git
   cd [YourRepositoryName]
   ```

2. **Execute the Script:**
   ```bash
   python port_scanner.py
   ```

3. **Input Target:**
   When prompted, enter your target IP or type `localhost` to test your local network.

---

## 🔍 Sample Output Screenshot / Demonstration
*(Tip: Once you take a screenshot of your terminal working, you can drag and drop the image here to display it on your GitHub page!)*
