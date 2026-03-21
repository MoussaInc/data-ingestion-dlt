# 📚 Open Library Data Pipeline

Pipeline d'ingestion de données avec **dlt** : Open Library API → DuckDB

## 🚀 Quick Start
```bash
# Installation
uv sync

# Exécution
uv run python main.py
```

## 📊 Explorer les données
```python
import duckdb

con = duckdb.connect("open_library.duckdb")
books = con.execute("SELECT * FROM library.books LIMIT 10").fetchdf()
print(books)
```

## 🛠️ Stack

- **dlt** - ETL framework
- **DuckDB** - Analytical database
- **uv** - Python package manager

## 📁 Structure
```
├── main.py              # Point d'entrée
├── pipeline.py          # Logique du pipeline
├── dlt_pipeline.ipynb   # Exploration notebook
├── pyproject.toml       # Configuration uv
└── open_library.duckdb  # Base de données
```

## 🔍 Usage
```bash
# Requête personnalisée
uv run python main.py --query "machine learning"

# Spécifier la base
uv run python main.py --db custom.duckdb

# Notebook
uv run jupyter notebook dlt_pipeline.ipynb
```