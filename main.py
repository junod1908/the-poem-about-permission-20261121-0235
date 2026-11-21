import os

POEM = """You run beside my bike, one hand on the seat.
'Don't let go,' I say. You don't.
My legs learn the speed of being believed.
Then, smaller than the wind: 'Let go.'
You do. That is why I ride straight."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
