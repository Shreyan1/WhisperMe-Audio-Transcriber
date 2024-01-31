'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe
WhisperMe
'''

# Sample usage:
# Use logging.debug() for detailed diagnostic information, useful for troubleshooting but typically turned off in production.
# Use logging.info() for general information about application operation.
# Use logging.warning() for situations that are unexpected but not necessarily errors.
# Use logging.error() for errors that occur during operation, which might cause issues or failures.
# Use logging.critical() for serious errors that might prevent the program from continuing.


import os
import logging
from datetime import datetime

def logsetup():
    # Create 'logs' directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure logging
    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    log_filename = f"logs/log_{current_time}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename,
        filemode='w'
    )
