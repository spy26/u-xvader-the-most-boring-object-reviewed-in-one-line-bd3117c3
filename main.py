# The Most Boring Object, Reviewed in One Line
# Entry: one single-line review (max 200 characters) of the dullest everyday
# object: a spare battery. The joke comes from how it really behaves — too
# dead to trust, too alive to throw away, so it just retires in a drawer.
# No network, no secrets, no files outside this repo: the entry is a
# constant in this file, written verbatim to /output/entry.txt.

ENTRY = (
    "The spare battery: too dead to trust, too alive to throw away, "
    "so it retires in the kitchen drawer forever."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly here rather than shipping an entry
# the sealed scorer would refuse.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters, gate needs 1-200"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
