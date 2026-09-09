"""Validated domain models used by the Internship Intelligence Platform.

These models deliberately contain only job-search data. Resumes, personal contact
details, and private application notes belong in ignored local files, never Git.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ApplicationStatus(StrEnum):
    """The lifecycle of a job application."""

    SAVED = "saved"
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFERED = "offered"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


def normalize_text(value: str) -> str:
    """Return a trimmed, lowercase value suitable for comparisons."""
    return " ".join(value.strip().lower().split())


def normalize_skills(skills: list[str]) -> list[str]:
    """Normalize, deduplicate, and preserve the first occurrence of each skill."""
    normalized: list[str] = []
    seen: set[str] = set()
    for skill in skills:
        value = normalize_text(skill)
        if not value:
            continue
        if value not in seen:
            normalized.append(value)
            seen.add(value)
    return normalized


def require_text(value: str, field_name: str) -> str:
    normalized = normalize_text(value)
    if not normalized:
        raise ValueError(f"{field_name} is required")
    return normalized


@dataclass(slots=True)
class JobPosting:
    """A normalized internship or entry-level job posting."""

    identifier: str
    title: str
    company: str
    location: str
    skills: list[str]
    source: str
    remote: bool = False
    url: str | None = None

    def __post_init__(self) -> None:
        self.identifier = require_text(self.identifier, "identifier")
        self.title = require_text(self.title, "title")
        self.company = require_text(self.company, "company")
        self.location = require_text(self.location, "location")
        self.source = require_text(self.source, "source")
        self.skills = normalize_skills(self.skills)
        if self.url is not None and not self.url.startswith(("https://", "http://")):
            raise ValueError("url must start with http:// or https://")


@dataclass(slots=True)
class CandidateProfile:
    """A private, local-only candidate profile used for explainable matching."""

    target_roles: list[str]
    skills: list[str]
    preferred_locations: list[str] = field(default_factory=list)
    work_authorization: str | None = None

    def __post_init__(self) -> None:
        self.target_roles = normalize_skills(self.target_roles)
        if not self.target_roles:
            raise ValueError("at least one target role is required")
        self.skills = normalize_skills(self.skills)
        self.preferred_locations = normalize_skills(self.preferred_locations)
        if self.work_authorization is not None:
            self.work_authorization = require_text(
                self.work_authorization, "work_authorization"
            )
