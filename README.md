# ScrapFlask - API Wrapper for Scrappy

ScrapFlask is a lightweight Flask-based API wrapper designed to extend the functionality of Scrappy, a command-line tool for property data scraping. It provides a seamless way to integrate Scrappy into external workflows by offering endpoints for triggering Scrappy operations and handling data programmatically.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
    - [RESTful Endpoints](#1-restful-endpoints)
    - [Seamless Integration with Scrappy](#2-seamless-integration-with-scrappy)
    - [Dynamic Outputs](#3-dynamic-outputs)
3. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
4. [Usage](#usage)
    - [Starting the Server](#starting-the-server)
    - [API Endpoints](#api-endpoints)
        - [Health Check](#1-health-check)
        - [Trigger Scraping](#2-trigger-scraping)
        - [Handle Confirmations](#3-handle-confirmations)
5. [Debugging and Logging](#debugging-and-logging)
6. [Roadmap](#roadmap)
    - [Immediate Goals](#immediate-goals)
    - [Long-Term Goals](#long-term-goals)
7. [Contributions](#contributions)
8. [Contact](#contact)

---

## Overview

ScrapFlask bridges the gap between command-line tools and modern applications by exposing Scrappy’s core functionality through a simple REST API. This allows:
- **Developers**: To integrate property scraping features into web applications or larger systems.
- **Automation**: For workflows requiring programmatic triggers and responses.
- **Custom User Interfaces**: To build GUIs that leverage Scrappy’s backend capabilities.

Key Features:
- **API-Driven Integration**: Trigger Scrappy operations and fetch results via HTTP.
- **Fuzzy Match Handling**: Manage match confirmations through external inputs.
- **JSON Responses**: Receive structured data for seamless integration into modern applications.

---

## Features

### 1. RESTful Endpoints
- **Trigger Scraping**: Provide owner names as input and receive detailed property data in JSON.
- **Handle Confirmations**: Manage fuzzy match confirmations programmatically.

### 2. Seamless Integration with Scrappy
ScrapFlask directly interfaces with Scrappy’s core functions to:
- Collect and organize property data.
- Download related PDFs.
- Handle match logic interactively or via API.

### 3. Dynamic Outputs
Receive structured JSON responses containing:
- Scraped property data.
- File paths for downloaded PDFs.
- Logs for debugging and error tracking.

---

## Installation

### Prerequisites
- **Python 3.8+** installed.
- Scrappy installed and configured.

### Installation Steps
1. Clone the ScrapFlask repository:
   ```bash
   git clone <repository-url>
   cd scrapflask
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation:
   ```bash
   python app.py
   ```

---

## Usage

### Starting the Server
Run the ScrapFlask server:
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000/` by default.

### API Endpoints

#### 1. Health Check
**Endpoint**: `/`

**Method**: `GET`

**Description**: Verifies that the ScrapFlask server is running.

**Response**:
```json
{
  "message": "Welcome to ScrapFlask API!"
}
```

#### 2. Trigger Scraping
**Endpoint**: `/scrape`

**Method**: `POST`

**Description**: Triggers Scrappy to scrape data for the provided owner names.

**Request Body**:
```json
{
  "owners": ["Owner Name 1", "Owner Name 2"]
}
```

**Response (Success)**:
```json
{
  "message": "Scraping completed!",
  "data": {
    "excel_file": "outputs/output_davidsonco.xlsx",
    "pdf_folder": "outputs/pdfs",
    "property_data": [
      {
        "Input Name": "Owner Name 1",
        "Matched Name": "OWNER NAME, LLC",
        "Address": "123 Main St",
        "Parcel": "001",
        "Improvement Value": "$100,000",
        "Land Value": "$50,000",
        "Tax Rate": "3.2%"
      }
    ]
  }
}
```

**Response (Confirmation Required)**:
```json
{
  "confirmation_id": "1234-5678-90ab-cdef",
  "error": "Confirmation required",
  "message": "Multiple matches found. Please confirm the best match.",
  "options": [
    "Match Option 1",
    "Match Option 2"
  ]
}
```

#### 3. Handle Confirmations
**Endpoint**: `/confirm`

**Method**: `POST`

**Description**: Resolves fuzzy match confirmations.

**Request Body**:
```json
{
  "confirmation_id": "1234-5678-90ab-cdef",
  "selection": "Match Option 1"
}
```

**Response (Success)**:
```json
{
  "message": "Confirmation received. Resuming scraping."
}
```

---

## Debugging and Logging

ScrapFlask logs API activity, errors, and integration details with Scrappy. Logs are written to the console and a file (`logs/scrapflask.log`) for debugging purposes.

### Debugging Tips
- **API Not Responding**:
  - Ensure ScrapFlask is running on the expected port.
  - Check logs for errors.

- **500 Internal Server Errors**:
  - Verify Scrappy is installed and accessible.
  - Check the target website’s availability.

---

## Roadmap

### Immediate Goals
1. Improve error handling for invalid inputs.
2. Add more robust unit tests for API endpoints.
3. Refine logging for better debugging.

### Long-Term Goals
- **Customizable Inputs**: Support additional filters for property searches.
- **Enhanced Reporting**: Allow users to define custom report templates.
- **Authentication**: Secure API endpoints with token-based authentication.

---

## Contributions
Contributions are welcome! If you have ideas for new features or ways to improve ScrapFlask, feel free to submit an issue or a pull request.

---

## Contact

Developed by Kendrick Isaac Reed Kirk. For inquiries, open an issue on GitHub or contact directly.
