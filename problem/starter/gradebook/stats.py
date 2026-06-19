"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    totals = {}
counts = {}

for record in records:
    name = record["name"]
    score = record["score"]

    totals[name] = totals.get(name, 0) + score
    counts[name] = counts.get(name, 0) + 1

averages = {}
for name in totals:
    averages[name] = round(totals[name] / counts[name], 2)

return averages
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    subjects = set()

for record in records:
    subjects.add(record["subject"])

return subjects
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    averages = average_per_student(records)

top_name = ""
top_avg = -1

for name, avg in averages.items():
    if avg > top_avg:
        top_name = name
        top_avg = avg

return (top_name, top_avg)
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    averages = average_per_student(records)

passed = []

for name, avg in averages.items():
    if avg >= threshold:
        passed.append(name)

passed.sort()

return passed
    pass
