#!/bin/bash
python3 generate.py && \
git add generate.py index.html && \
git commit -m "deploy: automatic build at $(date +'%Y-%m-%d %H:%M:%S')" && \
git push
