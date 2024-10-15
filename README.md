# Transaction Explorer Automation Project

## Overview
This project automates the testing of the transaction explorer on Blockstream.info for a specific Bitcoin block. It validates the transaction heading and extracts transaction hashes based on specified criteria.

## Prerequisites
- Python 3.6 or higher
- Chrome WebDriver

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd transaction-explorer-automation-project
   ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Running Tests**
     ```bash
     pytest tests/test_block_transactions.py
    ```

