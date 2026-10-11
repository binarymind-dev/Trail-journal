import csv, glob, subprocess, sys, collections, ollama

audio_dir = sys.argv[1]
LAT, LON = 19.88, 74.48  # Kopargaon

subprocess.run([sys.executable, "-m", "birdnet_analyzer.analyze", audio_dir,
                "-o", "out", "--rtype", "csv", "--min_conf", "0.4",
                "--lat", str(LAT), "--lon", str(LON)], check=True)

birds = collections.defaultdict(list)
for f in glob.glob("out/**/*.csv", recursive=True):
    with open(f, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if "Common name" in r:
                birds[r["Common name"]].append(float(r["Confidence"]))

summary = "\n".join(f"- {n}: {len(c)} detections, avg confidence {sum(c)/len(c):.2f}"
                    for n, c in sorted(birds.items(), key=lambda x: -len(x[1])))
print(summary)

prompt = f"""You are a warm nature journal writer. Write ONLY about the data below.
Do NOT invent any bird that is not listed. Do NOT mention other birds.

Bird data (from an offline sound model, near Kopargaon, Maharashtra):
{summary}

Write:
1. A 100-word journal entry in simple, correct Marathi (no Hindi words, no English words mixed in). Mention the bird and that the model was fairly confident.
2. Two lines in English.
3. One specific tip for the next walk (for example: time of day, or listening for the koel call near trees).
"""

reply = ollama.chat(model="gemma3:4b", messages=[{"role": "user", "content": prompt}])
journal = reply["message"]["content"]

with open("journal.md", "w", encoding="utf-8") as f:
    f.write("# Trail Journal\n\n## Birds heard\n" + summary + "\n\n## Entry\n" + journal)
print(journal)

