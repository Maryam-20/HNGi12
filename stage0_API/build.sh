ECHO is on.
#!/usr/bin/env bash
# Exit on error
chmod +x build.sh

set -o errexit

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install dependencies
# pip install -r requirements.txt

pip install --no-cache-dir --force-reinstall -r stage0_API/requirements.txt

# Run database migrations
python manage.py migrate --noinput

echo "Build complete!"