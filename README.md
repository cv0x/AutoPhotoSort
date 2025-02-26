# AutoPhotoSort - Organize Your Photos by Date

- Tired of messy photo libraries? **AutoPhotoSort** is a simple Python tool designed to automatically organize your photos into folders based on the year and month they are taken.
- Supported formats = '.jpg', '.jpeg', '.png', '.nef', '.mov', '.mp4', '.avi'

## Project Structure

```
AutoPhotoSort/
├── data/
│   ├── input/
│   └── output/
├── src/
│   ├── AutoPhotoSortLogo.png
│   └── sorter.py
├── autophotosort.py
├── autophotosort_gui.py
├── AutoPhotoSort start.bat
├── README.md
└── requirements.txt
```

## Dependencies

- Pillow (PIL): For image processing and EXIF data extraction.

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use AutoPhotoSort

1.  **Installation:**

    Open your terminal in the `AutoPhotoSort` project directory.
    Run the following command to install the necessary Python library:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Prepare Your Photos:**

    Place the photos you wish to organize into the `data/input` directory within the project folder.

3.  **Run the AutoPhotoSort Script:**

    In the same terminal, execute the `autophotosort.py` script:
    ```bash
    python autophotosort.py
    ```

4.  **Find Your Sorted Photos:**

    Once the script finishes, your photos will be sorted into folders by year and month within the `data/output` directory. For example, photos taken in November 2024 will be in a folder named `2024 November`.

## GUI Application
![AutoPhotoSort GUI](https://github.com/cv0x/AutoPhotoSort/blob/main/src/img/gui.png?raw=true)

This project now includes a graphical user interface (GUI) for easier interaction.

### How to Run the GUI

1.  **Run the `AutoPhotoSort start.bat` script:**
    Simply double-click the `AutoPhotoSort start.bat` file in the project directory.
    -   This script will automatically check if Python is installed and guide you to install it if necessary.
    -   It will also install the required Python libraries from `requirements.txt`.
    -   Finally, it will launch the `autophotosort_gui.py` application.

2.  **Using the GUI:**
    -   The GUI provides buttons to open and select input and output folders. By default, it is set to `data/input` and `data/output` folders in the project directory.
    -   Click "Start Sorting" to begin organizing your photos.

## Script Details

-   `src/sorter.py`: Contains the core logic for reading EXIF metadata from images and sorting photos into directories.
-   `autophotosort.py`:  The main script that sets up input and output directories and calls the photo sorting function for command line interface.
-   `autophotosort_gui.py`: Implements the graphical user interface using Tkinter, providing an easier way to interact with the photo sorting tool.
-   `AutoPhotoSort start.bat`: A batch script that simplifies running the GUI application by checking for Python, installing dependencies, and launching `autophotosort_gui.py`.

## Future Enhancements

-   Add command-line arguments for input and output directories.
-   Implement error handling and logging.
-   Add support for more image formats and metadata types.
