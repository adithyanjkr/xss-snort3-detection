import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

BASE_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JKRsec - Community Board</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            padding: 40px;
            max-width: 600px;
            margin: 0 auto;
        }
        h2 { color: #ffffff; border-bottom: 2px solid #333; padding-bottom: 10px; }
        .form-group { margin-top: 20px; }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            background: #1e1e1e;
            border: 1px solid #444;
            color: #fff;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
        }
        input[type="submit"] {
            margin-top: 10px;
            background: #007acc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        input[type="submit"]:hover { background: #005999; }
        .output-box {
            margin-top: 30px;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 6px;
            border-left: 4px solid #007acc;
            min-height: 50px;
        }
    </style>
</head>
<body>

    <h2>XSS-Test</h2>
    <p>Leave your feedback or ideas below.</p>
    
    <div class="form-group">
        <form method="POST" action="/">
            <input type="text" name="user_payload" placeholder="Type your comment here..." required>
            <input type="submit" value="Post Comment">
        </form>
    </div>
    
    <h3>Latest Activity:</h3>
    <div class="output-box">
        {{ rendered_output | safe }}
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    display_text = "No comments posted yet."
    
    if request.method == 'POST':
        raw_input = request.form.get('user_payload', '').strip()
        
        if raw_input:
            display_text = raw_input
            
    return render_template_string(BASE_LAYOUT, rendered_output=display_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
