import madlib_cli.madlib
from madlib_cli.madlib import load_template_file, merge_template, parse_template, prompt_for_word, save_file
import pytest
import os
from pathlib import Path

def test_load_template_file():
    expected = 'Test File Data'
    actual = load_template_file('test.txt')
    assert actual == expected 

def test_load_template_file_should_error_when_no_file_found():
    with pytest.raises(FileNotFoundError):
       load_template_file('nonexistant.txt')

def test_parse_template():
    expected = ['Adjective', 'A large animal', 'Noun', 'Number 1- 50', "A girl's name"]
    actual = parse_template("This is a {Adjective} and large {A large animal} {Noun}! I will pay {Number 1- 50} dollars it, {A girl's name}")
    print(actual)
    assert type(actual) is list
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])

def test_merge():
    template = 'This is a {Adjective} {Noun}!'
    words = ['cool', 'test']
    expected = 'This is a cool test!'
    actual = merge_template(template, words)
    assert expected == actual

def test_prompt_for_word_return_input():
    madlib_cli.madlib.input = lambda x: 'Table'
    prompt_for_word('Noun') == 'Table'

def test_save_file():
    # setup
    expected = 'Save File Data'
    filename = 'save_test.txt'
    filepath = Path('templates/') / filename
    if os.path.exists(filepath):
        os.remove(filepath)
    assert not os.path.exists(filepath)
    # test
    save_file(filename, 'Save File Data')
    actual = load_template_file(filename)
    assert actual == expected 
    # clean up
    if os.path.exists(filepath):
        os.remove(filepath)
    assert not os.path.exists(filepath)