import re
from pathlib import Path

def show_welcome():
    print("*" * 30)
    print("** Welcome to MadLib game! **")
    print("*" * 30)
    print("")

def prompt_for_word(token: str) -> str :
    return input(f"Please enter a suitable {token}: ")

def parse_template(template: str) ->  list:
    tokens = re.findall(r"{([\w\s'\d\-]+)}", template)
    return tokens

def load_template_file(filename: str) -> str :
    template_folder = Path('templates/')
    filepath = template_folder / filename
    with open(filepath, "r") as file:
        template = file.read()
    return template

def save_file(filename: str, madlib: str):
    template_folder = Path('templates/')
    filepath = template_folder / filename
    with open(filepath, "w") as file:
        file.write(madlib)

def merge_template(template: str, words: list) -> str :
    result = template
    for word in words:
        result = re.sub(r"{[\w\s'\d\-]+}",word,result,1)
    return result

def main():
    show_welcome()
    template = load_template_file('make_me_a_video_game.txt')
    tokens = parse_template(template)
    words = []
    for token in tokens:
        word = prompt_for_word(token)
        words.append(word)
    print("")
    madlib = merge_template(template, words)
    print(madlib)
    save_file('madlib.txt', madlib)
    print('Thank you! Come again!')
    

if __name__ == "__main__":
    main()