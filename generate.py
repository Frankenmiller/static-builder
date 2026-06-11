import os
from datetime import datetime

def build_site():
    project_name = "Operational Dashboard"
    status = "Active"
    modules = ["Git Workspace", "Python Engine", "GitHub Pages Deployment"]

    # this is to get the current timestamp for the build
    current_time = datetime.now().strftime("%D %H:%M:%S")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: #0f172a; color: #e2e8f0; padding: 2rem; max-width: 600px; margin: auto; }}
        h1 {{ color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 0.5rem; }}
        .status {{ background: #1e293b; padding: 0.75rem; border-radius: 6px; margin: 1rem 0; border-left: 4px solid #10b981; }}
        ul {{ padding-left: 1.2rem; line-height: 1.6; }}
    </style>
</head>
<body>
    <h1>{project_name}</h1>
    <div class="status"><strong>Status:</strong> {status}</div>
    <div class="timestamp">Last compiled: {current_time}</div>
    <h3>Core Modules:</h3>
    <ul>
        {"".join(f"<li>{mod}</li>" for mod in modules)}
    </ul>
</body>
</html>
"""
    
    with open("index.html", "w") as f:
        f.write(html_content)
    print("🚀 index.html generated successfully 🚀!!!")

if __name__ == "__main__":
    build_site()