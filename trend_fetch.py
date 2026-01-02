name: Google Trends Game Fetcher

on:
  workflow_dispatch:
  schedule:
    - cron: "0 */6 * * *"   # 6 saatte bir (istersen değiştiririz)

jobs:
  fetch:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run trend fetcher
        run: python trend_fetch.py
