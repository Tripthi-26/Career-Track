# CareerTrack

A simple, free, local Job Application & Resume Management System.

## Technology

- Python
- Flask
- SQLite
- HTML/CSS/JavaScript
- SQLAlchemy
- pytest
- PyPDF2
- python-docx
- ReportLab

No paid APIs, cloud services, or API keys are required.

## Run

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Run tests:

```bash
pytest
```

## Current features

- User registration/login
- Password hashing
- SQLite database
- Job application CRUD
- Application status tracking
- Search/filter
- Dashboard statistics
- Application deadlines
- Resume association

Additional modules will add resume upload/parsing, exports, matching, and REST endpoints.
