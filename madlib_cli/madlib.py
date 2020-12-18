import re
from pathlib import Path

def show_welcome():
    print("*" * 36)
    print("** Welcome to MadLib game! **")
    print("*" * 36)
    print("")

def prompt_for_word(token: str) -> str :
    pass

def parse_template(template: str) ->  list:
    tokens = re.findall("{[A-Za-z+]}", template)
    return tokens

def load_template_file(filename: str) -> str :
    template_folder = Path('templates/')
    print(template_folder)
    filepath = template_folder / filename
    print(filepath)
    with open(filepath, "r") as file:
        template = file.read()
    return template


def merge_template(template: str, words: list) -> str :
    pass

def main():
    show_welcome()

if __name__ == "__main__":
    main()