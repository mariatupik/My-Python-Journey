# Python Unit Testing with Pytest

This project demonstrates professional software testing techniques using the `pytest` framework. It features a robust `Form` class with integrated URL validation and a comprehensive suite of automated tests.

---

##  Key Features
* **Object-Oriented Logic:** A `Form` class that handles user credentials and dynamic URL assignment.
* **Network Integration:** Uses the `requests` library to validate website availability with custom `User-Agent` headers.
* **Automated Testing:** * Verification of object initialization with varying parameter counts.
    * Validation of default `None` states for optional attributes.
    * Real-world URL testing (checking for successful `200 OK` responses vs. connection failures).
* **Exception Handling:** Robust `try-except` blocks to manage network errors without crashing the application.

---

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Testing Framework:** `pytest`
* **Network Library:** `requests`

---

##  How to Run Tests
1. Install dependencies:
   ```bash
   pip install pytest requests
   ```
2. Run the test suite:
   ```bash
   pytest test_form.py
   ```

---
*Developed to demonstrate proficiency in Test-Driven Development (TDD) principles.*