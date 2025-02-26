# src/sorter.py

import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

def get_exif_date(image_path):
    """
    Extracts the date taken from EXIF metadata of an image file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        datetime.datetime or None: Datetime object if date is found, None otherwise.
                                   Returns None if image cannot be opened or EXIF data is missing.
    """
    try:
        try:
            # Attempt to open the image file using PIL library
            image = Image.open(image_path)
        except UnidentifiedImageError as e:
            print(f"Error opening image (or video) {image_path}: {e}")
            return None
        except Exception as e: # Catching other potential opening errors
            print(f"Error opening file {image_path}: {e}")
            return None

        try:
            # Extract EXIF data from the image
            exif_data = image._getexif()
        except Exception as e: # Catch errors during EXIF data extraction
            print(f"Error reading EXIF data from {image_path}: {e}")
            return None

        if not exif_data:
            print(f"No EXIF data found in {image_path}")
            return None

        # Iterate through EXIF tags to find 'DateTimeOriginal' tag
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag) # Get tag name from tag ID
            if tag_name == 'DateTimeOriginal':
                try:
                    # Convert EXIF date string to datetime object
                    date_object = datetime.datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                    return date_object
                except ValueError:
                    print(f"Could not parse DateTimeOriginal value '{value}' in {image_path}")
                    pass # Handle different date formats if needed
    except Exception as e:
        print(f"Unexpected error in get_exif_date for {image_path}: {e}")
    return None

def split_photos_by_date(image_dir, output_dir):
    """
    Splits photos and videos into folders by year and month based on EXIF metadata date.

    Args:
        image_dir (str): Directory containing image and video files to be sorted.
        output_dir (str): Directory where sorted files will be moved.
    """
    # Tuple of supported file extensions (case-insensitive)
    supported_extensions = ('.jpg', '.jpeg', '.png', '.nef', '.mov', '.mp4', '.avi') 

    # Iterate over each file in the input directory
    for filename in os.listdir(image_dir):
        # Check if the file extension is in the supported list
        if not filename.lower().endswith(supported_extensions):
            print(f"Skipping non-image/video file (not a supported format): {filename}")
            continue

        image_path = os.path.join(image_dir, filename) # Construct full file path
        date_taken = get_exif_date(image_path) # Extract date taken from EXIF data

        if date_taken:
            # Extract year and month from the date
            year = date_taken.year
            month_number = date_taken.month
            month_name = date_taken.strftime("%B")  # Full month name (e.g., November)
            month_dir_name = f"{year} {month_name}" # e.g., "2024 November"
            month_dir = os.path.join(output_dir, month_dir_name) # Construct month directory path

            os.makedirs(month_dir, exist_ok=True)  # Create year/month dirs if they don't exist
            output_path = os.path.join(month_dir, filename) # Construct output file path
            os.rename(image_path, output_path)  # Move the file to the destination directory
            print(f"Moved {filename} to {output_path}")
        else:
            print(f"Could not determine date from metadata for {filename}, skipping: {filename}")

def main():
    """Main function to execute the photo sorting script."""
    image_dir = "data/input"  # Directory where input images are located
    output_dir = "data/output" # Directory where sorted images will be placed

    # Ensure input and output directories exist; create them if they don't
    os.makedirs(image_dir, exist_ok=True) # Create input directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True) # Create output directory if it doesn't exist

    print(f"Splitting photos from '{image_dir}' into '{output_dir}'...")
    split_photos_by_date(image_dir, output_dir) # Call function to split photos by date
    print("Photo splitting complete.")

if __name__ == "__main__":
    main() # Execute main function when script is run
