import os
import shutil
import subprocess

# List of tools to install
tools = {
    'subfinder': 'github.com/projectdiscovery/subfinder',
    'amass': 'github.com/OWASP/Amass',
    'sublist3r': 'github.com/aboul3la/Sublist3r',
    'knockpy': 'github.com/guelfoweb/knock',
    'httprobe': 'github.com/tomnomnom/httprobe'
}

# Function to check if a tool is installed
def is_tool_installed(tool):
    return shutil.which(tool) is not None

# Function to install a tool using Go
def install_tool(tool, repository):
    if not is_tool_installed(tool):
        subprocess.call(['go', 'get', '-v', repository])

# Install required tools
for tool, repository in tools.items():
    install_tool(tool, repository)

# Function to find subdomains using multiple tools
def find_subdomains(domain):
    subdomains = set()

    # subfinder
    if is_tool_installed('subfinder'):
        output = subprocess.check_output(['subfinder', '-d', domain])
        subdomains.update(output.decode().splitlines())

    # amass
    if is_tool_installed('amass'):
        output = subprocess.check_output(['amass', 'enum', '-d', domain])
        subdomains.update(output.decode().splitlines())

    # sublist3r
    if is_tool_installed('sublist3r'):
        output = subprocess.check_output(['sublist3r', '-d', domain])
        subdomains.update(output.decode().splitlines())

    # knockpy
    if is_tool_installed('knockpy'):
        output = subprocess.check_output(['knockpy', '-w', domain])
        subdomains.update(output.decode().splitlines())

    return subdomains

# Function to check subdomain activity using httprobe
def check_subdomain_activity(subdomains):
    active_subdomains = set()

    for subdomain in subdomains:
        response = subprocess.call(['httprobe', subdomain])
        if response == 0:
            active_subdomains.add(subdomain)

    return active_subdomains

# Function to write subdomains to a file
def write_subdomains_to_file(subdomains, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(subdomains))

# Main function
def main():
    domain = input("Enter the target domain: ")

    # Find subdomains
    subdomains = find_subdomains(domain)

    # Write non-filtered subdomains to a file
    filename = f"non-filtered-{domain}.txt"
    write_subdomains_to_file(subdomains, filename)
    print(f"Non-filtered subdomains saved to '{filename}'.")

    # Check subdomain activity
    active_subdomains = check_subdomain_activity(subdomains)

    # Write active subdomains to a file
    filename = f"active-{domain}.txt"
    write_subdomains_to_file(active_subdomains, filename)
    print(f"Active subdomains saved to '{filename}'.")

# Run the script
if __name__ == '__main__':
    main()
