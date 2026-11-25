"""Write one code-review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential
dread: the code works, the tests pass, and the person who wrote it
left in 2021. It is ours now.
"""

import os

LINE = (
    "Approved. The code works, the tests pass, and the person who "
    "wrote it left in 2021. It is ours now."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of /output, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
