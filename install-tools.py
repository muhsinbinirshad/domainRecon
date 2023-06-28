import os

tools = [
    ("subfinder", "GO111MODULE=on go get -u github.com/projectdiscovery/subfinder/v2/cmd/subfinder"),
    ("amass", "GO111MODULE=on go get -v github.com/OWASP/Amass/v3/..."),
    ("sublist3r", "git clone https://github.com/aboul3la/Sublist3r.git && cd Sublist3r && pip install -r requirements.txt"),
    ("httprobe", "go get -u github.com/tomnomnom/httprobe"),
    ("knockpy", "git clone https://github.com/guelfoweb/knock.git && cd knock && python setup.py install")
]

for tool, command in tools:
    print(f"Installing {tool}...")
    if os.system(f"sudo {command}") == 0:
        print(f"{tool} installed successfully!")
    else:
        print(f"Failed to install {tool}.")

print("All tools installed successfully!")
