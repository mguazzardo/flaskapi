curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
mv ./kubectl /usr/local/sbin
chmod +x /usr/local/sbin/kubectl
