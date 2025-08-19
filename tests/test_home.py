from prompts import buildHomeInfo
import types
import sys
import importlib

def test_homepage_renders(monkeypatch):
    # fake st module to capture calls
    fake_st = types.SimpleNamespace()
    captured = {}

    # mock functions we care about
    fake_st.session_state = {}
    fake_st.set_page_config = lambda **kwargs: None
    fake_st.markdown = lambda text, **kwargs: captured.setdefault("markdown", []).append(text)
    fake_st.write = lambda text: captured.setdefault("write", []).append(text)
    fake_st.button = lambda label: False
    fake_st.switch_page = lambda page: captured.setdefault("switch", []).append(page)

    # patch the streamlit module
    monkeypatch.setitem(sys.modules, "streamlit", fake_st)

    # load Home
    importlib.reload(importlib.import_module("Home"))
    # check if text rendered
    assert buildHomeInfo() in captured["write"]
