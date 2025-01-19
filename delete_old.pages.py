import os
import time

# Directory containing the pages
PAGES_DIR = "/pages"

# Age limit in seconds (10 minutes = 600 seconds)
AGE_LIMIT = 10 * 60

def delete_old_files(directory, age_limit):
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
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

if __name__ == "__main__":
    if os.path.exists(PAGES_DIR):
        delete_old_files(PAGES_DIR, AGE_LIMIT)
    else:
        print(f"Directory not found: {PAGES_DIR}")