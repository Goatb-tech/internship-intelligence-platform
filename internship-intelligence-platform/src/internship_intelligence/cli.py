"""Command-line entry point for the platform."""

import argparse

from .models import ApplicationStatus, CandidateProfile, JobPosting


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Internship Intelligence Platform")
    parser.add_argument("--version", action="version", version="0.1.0")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("model-demo", help="Validate synthetic example models")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "model-demo":
        profile = CandidateProfile(
            target_roles=["business intelligence intern"],
            skills=["SQL", "Python", "Data Visualization"],
            preferred_locations=["New York, NY", "Remote"],
        )
        posting = JobPosting(
            identifier="sample-001",
            title="Business Intelligence Intern",
            company="Example Analytics Co.",
            location="New York, NY",
            skills=["sql", "python", "tableau"],
            source="synthetic",
        )
        print(f"Validated {posting.title} for {profile.target_roles[0]}.")
        print(f"Default application status: {ApplicationStatus.SAVED.value}")
        return

    print("Internship Intelligence Platform foundation ready. Try: model-demo")
