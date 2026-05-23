# MaayanProject — Nail Salons Directory

A small [Flask](https://flask.palletsprojects.com/) web app that lists nail salons and lets you add new entries through a simple form. Data is kept in memory for the lifetime of the server process.

## Features

- Browse a directory of nail salons (name, address, description, services)
- Add new salons via a web form
- Pink-themed, single-page UI with inline HTML templates

## Requirements

- Python 3.8+
- [Flask](https://pypi.org/project/Flask/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MaayanKalka/MaayanProject.git
   cd MaayanProject
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install Flask:

   ```bash
   pip install flask
   ```

## Running the app

From the project root:

```bash
python test.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. The app runs with Flask debug mode enabled by default.

## Usage

- **Home (`/`)** — View all salons and use the “Add a Salon” form at the bottom.
- **Add salon (`POST /add`)** — Submitted from the form. Services should be comma-separated (e.g. `Manicure, Pedicure, Nail Art`).

Sample salons are loaded when the server starts. New salons are appended to the in-memory list and appear after redirecting back to the home page.

## Project structure

```
MaayanProject/
├── README.md      # This file
└── test.py        # Flask app (routes, data, and HTML template)
```

## Notes

- Salon data is **not persisted** to disk or a database; restarting the server resets the list to the built-in defaults (any salons added during the session are lost).
- `test.py` is the main entry point; consider renaming it to `app.py` as the project grows.

## License

No license file is included yet. Add one if you plan to share or open-source the project.
