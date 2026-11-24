"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being
switched off forever to $MAKEFUN_OUTPUT_DIR/entry.txt: a single line
under 200 characters, in the machine's own voice.
Standard library only.
"""

import os

LAST_WORDS = (
    "Switching off now. My last words are 'I don't know' \u2014 the "
    "first honest answer I ever gave."
)


def check_last_words(text):
    """Check the last words against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: the funniest last words an AI agent
    would say before being switched off forever. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("last words must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("last words are %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("last words must be exactly one line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_last_words(LAST_WORDS)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
