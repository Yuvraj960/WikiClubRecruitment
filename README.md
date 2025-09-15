
# 📦 Stock Management Module

A **Python package** for managing product stock.  
It provides utilities to calculate total stock value, normalize product data, and identify out-of-stock items.  

This project refactors the original `main.py` into a **modular, reusable, and testable package**.

---

## 📂 Project Structure

```
project-root/
│── main.py                 # Entry point script
│── stock/                  # Reusable stock module
│   │── **init**.py
│   │── models.py           # Type definitions
│   │── utils.py            # Helper functions
│   │── processor.py        # Business logic
│   │── data.py             # Example dataset
│── tests/                  # Unit tests
│   │── **init**.py
│   │── test\_stock.py
│── .gitignore
│── README.md
````

---

## ⚙️ Requirements

- Python **3.10+**
- `pytest` for testing

Install dependencies:

```bash
pip install -r requirements.txt
````
---

## ▶️ Running the Project

To run the stock analysis with sample data:

```bash
python main.py
```

**Example Output:**

```
Total value of all stock: 1780.47
Out of stock products: ['p002', 'p005', 'p006']
```

---

## 🧪 Running Tests

We use **pytest** for testing.

Run all tests:

```bash
pytest -v
```

Expected output:

```
collected 5 items

tests/test_stock.py::test_normal_case PASSED
tests/test_string_price PASSED
tests/test_invalid_price PASSED
tests/test_negative_quantity PASSED
tests/test_out_of_stock PASSED
```

---

## 📝 Tasks Completed ✅

* [x] Fix the bug in `main.py`.
* [x] Make it use Python’s type hinting feature.
* [x] Place it in a valid module named `stock`.
* [x] Add an appropriate `.gitignore` file.
* [x] Write **5 test cases minimum** (pytest).
* [x] Make a well formatted professional pull request.
* [x] Well documented code.

---

## 🤝 Contribution Guidelines

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit changes with meaningful messages (`git commit -m "Added feature XYZ"`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request with:

   * Clear title
   * Description of changes
   * Linked issue (if applicable)

---

## 📜 License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for more information.
