import os
import re
from datetime import datetime

# ==== CONFIGURATION ====
ROOT = "problems"
README_PATH = "README.md"

# NeetCode 250 category -> total problems
CATEGORY_TOTALS = {
    "arrays-hashing": 22,
    "two-pointers": 14,
    "sliding-window": 11,
    "stack": 13,
    "binary-search": 7,
    "linked-list": 12,
    "trees": 26,
    "tries": 4,
    "heap": 9,
    "backtracking": 14,
    "graphs": 25,
    "dynamic-programming": 45,
    "greedy": 11,
    "intervals": 10,
    "math-bit": 7,
}

def count_solved():
    solved_counts = {}
    total_solved = 0

    for category, total in CATEGORY_TOTALS.items():
        category_path = os.path.join(ROOT, category)
        if not os.path.exists(category_path):
            solved_counts[category] = 0
            continue
        # Count folders (each folder = 1 problem)
        solved = len([f for f in os.listdir(category_path)
                      if os.path.isdir(os.path.join(category_path, f))])
        solved_counts[category] = solved
        total_solved += solved
    return solved_counts, total_solved

def generate_table(solved_counts):
    rows = []
    for cat, total in CATEGORY_TOTALS.items():
        solved = solved_counts.get(cat, 0)
        percent = int((solved / total) * 100) if total else 0
        emoji = "🟢" if percent >= 70 else "🟡" if percent >= 30 else "⚪"
        display_name = cat.replace("-", " ").title()
        rows.append(f"| {display_name} | {total} | {solved} | {emoji} {percent}% |")
    rows.append(f"| **Total** | **250** | **{sum(solved_counts.values())}** | ⚙️ Ongoing |")
    return "\n".join(rows)

def update_readme(table, total_solved):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Replace the progress table
    new_content = re.sub(
        r"(\| Category \| Total \| Solved \| Progress \|)([\s\S]*?)(\n---)",
        f"\\1\n|-----------|--------|---------|-----------|\n{table}\\3",
        readme,
    )

    # Update solved count in tracker
    new_content = re.sub(
        r"(\| 🧠 Problems Solved \| )\d+ / 250",
        f"\\1{total_solved} / 250",
        new_content
    )

    # Update last updated time
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    new_content = re.sub(
        r"Last Updated: .*",
        f"Last Updated: {now}",
        new_content
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    solved_counts, total_solved = count_solved()
    table = generate_table(solved_counts)
    update_readme(table, total_solved)
    print(f"✅ Updated README — {total_solved} problems solved.")
