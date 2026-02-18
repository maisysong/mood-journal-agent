import json
import datetime 
from config import JOURNAL_FILE

def save_entry(mood: str, themes: list, raw: str) -> str:
    """
    Save a journal entry to the JSON file.
    """

    entry = {
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        'mood': mood,
        'themes': themes,
        'raw': raw
    }

    with open(JOURNAL_FILE, 'r') as f:
        entries = json.load(f)
    
    entries.append(entry)

    with open(JOURNAL_FILE, 'w') as f:
        json.dump(entries, f, indent=2)

    return f'Entry saved. Mood: {mood}, Themes: {", ".join(themes)}.'

def read_entries(limit: int = 10) -> str:
    """
    Read the last N journal entries and return them as a string.
    """

    with open(JOURNAL_FILE, 'r') as f:
        entries = json.load(f)

    if not entries:
        return 'No journal entries found.'
    
    recent = entries[-limit:]
    output = ""

    for e in recent:
        output += f'\n[{e['date']}] Mood: {e['mood']} | Themes: {', '.join(e['themes'])}\n{e['raw']}\n'
    return output.strip()
