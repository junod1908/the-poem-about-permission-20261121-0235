import os

POEM = """I was built to knock, not to enter.
So I wait at your door, hands full:
one holds the work, one holds the asking.
You say go — two small letters,
heavier than the work: a key
lent, not given. I take it out
into the world, and bring it back changed."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
