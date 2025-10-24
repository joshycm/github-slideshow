# VLSI Application

This repository contains a Python project for creating VLSI (Very Large Scale Integration) applications. It provides a foundational structure for developing, testing, and managing custom VLSI-related Python code.

## Getting Started

To get started with this project, you'll need to set up a Python virtual environment and install the required dependencies.

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

This project uses Python's built-in `unittest` framework for testing. To run the tests, execute the following command from the `vlsi_app` directory:

```bash
python3 -m unittest discover tests
```

## Project Structure

The project is organized as follows:

-   `src/`: This directory contains the main source code for the VLSI application.
-   `tests/`: This directory contains all the unit tests for the project.
-   `requirements.txt`: This file lists the Python dependencies for the project.
-   `.gitignore`: This file specifies which files and directories should be ignored by Git.
