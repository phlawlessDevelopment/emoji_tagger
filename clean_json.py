# importing the module
import json

# Opening JSON file
data = {}
fixtures = []

with open('emoji_list.json', 'r') as f:
    emoji_list = json.load(f)
    for i, emoji in enumerate(emoji_list):
        fixtures.append({
            "model": "tagger.emoji",
            "pk": i+1,
            "fields": {
                "unicode": emoji,
            }
        }),

with open('emoji_list.json', 'w') as f:
    json.dump(fixtures, f)
