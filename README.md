# ScrapFlask - API Wrapper for Scrappy

ScrapFlask provides an intuitive and user-friendly API interface for the powerful Scrappy command-line tool. This Flask-based web application enables users to trigger Scrappy's functionality with ease, leveraging HTTP requests to control property data scraping and report generation.

---

## Overview
ScrapFlask is designed for individuals or teams who want to simplify and automate property data scraping workflows. By wrapping Scrappy's capabilities in a Flask application, ScrapFlask allows you to:

- **Send property owner queries via HTTP POST requests**.
- **Receive structured JSON responses** with scraping results.
- **Handle fuzzy match confirmations interactively or programmatically**.

With ScrapFlask, you can integrate Scrappy into your existing systems or workflows without manually running CLI commands.

---

## Features
### 1. Simplified HTTP API
ScrapFlask exposes a clean API for interacting with Scrappy:

- `/`: Health check endpoint that ensures the server is running.
- `/scrape`: Main scraping endpoint for submitting owner queries.
- `/confirm`: Endpoint for handling fuzzy match confirmations during the scraping process.

### 2. Dynamic JSON Output
ScrapFlask converts Scrappy's raw output into structured JSON, making it easy to integrate with modern applications.

### 3. Real-Time Match Confirmation
When Scrappy encounters multiple potential matches, ScrapFlask pauses the process and emits a JSON payload with the options for user confirmation.

---

## Installation
### Prerequisites
- **Python 3.8+** installed on your system.
- **Scrappy** installed and operational. ScrapFlask depends on Scrappy for core functionality.
- **Flask** Python package installed.

### Steps
1. Clone the ScrapFlask repository:
   ```bash
   git clone <your-repository-url>
   cd scrapflask
   ```

2. Ensure Scrappy is available:
   - Place Scrappy in a directory accessible from ScrapFlask.
   - Confirm Scrappy's functionality by running:
     ```bash
     python scrappy/main.py
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. The server will start at `http://127.0.0.1:5000`.

---

## Usage
### Health Check
To ensure ScrapFlask is running, send a GET request to the root endpoint:

```bash
curl http://127.0.0.1:5000/
```
Expected response:
```json
{
    "message": "Welcome to ScrapFlask API!"
}
```

### Submit a Scraping Request
Send a POST request to `/scrape` with the list of owner names in JSON format:

```bash
curl -X POST http://127.0.0.1:5000/scrape \
-H "Content-Type: application/json" \
-d '{"owners": ["101 Hart Lane"]}'
```

Expected response:
```json
{
    "message": "Scraping completed!",
    "data": {
        "excel_file": "path/to/excel_file.xlsx",
        "pdf_folder": "path/to/pdf/folder",
        "property_data": [ ... ],
        "errors": []
    }
}
```

### Handle Match Confirmations
If Scrappy encounters multiple matches, ScrapFlask will emit a JSON payload requiring user confirmation. For example:

```json
{
    "confirmation_id": "unique-id",
    "error": "Confirmation required",
    "message": "Multiple matches found. Please confirm the best match.",
    "options": [
        "101 Hart Lane, Nashville, TN",
        "102 Hart Ln, Nashville, TN"
    ]
}
```

Respond with your confirmation via the `/confirm` endpoint:

```bash
curl -X POST http://127.0.0.1:5000/confirm \
-H "Content-Type: application/json" \
-d '{"owner": "101 Hart Lane", "match": "101 Hart Lane, Nashville, TN", "confirmation": "yes"}'
```

---

## Technical Details
### Architecture
ScrapFlask wraps Scrappy’s Python CLI in a subprocess. It captures its output, parses it into JSON, and handles any intermediate confirmations via environment variables or external APIs.

### Logging
ScrapFlask includes detailed logging to assist with debugging and monitoring. Logs are printed to the console and include:
- Incoming requests
- Environment variable changes
- Scrappy subprocess results

### Temporary State Management
For user confirmations, ScrapFlask leverages a temporary in-memory store to track confirmation IDs and associated options.

---

## Roadmap
### Immediate Goals
- **Improve JSON output styling**: Ensure CLI outputs are clean and human-readable.
- **Enhance error handling**: Make error responses more descriptive.
- **Dynamic configuration**: Add support for user-defined settings via a configuration file.

### Long-Term Goals
- **Comprehensive UI**: Build a web-based wizard for submitting requests and reviewing results.
- **Token-based authentication**: Secure API endpoints for multi-user environments.
- **Asynchronous processing**: Allow users to submit requests and retrieve results later.

---

## Contributions
Contributions are welcome! If you have ideas for improving ScrapFlask, feel free to submit issues or pull requests on GitHub.

---

## Contact
Developed by Kendrick Isaac Reed Kirk.
