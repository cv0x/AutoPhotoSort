# src/sorter.py

import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_date(image_path):
    """Extracts the date taken from EXIF metadata."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            print(f"No EXIF data found in {image_path}")
            return None
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                try:
                    date_object = datetime.datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    return date_object
                except ValueError:
                    print(f"Could not parse DateTimeOriginal value '{value}' in {image_path}")
                    pass # Handle different date formats if needed
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
    return None

def split_photos_by_date(image_dir, output_dir):
    """Splits photos into folders by year and month based on EXIF date."""
    for filename in os.listdir(image_dir):
        image_path = os.path.join(image_dir, filename)
        date_taken = get_exif_date(image_path)

        if date_taken:
            year = date_taken.year
            month_number = date_taken.month
            month_name = date_taken.strftime("%B")  # Full month name (e.g., November)
            month_dir_name = f"{year} {month_name}" # e.g., "2024 November"
            month_dir = os.path.join(output_dir, month_dir_name)

            os.makedirs(month_dir, exist_ok=True)  # Create year/month dirs if they don't exist
            output_path = os.path.join(month_dir, filename)
            os.rename(image_path, output_path)  # Move the file
            print(f"Moved {filename} to {output_path}")
        else:
            print(f"Could not determine date for {filename}, skipping: {filename}")

def main():
    image_dir = "data/input"  # Input directory for photos
    output_dir = "data/output" # Output directory for sorted photos

    os.makedirs(image_dir, exist_ok=True) # Ensure input directory exists
    os.makedirs(output_dir, exist_ok=True) # Ensure output directory exists

    print(f"Splitting photos from '{image_dir}' into '{output_dir}'...")
    split_photos_by_date(image_dir, output_dir)
    print("Photo splitting complete.")

if __name__ == "__main__":
    main()
