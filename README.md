# India.Runs — Candidate Ranking System

## Setup
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt

## Run
python rank.py --candidates data/candidates.jsonl --out outputs/submission.csv --verbose

## Validate
python validate_submission.py outputs/submission.csv