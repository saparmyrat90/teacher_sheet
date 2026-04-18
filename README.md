# Teacher Sheet

Anonymous student feedback system for evaluating teachers and subjects with Django.

The project has two main parts:
- a public survey page where students can submit anonymous feedback
- an admin panel where staff can manage teachers, subjects, questions, and exported results

## Features

- Anonymous survey form for students
- Dynamic subject loading by selected teacher
- Dynamic question loading by lesson type
- Admin panel styled with `django-jazzmin`
- Import teachers from `.xlsx`, `.csv`, and `.numbers`
- Import subjects by teacher from `.xlsx`, `.csv`, and `.numbers`
- Export feedback sessions and answers to Excel
- Example subject import files included in `examples/`

## Tech Stack

- Python 3.10+
- Django 5.2
- SQLite
- Pandas
- OpenPyXL
- Jazzmin
- numbers-parser

## Project Structure

```text
core/                 Django project settings and root URLs
survey/               Main app: models, admin, views, templates
examples/             Example import files
requirements.txt      Python dependencies
manage.py             Django management entry point
```

## Data Model

The main models are:

- `Teacher`: teacher name
- `Subject`: subject name linked to a teacher
- `Question`: survey question linked to a lesson type
- `FeedbackSession`: one submitted anonymous survey
- `Answer`: numeric answer for a question inside a session

Supported lesson types:

- `umumy`
- `amaly`
- `tejribe`
- `sohbet`

## How To Run

### 1. Clone the repository

```bash
git clone https://github.com/saparmyrat90/teacher_sheet.git
cd teacher_sheet
```

### 2. Create and activate a virtual environment

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

- Public survey: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Admin Usage

After signing in to `/admin/`, you can:

- add teachers manually
- add subjects manually
- add survey questions for each lesson type
- review feedback sessions and answers
- export selected feedback sessions to Excel

### Import Teachers

Go to:

- `/admin/survey/teacher/`

Use the `Excel import` button and upload one of:

- `.xlsx`
- `.csv`
- `.numbers`

Accepted teacher column names:

- `full_name`
- `teacher`
- `teacher_name`
- `mugallym`
- `mugallym_ady`

For teacher import, a file with only one teacher-name column is enough.

### Import Subjects

Go to:

- `/admin/survey/subject/`

Use the `Excel import` button and upload a file with both teacher and subject columns.

Accepted subject column names:

- `subject`
- `subject_name`
- `name`
- `ders`
- `ders_ady`

Example files:

- [examples/subject_import_example.csv](examples/subject_import_example.csv)
- [examples/subject_import_example.xlsx](examples/subject_import_example.xlsx)

Expected structure:

```csv
full_name,subject
Ahmet Charyyev,Matematika
Ahmet Charyyev,Fizika
Ayna Orazowa,Inlis dili
```

## Public Survey Flow

At `/`, a student can:

1. choose a teacher
2. choose one of that teacher's subjects
3. choose lesson type
4. answer the loaded questions
5. leave an optional comment
6. submit the form anonymously

The frontend loads:

- subjects from `/get-subjects/<teacher_id>/`
- questions from `/get-questions/<lesson_type>/`

## Development Notes

- Database: SQLite (`db.sqlite3`)
- Static URL: `/static/`
- Default local hosts already allowed:
  - `127.0.0.1`
  - `localhost`

If you change models later, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Useful Commands

Run checks:

```bash
python manage.py check
```

Open Django shell:

```bash
python manage.py shell
```

Collect static files for production-style serving:

```bash
python manage.py collectstatic
```

## License

This project is released under the license in [LICENSE](LICENSE).
