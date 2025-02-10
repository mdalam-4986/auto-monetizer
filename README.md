# hybrid-miner
A hybrid cryptocurrency miner that uses a computer's CPU, GPU, Storage, and RAM.
!! **THIS CODE IS UNFINISHED - IT WILL NOT WORK PROPERLY AS OF NOW** !!

Setup:
Save the client.py file and run it. Ensure all libraries and dependants are installed correctly.
Installation is correct if it asks for admin permissions
Follow all steps that the script asks.

Step 1: Clone the Repository or Download the Script
Navigate to your GitHub repository hybrid-miner.

Clone the repository:
git clone https://github.com/mdalam-4986/hybrid-miner.git
OR download the ZIP archive and extract it.

Step 2: Install Python
Ensure Python 3.x is installed.

Windows: Download and install from python.org.

Linux: Install via package manager (sudo apt install python3 on Debian-based systems).

MacOS: Install via Homebrew (brew install python3) or download from python.org.

Step 3: Install Dependencies
Navigate to the directory where requirements.txt is located and run the following command to install the required packages:
pip3 install -r requirements.txt

For permission errors (Linux/MacOS):
sudo pip3 install -r requirements.txt
Step 4: Get Your Binance API Keys
This step is required for automatic payouts through Binance.

Sign in to your Binance account (binance.com).

Navigate to the API Management page:
https://www.binance.com/en/my/settings/api-management

Create a new API key:

Label: Give your key a name (e.g., "Hybrid Miner").
Enable the following permissions:
Read (for reading balances).
Withdraw (for auto payouts).
Copy the API Key and Secret Key. You'll need them when running the hybrid script for the first time.

Step 5: Run the Client Script
The client script decrypts and executes the hybrid_monetization.py script from your GitHub repository.

To run the client script:

python3 client.py
Windows users should use:
python client.py

If the script prompts for admin privileges:

Linux/MacOS: It will re-run with sudo.

Windows: Run Command Prompt as Administrator.

Step 6: Configure Wallet and API Settings (First Run Only)

When you run the hybrid_monetization.py script for the first time, you’ll be prompted to enter:

Monero Wallet Address:
This address will be used for CPU mining payouts.
If you don't have one, create a wallet using services like MyMonero.

Binance API Key:
Enter the key you generated in Step 4.
Binance Secret Key:

Enter the corresponding secret key.
These details are saved in userdata.json and reused on subsequent runs.

Step 7: Start Monetization Services
The hybrid script runs the following services in the background:

CPU Mining (via XMRig).

GPU Rental (via NiceHash).

Storage Sharing (via Storj, if added).

Bandwidth Sharing (via Honeygain, if added).

The services are automatically managed by the script.

Step 8: Auto Payouts
The script will perform automatic payouts every 30 minutes using the Binance API.

Client Wallet: Receives 90% of the earnings.
Maintenance Wallet: Receives 10% of the earnings to ensure fee overflows do not occur.
The payout details are printed in the terminal during each interval.

Step 9: Troubleshooting
Common Issues and Solutions

Permission Denied Errors:
Ensure you run the script with admin privileges (sudo on Linux/MacOS or Administrator mode on Windows).

ModuleNotFoundError:
Make sure you installed dependencies correctly with pip3 install -r requirements.txt.

Connection or File Fetch Errors:
Verify your internet connection.
Ensure your GitHub repository is publicly accessible or has the required encrypted files.

Checksum Verification Failure:
Ensure the encryption key matches the one used in the encryption process.
Verify that the encrypted script and checksum file on GitHub are up-to-date.

File Structure Overview
hybrid-miner/
  ├── client.py                # Client script to decrypt and execute the main script
  ├── hybrid_monetization.py    # Main hybrid monetization script
  ├── requirements.txt          # List of required Python packages
  ├── userdata.json             # Stores user data (wallet, API keys)
  └── tools/                    # Contains extracted mining/rental tools (e.g., XMRig)
  
These instructions should guide you through the full setup and usage of the system.
