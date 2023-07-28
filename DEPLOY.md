## Deploy to server
```
sudo apt update && sudo apt upgrade
sudo apt install -y pkg-config
cd ~
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzvf Python-3.11.1.tgz
cd Python-3.11.1
./configure --enable-optimizations --prefix=~/.python3.11
sudo make altinstall
```

Install last Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Clone repo into `~/visitor-observer`:
```
mkdir -p ~/visitor-observer/
cd ~/visitor-observer
git clone https://github.com/yastcher/visitors-observer.git
```

Install dependencies:
```
poetry install
```
