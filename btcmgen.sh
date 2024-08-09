#!/usr/bin/env bash

# BTC-MGen: a tool where you can generate mnemonics and then check if they have BTC in it

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}[!] This script must be run as root${NC}" 
   exit 1
fi

if ! dpkg -l | grep -qw python3; then
    echo -e "${RED}[-] python3 is not installed. Installing python3...${NC}"
    apt install -y python3
fi

if ! dpkg -l | grep -qw figlet; then
    echo -e "${RED}[-] figlet is not installed. Installing figlet...${NC}"
    apt install -y figlet
fi

pip3 install requests bip32utils mnemonic --break-system-packages

clear

figlet "BTC-MGen"

echo -e "${GREEN}\n[01] Mnemonics generator\n[02] Address checker\n[00] Exit"

read -p "Enter your choice: " input

if [ "$input" -eq 1 ]; then
    clear
    figlet "MGen"
    python3 mgen.py
elif [ "$input" -eq 2 ]; then
    clear
    figlet "AddChkr"
    python3 checker.py
elif [ "$input" -eq 0 ]; then
    echo "${GREEN}Bye ツ${NC}"
    exit 0
else
    echo "${RED}Invalid choice, please enter 1, 2, or 0.${NC}"
fi
