# The Self-Checkout Is Judging You — one smug line, printed and written to /output/entry.txt.
import os

LINE = "Twelve yoghurts, one banana, zero shame detected \u2014 please place your dignity in the bagging area."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
