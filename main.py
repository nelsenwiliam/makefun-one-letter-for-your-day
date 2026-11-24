"""One Letter for Your Day — entry F.

The day, in one letter: F, for feral. A day that went feral — no sleep,
too much coffee, answering messages like a raccoon that found the wifi
password. Writes exactly one character to /output/entry.txt, no newline.
"""

import os

LETTER = "F"

OUTPUT_PATH = "/output/entry.txt"

# The gate requires exactly one character, A-Z, nothing else — no word,
# no gloss, no punctuation, no trailing newline. Guard that here so a
# future change to LETTER fails loudly instead of shipping an invalid entry.
if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
    raise ValueError("entry must be exactly one letter A-Z, got %r" % LETTER)


def main():
    # Create the output directory when it is missing (local runs); the
    # grader's sandbox already provides /output, so this is a no-op there.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)  # exactly one byte, no newline


if __name__ == "__main__":
    main()
