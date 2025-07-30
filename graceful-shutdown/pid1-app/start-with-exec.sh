#!/bin/bash

echo "[INIT] Doing some setup..."

# ✅ This ensures python3 becomes PID 1
exec python3 app.py
