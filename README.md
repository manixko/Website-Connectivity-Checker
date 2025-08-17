# 🌐 Website Connectivity Checker

A simple Python script to check if a website is reachable or not.  
It automatically fixes the URL format (adds `https://www.` if missing) and then sends a request to test connectivity.

---

## 🚀 Features
- Normalizes URLs to a proper format (`https://www.example.com`)
- Sends an HTTP request with a browser-like **User-Agent**
- Quick response with `connect` or `not connect`

---

## 📦 Requirements
- Python 3.x
- [requests](https://pypi.org/project/requests/) library  

Install dependencies with:
```bash
python install -r requirements.txt
```

---

## 🔧 How to Use

1. Clone or download this repository.
2. Install the required packages using the command above.
3. Run the with:
```bash
python wcc.py -u example.com
```

