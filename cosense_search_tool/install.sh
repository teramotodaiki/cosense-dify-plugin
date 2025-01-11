#!/bin/bash
pip install requests

# Set environment variables
export FORCE_VERIFYING_SIGNATURE=false

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "FORCE_VERIFYING_SIGNATURE=false" > .env
fi
