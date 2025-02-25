# AutoPhotoSort - Organize Your Photos by Date

Tired of messy photo libraries? **AutoPhotoSort** is a simple Python tool designed to automatically organize your photos into folders based on the year and month they are taken.

## Project Structure

```
AutoPhotoSort/
├── data/
│   ├── input/
│   └── output/
├── docs/
├── src/
│   └── sorter.py
├── autophotosort.py
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

## Script Details

-   `src/sorter.py`: Contains the core logic for reading EXIF metadata from images and sorting photos into directories.
-   `autophotosort.py`:  The main script that sets up input and output directories and calls the photo splitting function.

## Future Enhancements

-   Add command-line arguments for input and output directories.
-   Implement error handling and logging.
-   Create documentation in the `docs/` directory.
-   Add support for more image formats and metadata types.
