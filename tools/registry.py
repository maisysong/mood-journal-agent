from tools.journal import save_entry, read_entries

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "save_entry",
            "description": "Save a journal entry after the user shares how they're feeling. Extract mood and themes from the conversation before calling this.",
            "parameters": {
                "type": "object",
                "properties": {
                    "mood": {
                        "type": "string",
                        "description": "A single word or short phrase describing the user's mood (e.g. anxious, calm, overwhelmed)"
                    },
                    "themes": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "A list of themes from the entry (e.g. ['work', 'sleep', 'relationships'])"
                    },
                    "raw": {
                        "type": "string",
                        "description": "The user's original message, copied exactly as they wrote it"
                    }
                },
                "required": ["mood", "themes", "raw"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_entries",
            "description": "Read past journal entries. Use this when the user asks about their history, patterns, or how they've been feeling over time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "How many recent entries to retrieve. Default is 10."
                    }
                },
                "required": []
            }
        }
    }
]

TOOL_MAP = {
    "save_entry": save_entry,
    "read_entries": read_entries
}