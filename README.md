# domainRecon-subdomain recon automation tool

DomainRecon is a powerful automation tool for subdomain enumeration and checking subdomain activity. It leverages popular tools such as Amass, Subfinder, Sublist3r, Knockpy, and Httprobe to streamline the process of bug hunting and reconnaissance.

## Prerequisites

Before using this tool, make sure you have the following prerequisites installed on your Kali Linux system:

- **Git**: Git is required for cloning the repository. If you don't have Git installed, you can install it by running the following command:

   ```bash
   sudo apt update
   sudo apt install git

- **go**:  Go is required to build and install some of the tools used by DomainRecon. You can install Go by following these steps:

    ```bash
    wget https://golang.org/dl/go<version>.linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf go<version>.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    source ~/.bashrc

- **Python**: Python is required to run the DomainRecon script. Kali Linux usually comes with Python pre-installed. You can check the installed version by 
    running  "python --version". If Python is not installed, you can install it by running:
    
    ```bash
    sudo apt update
    sudo apt install python3

- **Pip**: Pip is the package installer for Python. It is required to install Python dependencies. You can install Pip by running the following command:

    ```bash
    sudo apt update
    sudo apt install python3-pip

 ## Installation
  
 ### To install and set up DomainRecon on Kali Linux, follow the steps below:
  - **Clone the repository:**
    ```bash
    git clone https://github.com/muhsinbinirshad/domainRecon
- **Navigate to the cloned repository:**
    ```bash
    cd domainRecon
- ** Set Execute Permission  **
   ```bash 
    chmod +x install-tools.py
- **Run the installation script to install all the tools:**
    ```bash
    python3 install-tools.py

- **The script will automatically install the required tools (Amass, Subfinder, Sublist3r, Knockpy, and Httprobe). Follow any prompts or instructions during the installation proces
## Usage
### To use DomainRecon for subdomain enumeration and activity checking, follow the steps below

   - **set Execute Permission**
     ```bash
     chmod +x domainRecon.py
   - **to run**  
     ```bash 
     python3 domainRecon.py

 - **Enter the target domain when prompted.**
 - **The script will utilize the installed tools to find subdomains and check their activity.**
 - **The results will be stored in two separate text files: one for all subdomains and another for active subdomains.**


