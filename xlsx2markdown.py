import os
import pandas as pd

# read .xlsx file and write .md files

input_filename = input("filename(.xlsx): ")
output_dir = input("output dirname: ")

df = pd.read_excel(input_filename, dtype=str)

### write
for i, row in df.iterrows():
    index = row["index"]
    url = row["url"]
    title = row["title"]
    date = row["date"]
    description = row["description"]
    about = row["about"]

    steps = []
    for i in range(4):
        d = row["step" + str(i)]
        if not pd.isna(d):
            steps.append(d)

    points = []
    for i in range(4):
        d = row["point" + str(i)]
        if not pd.isna(d):
            points.append(d)

    # write
    with open(os.path.join(output_dir, str(index).zfill(3) + url + ".md"), "w", encoding="utf-8", newline="") as f:
        f.write("---\n")
        f.write("index: '" + str(index) + "'\n")
        f.write("title: '" + title + "'\n")
        f.write("date: '" + str(date) + "'\n")
        f.write("description: '" + str(description) + "'\n")
        f.write("about: '" + str(about) + "'\n")
        f.write("steps: [")
        for step in steps:
            f.write("'" + str(step) + "',")
        f.write("]\n")
        f.write("points: [")
        for point in points:
            f.write("'" + str(point) + "',")
        f.write("]\n")
        f.write("---\n")