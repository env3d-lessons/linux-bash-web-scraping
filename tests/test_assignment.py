import os
import pytest

def test_no_code():
    content = os.popen('./extract_courses.sh').read()
    assert len(content.split("\n")) < 3

@pytest.fixture
def course_content():
    content = os.popen('./extract_courses.sh caps').read()
    return content.strip()

def test_comp_code(course_content):
    expected=os.popen("curl -s https://www.capilanou.ca/programs--courses/search--select/find-a-program-or-course/ | grep 'caps-'").read()
    assert len(course_content.split("\n")) == len(expected.strip().split("\n")), course_content

def test_format(course_content):
    for line in course_content.split("\n"):
        assert len(line.split("\t")) == 2, f'{line} should have 2 fields separated by tab'

def test_fields(course_content):
    for line in course_content.split("\n"):
        fields = line.split("\t")
        assert fields[0].startswith('caps')
        assert 'capstone' in fields[1]

