from pages.utils.session import initSessionState
from prompts import buildIntro

def test_initSessionState():
    state = initSessionState()
    assert state["quiz_started"] == False
    assert state["awaiting_response"] == True
    
    assert len(state["chat_history"]) == 4
    assert state["chat_history"][3]["content"] == buildIntro()

    assert state["results"] == []
    assert state["results_index"] == -1
    assert state["results_list"] == False