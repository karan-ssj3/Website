# utils/form_handler.py
import csv
import os
from datetime import datetime


def save_contact_submission(name: str, email: str, phone: str, company: str, message: str):
    """Save contact form submission to CSV file."""
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    csv_file = "data/contact_submissions.csv"
    file_exists = os.path.isfile(csv_file)
    
    # Prepare the data
    submission_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name,
        "email": email,
        "phone": phone,
        "company": company if company else "N/A",
        "message": message,
    }
    
    # Write to CSV
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=submission_data.keys())
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(submission_data)
    
    return True