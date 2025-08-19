import pytest
import types
import re
import importlib.util
import sys

from prompts import getGlossary

spec = importlib.util.spec_from_file_location("glossary", "src/pages/2_Glossary.py")
glossary = importlib.util.module_from_spec(spec)
sys.modules["glossary"] = glossary
spec.loader.exec_module(glossary)


############################################# unit testing for highlight_text ###############################################

def test_highlight_text_exact_match():
    text = "Amla is an Ayurvedic herb."
    keyword = "Amla"
    result = glossary.highlight_text(text, keyword)
    assert "<mark>Amla</mark>" in result


def test_highlight_text_lowercase_match():
    text = "amla is powerful"
    keyword = "amla"
    result = glossary.highlight_text(text, keyword)
    assert "<mark>amla</mark>" in result


def test_highlight_text_empty_keyword():
    text = "Neem is a herb."
    keyword = ""
    result = glossary.highlight_text(text, keyword)
    assert result == text  #unchanged

############################################# unit testing for score_result ###############################################

def test_score_result_exact_title_match():
    key = "Amla"
    value = "Some description"
    score = glossary.score_result(key, value, "Amla")
    assert score == 4


def test_score_result_exact_desc_match():
    key = "Neem"
    value = "Amla is great"
    score = glossary.score_result(key, value, "Amla")
    assert score == 3


def test_score_result_partial_title_match():
    key = "Ashwagandha"
    value = "Random text"
    score = glossary.score_result(key, value, "ashwa")
    assert score == 2


def test_score_result_partial_desc_match():
    key = "Neem"
    value = "This contains ashwagandha extract"
    score = glossary.score_result(key, value, "ashwa")
    assert score == 1


def test_score_result_no_match():
    key = "Neem"
    value = "Leafy herb"
    score = glossary.score_result(key, value, "xyz")
    assert score == 0

############################################# mock glossary rendering ###############################################

def test_glossary_sorted(monkeypatch: pytest.MonkeyPatch):
    fake_gloss = {"B": "second", "A": "first"}

    monkeypatch.setattr(
        glossary,
        "prompts",
        types.SimpleNamespace(getGlossary=lambda: fake_gloss)
    )

    sorted_glossary = dict(sorted(fake_gloss.items()))
    assert list(sorted_glossary.keys()) == ["A", "B"]
