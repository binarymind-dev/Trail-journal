# 🐦 Trail Journal

**An offline bird-walk companion.** Record a walk with your phone in your pocket, then let open-source AI tell you which birds you heard and write a short journal entry about it in **Marathi**.

Built for the Hacktoberfest Open-Source AI Challenge (Week 1, theme: *Touch Grass*). The screen is the shortest part of the experience: the walk is the point.

## How it works

```
walk recording (.wav/.mp3/.m4a)
        |
        v
BirdNET-Analyzer       -> which birds, how confident (offline)
        |
        v
Gemma 3 4B via Ollama  -> short Marathi journal entry (offline)
        |
        v
journal.md
```

Everything runs locally on a laptop. No API keys, no cloud, no data leaving the machine.

## Why open-source / open-weight

- **Works with no signal:** record on the trail, process at home. Nothing needs the internet after the one-time model downloads.
- **Your recordings stay yours:** audio never touches a server you don't control.
- **Free to run:** BirdNET (~224 MB model) and Gemma 3 4B (~3 GB) are downloaded once.
- **Swappable:** change one line to try another Ollama model (e.g. `gemma3:12b`) or tweak the prompt to change how the journal sounds.

## Setup

Install [Ollama](https://ollama.com/download) first, then:

```bash
pip install birdnet-analyzer ollama
ollama pull gemma3:4b
```

## Run

Put your recordings in a folder called `walk/`, then:

```bash
python trail_journal.py walk
```

The first run downloads the BirdNET model (~224 MB), so give it a few minutes. When it finishes you get `journal.md`.

Set your location in `trail_journal.py` (`LAT, LON`) so BirdNET narrows its species list to your region. The default is Kopargaon, Maharashtra.

## Example output

```
- Asian Koel: 27 detections, avg confidence 0.78
```

See [`journal.md`](journal.md) for a sample generated entry.

## What I learned

My first prompt let Gemma 3 4B invent birds the model never detected and mix Hindi and English words into the Marathi. A stricter prompt fixed it: *write only about the data, do not invent any bird, simple correct Marathi*. Small local models need tight guardrails, but they can do the job.

## Limitations

- The first test used a recording from xeno-canto, not my own walk.
- Gemma 3 4B's Marathi is good but not perfect. Check the text before sharing.
- BirdNET confidence is a guide, not proof. Treat low-confidence detections as maybes.

## Credits

- [BirdNET-Analyzer](https://github.com/birdnet-team/BirdNET-Analyzer), Cornell Lab of Ornithology and Chemnitz University of Technology. Non-commercial license.
- Test audio: Asian Koel recording XC1173496 by Lars Lachmann, from [xeno-canto.org](https://xeno-canto.org).
- [Gemma](https://ai.google.dev/gemma) by Google, run through [Ollama](https://ollama.com).
