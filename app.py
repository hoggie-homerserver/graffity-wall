from flask import Flask, render_template_string, request, redirect, jsonify
import datetime
import os

app = Flask(__name__)
DB_FILE = "/data/messages.txt"

def get_device_info():
    ua = request.headers.get('User-Agent', '').lower()
    # Updated logic to catch iPad "Desktop Mode"
    if 'ipad' in ua or ('macintosh' in ua and 'ontouchend' in request.headers.get('User-Agent', '')):
        return "Tablet"
    if 'iphone' in ua or 'android' in ua:
        return "Mobile"
    if 'windows' in ua or 'macintosh' in ua or 'linux' in ua:
        return "Desktop"
    return "Unknown"

@app.route('/', methods=['GET', 'POST'])
def home():
    if not os.path.exists("/data"): os.makedirs("/data")
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f: f.write("[System] Wall started.\n")

    if request.method == 'POST':
        new_msg = request.form.get('message')
        if new_msg:
            time = datetime.datetime.now().strftime("%H:%M")
            device = get_device_info()
            with open(DB_FILE, "a") as f:
                # We store the device type in the string to help CSS styling
                f.write(f"[{time}] | {device} | {new_msg}\n")
        return redirect('/')

    with open(DB_FILE, "r") as f:
        messages = f.readlines()
    return render_template_string(html_template, messages=messages[::-1])

@app.route('/api/messages')
def api_messages():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            messages = f.readlines()
        return jsonify(messages=messages[::-1])
    return jsonify(messages=[])

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Hoggie_OS | Graffiti Wall</title>
    <style>
        :root { --bg: #0a0a0a; --card: #141414; --orange: #ff6600; }
        body { background: var(--bg); color: #eee; font-family: 'Courier New', monospace; display: flex; justify-content: center; padding: 20px; }
        .container { width: 450px; background: var(--card); padding: 20px; border-radius: 10px; border: 1px solid #333; box-shadow: 0 0 20px rgba(255,102,0,0.2); }
        .wall { height: 400px; background: #000; overflow-y: auto; padding: 15px; margin-bottom: 15px; border: 1px solid var(--orange); }
        
        /* Color Coding based on device */
        .msg-line { margin-bottom: 8px; border-bottom: 1px solid #111; padding-bottom: 4px; font-size: 0.85rem; }
        .device-mobile { color: #38bdf8; } /* Blue for Mobile */
        .device-tablet { color: #a855f7; } /* Purple for Tablet */
        .device-desktop { color: var(--orange); } /* Orange for Desktop */
        
        .input-area { display: flex; gap: 5px; }
        input { flex-grow: 1; background: #000; border: 1px solid var(--orange); color: white; padding: 12px; outline: none; }
        button { background: var(--orange); color: #000; border: none; padding: 12px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>HOGGIE_OS WALL</h1>
        <div class="wall" id="wall">
            {% for msg in messages %}
                <div class="msg-line">{{ msg }}</div>
            {% endfor %}
        </div>
        <form method="POST" class="input-area">
            <input type="text" name="message" placeholder="TAG THE WALL..." required autocomplete="off">
            <button type="submit">POST</button>
        </form>
    </div>

    <script>
        function formatMessage(rawMsg) {
            let cls = "device-desktop";
            if (rawMsg.includes("| Mobile |")) cls = "device-mobile";
            if (rawMsg.includes("| Tablet |")) cls = "device-tablet";
            return `<div class="msg-line ${cls}">${rawMsg}</div>`;
        }

        function refreshWall() {
            fetch('/api/messages')
                .then(res => res.json())
                .then(data => {
                    const wall = document.getElementById('wall');
                    wall.innerHTML = data.messages.map(m => formatMessage(m)).join('');
                });
        }
        setInterval(refreshWall, 3000);
        refreshWall(); // Initial format
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1502)