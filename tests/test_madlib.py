from madlib_cli.madlib import load_template_file, merge_template,parse_template
import pytest

def test_load_template_file():
    expected = 'Test File Data'
    actual = load_template_file('test.txt')
    assert actual == expected 

def test_load_template_file_should_error_when_no_file_found():
    with pytest.raises(FileNotFoundError):
       load_template_file('nonexistant.txt')

def test_parse_template():
    expected = ['Adjective', 'Noun']
    actual = parse_template('This is a {Adjective} {Noun}!')
    assert type(actual) is list
    assert all([a == b for a, b in zip(actual, expected)])

def test_merge():
    template = 'This is a {Adjective} {Noun}!'
    words = ['cool', 'test']
    expected = 'This is a cool test!'
    actual = merge_template(template, words)
    assert expected == actual
