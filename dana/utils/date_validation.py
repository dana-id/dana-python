# Copyright 2026 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
DateValidation

Utility module for validating date fields, specifically validUpTo dates.
"""

import datetime
import os


def validate_valid_up_to_date(date_str: str) -> None:
    """
    Validate that a date string is not more than 30 minutes in the future (sandbox only).
    
    This function checks the DANA_ENV or ENV environment variable and only validates in sandbox environment.
    
    Args:
        date_str: The date string to validate in RFC3339 format (e.g., "2024-01-01T12:00:00+07:00")
    
    Raises:
        ValueError: If the date is invalid or exceeds 30 minutes in the future
    """
    # Only validate in sandbox environment
    env = os.getenv("DANA_ENV", os.getenv("ENV", "sandbox")).lower()
    if env == "sandbox":
        try:
            # Create Jakarta timezone (GMT+7)
            jakarta_tz = datetime.timezone(datetime.timedelta(hours=7))
            
            # Current date in Jakarta timezone
            current_date = datetime.datetime.now(jakarta_tz)
            
            # Maximum allowed date (current date + 30 minutes)
            max_date = current_date + datetime.timedelta(minutes=30)
            
            # Parse the input date
            # The date string should be in format: YYYY-MM-DDTHH:mm:ss+07:00
            # Remove the timezone offset part for parsing
            date_part = date_str[:-6]  # Remove '+07:00' or similar
            input_date = datetime.datetime.fromisoformat(date_part).replace(tzinfo=jakarta_tz)
            
            # Check if the input date exceeds the maximum allowed date
            if input_date > max_date:
                raise ValueError('validUpTo date cannot be more than 30 minutes in the future')
        except ValueError as e:
            if 'minutes' in str(e):
                raise
            raise ValueError('Invalid date format for validUpTo. Expected format: YYYY-MM-DDTHH:mm:ss+07:00') from e
