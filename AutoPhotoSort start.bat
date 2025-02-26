@echo off
REM Check if Python is installed
where python
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

REM Install requirements
pip install -r requirements.txt

REM Run the GUI
python autophotosort_gui.py
pause
