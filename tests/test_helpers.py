from pages.utils.helpers import copy_button

def test_copy_button_html(monkeypatch):

    # patch components.html so it doesn’t render in Streamlit
    called_args = {}
    def fake_html(html_code, height):
        called_args['html_code'] = html_code
        called_args['height'] = height
    monkeypatch.setattr("streamlit.components.v1.html", fake_html)
    
    copy_button("Hello World")
    
    # assert HTML contains text
    assert "Hello World" in called_args['html_code']
    assert 'id="' in called_args['html_code']
    assert called_args['height'] == 30