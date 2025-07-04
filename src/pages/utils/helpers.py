import uuid
import streamlit.components.v1 as components

def copy_button(text: str):
    # Unique ID for each button to avoid conflicts
    button_id = str(uuid.uuid4()).replace("-", "")
    html_code = f"""
    <button id="{button_id}" title="Copy text" style="
        color: #A48172;
        background-color: #FAF5EE !important;
        border: none !important;
        padding: 5px 5px;
        float: right;
        cursor: pointer; j
        font-size: 16px;
        font-weight: bold;
        border-radius: 4px;
    ">⧉</button>
    <script>
    const btn = document.getElementById("{button_id}");
    btn.onclick = () => {{
        navigator.clipboard.writeText({text!r}).then(() => {{
            btn.textContent = '✓';
            setTimeout(() => btn.textContent = '⧉', 1500);
        }});
    }};
    </script>
    """
    components.html(html_code, height=30)