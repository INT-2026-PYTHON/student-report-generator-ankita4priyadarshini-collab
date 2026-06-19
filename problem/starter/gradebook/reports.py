"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement

    avg = average_per_student(records)
subjects = sorted(subjects_offered(records))
top_name, top_avg = top_scorer(records)
passed = passing_students(records)

lines = []

lines.append(f"Total records: {len(records)}")
lines.append(f"Subjects offered: {', '.join(subjects)}")
lines.append("Average score per student:")

for name in sorted(avg):
    lines.append(f"  {name}: {avg[name]:.2f}")

lines.append(f"Top scorer: {top_name} ({top_avg:.2f})")
lines.append(f"Passing students: {', '.join(passed)}")

return "\n".join(lines)
pass
