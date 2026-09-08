"""Command-line entry point for the platform."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Internship Intelligence Platform")
    parser.add_argument("--version", action="version", version="0.1.0")
    return parser


def main() -> None:
    build_parser().parse_args()
    print("Internship Intelligence Platform foundation ready.")
