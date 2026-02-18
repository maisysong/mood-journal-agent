# Mood Journal Agent

A conversational AI agent that helps you track your mood over time. Tell it how you're feeling, and it will save your entry, remember your history, and surface patterns — all through a natural conversation in your terminal.

Built with Python, LLaMA 3.3 (via Groq), and a simple JSON file for storage.

---

## What It Does

- Listens to how you're feeling and responds with empathy
- Extracts your mood and themes (e.g. work, sleep, anxiety) and saves them automatically
- Recalls past entries when you ask how you've been feeling over time
- Notices patterns across entries and reflects them back to you

This is a wellness journaling tool — not a replacement for therapy or clinical care.

---

## Project Structure

```
mood-journal-agent/
│
├── main.py              # Entry point — run this to start the agent
├── agent.py             # The agent loop (where the magic happens)
├── config.py            # API key, model name, settings
├── requirements.txt     # Python dependencies
│
├── prompts/
│   └── system.txt       # The agent's personality and rules
│
├── tools/
│   ├── __init__.py
│   ├── journal.py       # save_entry() and read_entries() functions
│   └── registry.py      # Connects tool functions to the LLM
│
└── data/
    └── journal.json     # Where your journal entries are stored
```

---

## Setup

### 1. Clone the repo and navigate into it

```bash
git clone <your-repo-url>
cd mood-journal-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a Groq API key

Create a free account at [console.groq.com](https://console.groq.com), go to **API Keys**, and generate a key.

### 5. Create a `.env` file

In the root of the project, create a file called `.env` and add your key:

```
GROQ_API_KEY=gsk_your-key-here
```

### 6. Initialize the journal file

```bash
echo "[]" > data/journal.json
```

---

## Running the Agent

```bash
python main.py
```

You'll see a prompt. Just start talking:

```
You: I've been feeling really anxious lately, mostly about work deadlines.

Agent: That sounds really exhausting — carrying that kind of pressure day to day takes a toll...
```

To exit, type `quit` or `exit`.

---

## Example Interactions

**Logging a mood:**
> "I had a rough day. Couldn't sleep last night and felt overwhelmed at work."

**Asking about patterns:**
> "How have I been feeling this week?"
> "Have you noticed any patterns in my entries?"

---

## How It Works

The agent runs in a loop:

1. You send a message
2. The LLM decides whether to respond directly or call a tool
3. If it calls a tool, the result is fed back into the conversation
4. The loop continues until the LLM gives a final response

There are two tools: `save_entry` (writes to `data/journal.json`) and `read_entries` (reads from it). Everything else — empathy, pattern recognition, summarization — is handled by the LLM.

---

## Tech Stack

- **Python 3.10+**
- **Groq API** — free LLM inference
- **LLaMA 3.3 70B** — the underlying model
- **python-dotenv** — for managing the API key

---

## Roadmap

- [ ] Phase 2: CBT thought reframing assistant
- [ ] Phase 3: Combined agent — journal history informs reframing sessions

---

## Disclaimer

This tool is for personal wellness journaling only. It is not a licensed mental health product and should not be used as a substitute for professional mental health care. If you are in crisis, please contact the 988 Suicide & Crisis Lifeline by calling or texting **988**.