﻿# Solana Token Scanner
Setup Instructions
Install Python 3.13.2
Download and install from python.org. Add to PATH if necessary.

Set Up in IntelliJ

Open IntelliJ → File → Project Structure → Set SDK to Python 3.13.2.
Create a new virtual environment:
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate (CMD) or venv\Scripts\Activate.ps1 (PowerShell).
Install Dependencies
Install the required packages:
pip install requests solana solders
(Upgrade pip if needed):
python -m pip install --upgrade pip

Run Script
Run the Solana Token Scanner script:
python scanner.py
