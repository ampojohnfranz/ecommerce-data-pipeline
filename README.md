# E-Commerce Data Pipeline & API Integration

## Overview
This project simulates a backend data architecture for an e-commerce platform. It processes raw, unstructured order data (simulating an Amazon SP-API JSON payload), structures it into a relational SQL database, and serves it to frontend dashboards via a live REST API built with FastAPI.

## Tech Stack
* **Language:** Python 3
* **Framework:** FastAPI, Uvicorn
* **Database:** SQLite
* **Analytics/BI:** Power BI, DAX

## Features Built
1. **Data Ingestion (`import_data.py`):** Parses raw JSON payloads and constructs a structured SQL database schema, matching external data structures to internal storage requirements.
2. **REST API (`api.py`):** A live web server handling full CRUD operations for inventory management:
   * `GET /orders`: Fetches live inventory data.
   * `POST /orders`: Inserts new customer orders.
   * `PUT /orders/{order_id}/status`: Updates fulfillment status (e.g., Pending to Shipped).
   * `DELETE /orders/{order_id}`: Removes canceled or flagged orders.
3. **Business Intelligence:** Live connection between the Python backend and Power BI using Power Query, utilizing DAX measures to track real-time KPIs like Total Revenue and Average Order Value.

## How to Run Locally
1. Clone the repository.
2. Run `python import_data.py` to initialize the database.
3. Run `uvicorn api:app --reload` to start the local server.
4. Access the interactive Swagger UI at `http://127.0.0.1:8000/docs` to test endpoints.
