import os
from datetime import datetime

def build_site():
    project_name = "Operational Dashboard"
    status = "Active"
    modules = ["Git Workspace", "Python Engine", "GitHub Pages Deployment"]

    nft_collection = [
        "https://g.irys.xyz/6nRvg2dRTFpRNeq7PYDya8jUdj3SsFQE185Ada92riZP?ext=png",
        "https://g.irys.xyz/HPf5wprcVD55351S56PdZoyEo7B1ottKkyaxjcxdzA7q?ext=png",
        "https://arweave.net/bgVJw-s_vWHSKYGCKMEmtgUxTiLTqX_DgIX8w5_M3_4?ext=png",
        "https://g.irys.xyz/6nRvg2dRTFpRNeq7PYDya8jUdj3SsFQE185Ada92riZP?ext=png"
    ]

    nft_html_grid = ""
    for index, url in enumerate(nft_collection, 1):
        nft_html_grid += f"""
        <div class="nft-card">
            <img src="{url}" alt="cNFT #{index}">
            <div class="nft-info">Asset #{index:03d}</div>            
        </div>
        """

    # this is to get the current timestamp for the build
    current_time = datetime.now().strftime("%D %H:%M:%S")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="stylesheet" href="style.css" >
</head>
<body>
    <h1>{project_name}</h1>
    <div class="status"><strong>Status:</strong> {status}</div>
    <div class="timestamp">Last compiled: {current_time}</div>
    <h3>Core Modules:</h3>
    <ul>
        {"".join(f"<li>{mod}</li>" for mod in modules)}
    </ul>
    <h3 class="gallery-title">Asset Vault (Square Specs)</h3>
    <div class="nft-grid">
        {nft_html_grid}
    </div>
</body>
</html>
"""
    
    with open("index.html", "w") as f:
        f.write(html_content)
    print(current_time, "🚀 index.html generated successfully 🚀!!!")
    print(current_time, "Go take a look at your index.html")

if __name__ == "__main__":
    build_site()