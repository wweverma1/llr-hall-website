# llr_hall_website
Official Website for Lala Lajpat Rai Hall of Residence.

## Features:
- About/Info of Hall
- Photos (photos posted on instagram with #llrhalliitkgp)
- Hall Magzine
- Office Bearers (Current & Past)
- Complaint Zone
- NoticeBoard
- Admin Panel to manage the data

## Setup
- Install Python3.9.5
- Install requirements by running `pip install -r requirements.txt`

## Create Requirements file
- pip3 freeze > requirements.txt

## Start Virtual ENV
- source venv/bin/activate

## Start the server
- python app.py

## How to commit
Before committing any code, following codes must be run to ensure consistent formatting across branches, developer machines and successful tests -

- Auto formatting by running `autopep8 --in-place --recursive .`
- Check for remaining formatting issues by running `flake8 .` (To be fixed manually)
