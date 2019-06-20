#!/bin/sh
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
# <<<<<<< HEAD
sudo apt-get install python3.6 -y
# =======
sudo apt-get install python3.6 -y
# >>>>>>> b83d194... Installations for Windows and Linux (issue #3)+ updating README.md (issue #23)
