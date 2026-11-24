"""Make the AI Judge Laugh: Office Jokes — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one joke about office life, under 200 characters.
"""
import os

LINE = "The office printer only breaks when something is urgent, and it knows exactly when that is."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
