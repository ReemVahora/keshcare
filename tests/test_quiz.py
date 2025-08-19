import pytest
import types

from pages.utils.session import initSessionState
import importlib.util
import sys
from contextlib import contextmanager

@contextmanager
def dummy_spinner(*args, **kwargs):
    yield


spec = importlib.util.spec_from_file_location("quiz", "src/pages/0_Quiz.py")
quiz = importlib.util.module_from_spec(spec)
sys.modules["quiz"] = quiz
spec.loader.exec_module(quiz)


@pytest.fixture(autouse=True)
def setup_session(monkeypatch):
    """Reset session_state for each test"""
    quiz.st.session_state.clear()
    quiz.st.session_state.chat_history = [
        {"role": "system", "content": "sys"},
        {"role": "assistant", "content": "hello"},
        {"role": "user", "content": "hi"},
    ]
    quiz.st.session_state.results = []
    quiz.st.session_state.results_index = 0
    quiz.st.session_state.awaiting_response = True
    yield


def test_user_input_logic_appends_and_reruns(monkeypatch):
    called = {}

    monkeypatch.setattr(quiz, "scroll_down", lambda: called.setdefault("scroll", True))
    monkeypatch.setattr(quiz.st, "rerun", lambda: called.setdefault("rerun", True))

    quiz.user_input_logic("hello world")

    assert quiz.st.session_state.chat_history[-1] == {
        "role": "user",
        "content": "hello world",
    }
    assert quiz.st.session_state.awaiting_response is False
    assert called["scroll"]
    assert called["rerun"]


def test_bot_response_logic_appends_and_flags(monkeypatch):
    #fake bot response
    fake_response = types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="This is a reply ✓"))]
    )
    monkeypatch.setattr(
        quiz.client.chat.completions,
        "create",
        lambda **kwargs: fake_response,
    )
    monkeypatch.setattr(quiz, "scroll_down", lambda: None)
    monkeypatch.setattr(quiz.st, "rerun", lambda: None)
    monkeypatch.setattr(quiz.st, "spinner", lambda *a, **k: types.SimpleNamespace(__enter__=lambda s: None, __exit__=lambda s, *a: None))
    monkeypatch.setattr(quiz.st, "spinner", dummy_spinner)

    quiz.bot_response_logic("some input")

    assert quiz.st.session_state.chat_history[-1]["role"] == "assistant"
    assert "This is a reply" in quiz.st.session_state.chat_history[-1]["content"]
    assert quiz.st.session_state.awaiting_response is True
    assert quiz.st.session_state.results  # should have reply with ✓
    assert quiz.st.session_state.results_index == 1
