import unittest

from internship_intelligence.models import CandidateProfile, JobPosting, normalize_skills


class SkillNormalizationTests(unittest.TestCase):
    def test_normalizes_and_deduplicates_skills(self) -> None:
        self.assertEqual(
            normalize_skills([" SQL ", "python", "sql", "", "Data   Viz"]),
            ["sql", "python", "data viz"],
        )


class JobPostingTests(unittest.TestCase):
    def test_normalizes_posting_fields(self) -> None:
        posting = JobPosting(
            identifier=" Posting-1 ",
            title=" Data Analyst Intern ",
            company=" Example Co. ",
            location=" Remote ",
            skills=["SQL", "sql", "Python"],
            source=" Synthetic ",
        )
        self.assertEqual(posting.identifier, "posting-1")
        self.assertEqual(posting.skills, ["sql", "python"])

    def test_rejects_non_http_url(self) -> None:
        with self.assertRaises(ValueError):
            JobPosting(
                identifier="posting-1",
                title="Data Analyst Intern",
                company="Example Co.",
                location="Remote",
                skills=[],
                source="synthetic",
                url="ftp://example.com",
            )


class CandidateProfileTests(unittest.TestCase):
    def test_requires_target_role(self) -> None:
        with self.assertRaises(ValueError):
            CandidateProfile(target_roles=[], skills=["SQL"])

