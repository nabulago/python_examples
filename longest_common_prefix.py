glo_words = [
    # "circle",
    "glow",
    "global",
    "glorious",
    "globe",
    "glob",
    "glowworm",
    "gloriousness",
    "globally",
    "glorify",
    "glossary",
    "glottal",
    "glowstick",
    "glowlight",
    "glorification",
    "gloss",
    "glowingly",
    "glowiness",
    "gloveless",
    "gloversville",
    "gloomy"
]

print(glo_words)
# glo_words = sorted(glo_words,key=lamda x: len(x))
# glo_words = sorted(glo_words, key=lambda x: len(x))

print(glo_words)
# Get the prefix by finding the longest common starting substring
def longest_common_prefix(words):
    if not words:
        return ""
    shortest = min(words, key=len)
    for i in range(len(shortest)):
        for word in words:
            if word[i] != shortest[i]:
                return shortest[:i]
    return shortest

prefix = longest_common_prefix(glo_words)

# Filter using that detected prefix
filtered = [word for word in glo_words if word.startswith(prefix)]

print(f"Detected prefix: '{prefix}'")
print("Matching words:", filtered)