# ClamAV Wrapper with Generative AI Integration

This repository provides a Python wrapper script for ClamAV that captures the scan report and sends it to the Gemini API using the Generative AI SDK.

## Features

- Run ClamAV scans
- Capture ClamAV scan reports
- Send scan reports to the Gemini API using the Generative AI SDK
- Display the response from the Generative AI API

## Prerequisites

- Python 3.x
- ClamAV installed
- Generative AI SDK
- Gemini API key

## Installation

1. **Install ClamAV:**
   Follow the instructions on the [ClamAV website](https://www.clamav.net/documents/installing-clamav).

2. **Install the Generative AI SDK:**
   ```sh
   pip install generative-ai-sdk
   ```
   
3. **Clone the Repository:**
   ```sh
   git clone https://github.com/quangbao368/clamav-gemini-wrapper
   cd clamav-gemini-wrapper
   ```
   
## Configuration

Replace the placeholder API key in **wrapper_script.py** with your actual Gemini API key:
```python
GEMINI_API_KEY = "your_gemini_api_key_here"
```

## Usage
1. **Make the script executable:**
```sh
chmod +x wrapper_script.py
```

2. **Run the script:**
```sh
./wrapper_script.py
````

