<div align="center">

# 🐦 Trail Journal

**Your offline bird-walk companion.**
Record the walk. Keep your phone in your pocket. Let open-source AI tell you which birds you heard, and write the journal entry in **Marathi**.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Runs offline](https://img.shields.io/badge/Runs-100%25%20offline-brightgreen)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-black)
![Gemma 3](https://img.shields.io/badge/Gemma%203-4B-orange)
![BirdNET](https://img.shields.io/badge/BirdNET-bird%20ID-teal)
![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026-purple)

[Read the article](https://dev.to/loading08/i-let-open-source-ai-name-the-birds-so-my-phone-could-stay-in-my-pocket-c85) · [Quick start](#quick-start) · [How it works](#how-it-works) · [Contributing](#contributing)

</div>

Built for the **Hacktoberfest 2026 DEV Open-Source AI Challenge, Week 1: "Touch Grass."**

Trail Journal turns a raw audio recording into a short, personal bird-walk journal. **BirdNET** identifies the birds, **Gemma 3 4B** (running locally through Ollama) writes the entry, and a small Python script saves it as `journal.md`. No cloud, no account, no API key.

---

## Table of contents

- [Why](#why)
- [Features](#features)
- [Demo](#demo)
- [How it works](#how-it-works)
- [Tech stack](#tech-stack)
- [Quick start](#quick-start)
- [Install (Windows, PowerShell)](#install-windows-powershell)
- [Usage](#usage)
- [Customize](#customize)
- [Project structure](#project-structure)
- [Privacy](#privacy)
- [Why open-weight, local AI](#why-open-weight-local-ai)
- [What went wrong (and how it was fixed)](#what-went-wrong-and-how-it-was-fixed)
- [Results](#results)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Credits](#credits)
- [Author](#author)
- [License](#license)

---

## Why

Most bird apps ask you to stare at a screen while you are supposed to be listening to the trees. The walk should be the point, not the phone. Trail Journal flips the order: **record first, look later.** The screen is the shortest part of the experience.

It also keeps your data yours. A recording of where you walk is personal, so it never leaves your laptop. And the journal is written in the language you actually think in.

## Features

- 🎧 **Offline bird identification.** BirdNET-Analyzer lists the birds it heard, with detection counts and confidence scores.
- 🪶 **Journal in Marathi.** Gemma 3 4B writes a short entry from the detected birds. Bird and place names stay in English, the sentences are Marathi.
- 🛡️ **Guardrailed prompt.** The model is told to write only about the data, never invent a bird, and use simple, correct Marathi.
- 📄 **Plain output.** Everything is saved to a readable `journal.md` file you can keep, edit, or share.
- 🔁 **Swappable parts.** Change the model or the prompt with a one-line edit.
- 🔒 **Private and free.** No login, no tracking, no API keys, no credits. After the one-time model downloads, nothing needs the internet.

## Demo

Test run on an Asian Koel recording from xeno-canto: **27 detections, average confidence 0.78.**

![journal.md output with Marathi entry](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/nj74i8m7bmft704got21.png)

The generated `journal.md` has two parts:

1. **Birds heard**: the BirdNET result (bird, detections, average confidence)
2. **Entry**: the Marathi journal entry written by Gemma 3 4B

The full, unedited result is in [`journal.md`](journal.md).

## How it works

```
 phone recording
        │
        ▼
 ┌───────────────┐   bird list + confidence   ┌──────────────────────┐
 │   BirdNET     │ ─────────────────────────► │ Gemma 3 4B (Ollama)  │
 │  (offline)    │                            │  local, open-weight  │
 └───────────────┘                            └──────────┬───────────┘
                                                         │ Marathi entry
                                                         ▼
                                                    journal.md
```

1. **BirdNET-Analyzer** listens to the recording and lists the birds with confidence scores.
2. **Gemma 3 4B** turns that list into a Marathi journal entry, using a strict prompt.
3. **`trail_journal.py`** (about 40 lines) glues the two together and writes `journal.md`.

The whole pipeline runs on your own machine.

## Tech stack

| Part | Tool | Role |
|---|---|---|
| Bird identification | [BirdNET-Analyzer](https://github.com/birdnet-team/BirdNET-Analyzer) | Detects birds in audio, offline |
| Language model | [Gemma 3 4B](https://ai.google.dev/gemma) | Writes the Marathi journal entry |
| Model runner | [Ollama](https://ollama.com) | Runs Gemma locally |
| Glue | Python 3.10+ | `trail_journal.py` connects everything |
| Output | Markdown | `journal.md` |

## Quick start

```powershell
git clone https://github.com/binarymind-dev/Trail-journal.git
cd Trail-journal
ollama pull gemma3:4b
python trail_journal.py <your-recording>.wav
```

You need BirdNET-Analyzer installed first. See the full steps below.

## Install (Windows, PowerShell)

Requires **Python 3.10+** and roughly **3 GB** of free disk space for the models.

```powershell
cd $HOME\Documents
git clone https://github.com/binarymind-dev/Trail-journal.git
cd Trail-journal
```

**1. BirdNET-Analyzer** (model is about 224 MB). Follow the official install guide: <https://github.com/birdnet-team/BirdNET-Analyzer>

**2. Ollama + Gemma 3 4B** (model is about 3 GB). Install Ollama from <https://ollama.com/download>, reopen the terminal, then:

```powershell
ollama pull gemma3:4b
ollama list
```

The first downloads need internet. After that, everything runs offline.

## Usage

1. Record your walk on your phone and copy the audio file to your computer.
2. Make sure Ollama is running.
3. Run the script on your recording:

   ```powershell
   python trail_journal.py <your-recording>.wav
   ```

4. Open the generated `journal.md`.

> Check the top of `trail_journal.py` for the exact arguments and paths it expects.

**Tip for better results:** a clear recording with the phone close to you works better than one muffled in a bag. Birds that call often are detected more reliably.

## Customize

Everything that matters lives in `trail_journal.py`:

| What | Where | Why change it |
|---|---|---|
| Model | the model name in the script | Try a different Ollama model |
| Prompt | the prompt text in the script | Change the language, tone, or length of the entry |

Swapping the prompt is how the hallucination problem described below was fixed.

## Project structure

```
Trail-journal/
├── trail_journal.py   # the glue script: BirdNET → Gemma → journal.md
├── journal.md         # sample output from the Asian Koel test run
├── README.md          # this file
├── CONTRIBUTING.md    # how to contribute
├── LICENSE            # MIT license for this project's code
└── .gitignore
```

## Privacy

- Recordings are processed on your own machine.
- No audio is uploaded, and no cloud AI service is called.
- No accounts, analytics, or tracking.
- The only internet use is the one-time download of the models.

## Why open-weight, local AI

- **No signal needed.** Record on the trail, process at home.
- **Your recordings stay on your laptop.** No audio goes to a server you don't control.
- **Free.** No API keys or credits.
- **Inspectable and swappable.** Anyone can read, change, or replace the model and the prompt.
- **Marathi.** The journal is in the author's own language, which many apps still ignore.

## What went wrong (and how it was fixed)

The first prompt made Gemma mention "other birds" that BirdNET never detected, and the Marathi contained a stray Hindi word and some garbage text. A stricter prompt fixed most of it: *write only about the data, never invent a bird, use simple correct Marathi.*

Small local models need tight guardrails, but with them they do the job.

## Results

| Item | Value |
|---|---|
| Test recording | Asian Koel, XC1173496 (xeno-canto) |
| BirdNET detections | **27** |
| Average confidence | **0.78** |
| Output | Bird list plus Marathi journal entry ([`journal.md`](journal.md)) |

This is a single test run, not a benchmark.

## Limitations

- The first test used a xeno-canto recording, not a real walk.
- Gemma 3 4B's Marathi is good but not perfect. Check the entry before sharing it.
- The model's raw output can include an English intro line or small spelling slips. The sample in `journal.md` is unedited.
- BirdNET confidence is a guide, not proof. Do not treat a detection as certain.
- Only one recording is tested so far.

## Roadmap

Ideas, not promises:

- [ ] Clean up the model's output (remove the English intro line)
- [ ] Process a whole folder of recordings
- [ ] Add location and date to each entry
- [ ] Support more languages
- [ ] Add automated tests
- [ ] Simple desktop or phone front end

## FAQ

**Does it need the internet?**
Only once, to download BirdNET and Gemma. After that, it runs fully offline.

**Does it cost anything?**
No. There are no API keys or credits.

**Is my audio uploaded anywhere?**
No. Everything is processed on your own machine.

**Why Marathi?**
Because it is the author's own language, and many tools support it poorly. The prompt can be changed to any language Gemma supports.

**Can I use a different model?**
Yes. Change the model name in `trail_journal.py` to any model you have pulled in Ollama.

**Is the bird identification always correct?**
No. BirdNET gives a confidence score, which is a guide, not proof.

**Can I use this commercially?**
The code in this repository is MIT licensed, but BirdNET-Analyzer has a non-commercial license. Check its terms first.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ollama` not recognized | Reopen the terminal, or reinstall Ollama from <https://ollama.com/download> |
| Connection error to Ollama | Start Ollama from the Start menu, or run `ollama serve` |
| Model not found | Run `ollama pull gemma3:4b` |
| First run is slow | The model is loading into memory. Wait, it is faster afterwards |
| Marathi has odd or Hindi words | Tighten the prompt in `trail_journal.py` and run again |
| Model mentions birds that were not detected | Add or strengthen the "never invent a bird" rule in the prompt |
| BirdNET finds nothing | Try a clearer or longer recording |
| Entry starts with an English intro line | Add "Start directly with the entry, no intro line" to the prompt |

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Good first ideas: test on your own recordings, improve the Marathi prompt, or add another language.

## Credits

- **[BirdNET-Analyzer](https://github.com/birdnet-team/BirdNET-Analyzer)**, Cornell Lab of Ornithology and Chemnitz University of Technology (non-commercial license)
- **[Gemma](https://ai.google.dev/gemma)** by Google, run through **[Ollama](https://ollama.com)**
- Test audio **XC1173496** by Lars Lachmann via **[xeno-canto](https://xeno-canto.org)**

## Author

**Snehal Thombare**

- GitHub: [@binarymind-dev](https://github.com/binarymind-dev)
- DEV: [@loading08](https://dev.to/loading08)
- Article: [I let open-source AI name the birds, so my phone could stay in my pocket](https://dev.to/loading08/i-let-open-source-ai-name-the-birds-so-my-phone-could-stay-in-my-pocket-c85)

## License

The code in this repository is released under the [MIT License](LICENSE).

BirdNET-Analyzer, Gemma, and the test audio are separate projects with their own licenses (see Credits). BirdNET-Analyzer is released under a **non-commercial** license, so check its terms before any commercial use.

---

<div align="center">

Made for the walk, not the screen. 🌿

</div>
