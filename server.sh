#!/bin/bash

# Exit if anything fails
set -e

echo "🚀 Connecting to remote server..."

ssh -t -p 1980 prakash2@95.217.203.22 '
  set -e
  # Activate virtual environment and change to project directory
  source /home3/prakash2/virtualenv/meguro.com.np/3.11/bin/activate && cd /home3/prakash2/meguro.com.np
  echo "✅ Environment ready. You are now inside the server shell."
  exec bash
'

echo "🔚 SSH session closed."
