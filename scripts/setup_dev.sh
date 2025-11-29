#!/bin/bash

# This script sets up the development environment for the Personalized Learning Assistant project.

# Update package list and install necessary packages
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install

# Return to the project root
cd ..

echo "Development environment setup complete."