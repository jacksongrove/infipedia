import os
import time

# Directory containing the pages (adjusted for your Docker container structure)
PAGES_DIR = "/app/pages"

# Age limit in seconds (10 minutes)
AGE_LIMIT = 10 * 60

def delete_old_files(directory, age_limit):
    """
    Deletes files in the specified directory that are older than the age limit.

    Args:
        directory (str): The directory to scan for old files.
        age_limit (int): The age limit in seconds. Files older than this will be deleted.
    """
    now = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                # Check if the file is older than the age limit
                file_age = now - os.path.getmtime(file_path)
                if file_age > age_limit:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            else:
                print(f"Skipped: {file_path} (not a file)")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Ensure the directory exists before attempting to delete files
    if os.path.exists(PAGES_DIR):
        print(f"Scanning directory: {PAGES_DIR}")
        delete_old_files(PAGES_DIR, AGE_LIMIT)
    else:
        print(f"Directory not found: {PAGES_DIR}")