# Internship Intelligence Platform

A portfolio project for collecting internship postings, removing duplicates, scoring fit against a candidate profile, and tracking applications.

## Current milestone

The foundation and core validated domain models are complete. The project can now represent normalized job postings, candidate preferences, skills, and application states without storing private candidate information in the repository.

## Planned capabilities

- Import job postings from structured sources
- Normalize titles, companies, locations, and requirements
- Detect duplicate postings
- Score opportunities against a candidate profile
- Track applications and status changes
- Produce weekly search and application analytics

## Safety

This repository uses synthetic sample data. Do not commit private resumes, personal contact details, employer credentials, or API keys.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m internship_intelligence --help
python -m internship_intelligence model-demo
```

Run the model tests with `python -m unittest discover -s tests`.

## Roadmap

See `docs/roadmap.md`.
