# Trail Journal

Offline bird-walk companion. Record a walk, then:

1. BirdNET-Analyzer identifies birds from the audio (offline).
2. Gemma 3 4B (via Ollama) writes a short Marathi journal entry.

## Run
pip install birdnet-analyzer ollama
ollama pull gemma3:4b
python trail_journal.py walk

Credit: BirdNET-Analyzer (Cornell Lab of Ornithology / Chemnitz University of Technology), non-commercial license.
