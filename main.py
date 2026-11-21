import os

POEM = """You run beside my bike, one hand on the seat.
'Don't let go,' I say. You don't.
My legs learn the speed of being believed.
Then, smaller than the wind: 'Let go.'
You do. That is why I ride straight."""


OUTPUT_NAME = "entry.txt"


def main():
    """Write the poem to OUTPUT_NAME inside the MAKEFUN_OUTPUT_DIR directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
