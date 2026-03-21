# 📚 Open Library Data Pipeline

Pipeline d'ingestion de données avec **dlt** : extrait des livres depuis l'API Open Library et les charge dans DuckDB.

## 🚀 Quick Start
```bash
# Installer les dépendances et exécuter le pipeline
uv sync
uv run python main.py
```

## 📊 Résultat

Le pipeline charge automatiquement :
- Livres sur **data engineering**
- Livres sur **harry potter**

Dans la base `open_library.duckdb` avec le schéma `library`.

## 🔍 Explorer les données
```python
import duckdb

con = duckdb.connect("open_library.duckdb")

# Statistiques
stats = con.execute("SELECT COUNT(*) FROM library.books").fetchdf()
print(stats)

# Top auteurs
authors = con.execute("""
    SELECT value as author, COUNT(*) as books
    FROM library.books__author_name
    GROUP BY author
    ORDER BY books DESC
    LIMIT 10
""").fetchdf()
print(authors)

con.close()
```

## 📁 Structure
```
├── main.py              # Point d'entrée du pipeline
├── pipeline.py          # Logique dlt (source, run, analyze)
├── dlt_pipeline.ipynb   # Notebook d'exploration
├── pyproject.toml       # Configuration uv
└── open_library.duckdb  # Base de données (généré)
```

## 📈 Schéma des données

dlt crée automatiquement :

- `library.books` - Table principale des livres
- `library.books__author_name` - Table des auteurs (normalisée)
- `library.books__subject` - Table des sujets (normalisée)
- `library.books__language` - Table des langues (normalisée)

## ⚙️ Personnalisation

Modifiez les requêtes dans `main.py` :
```python
queries = ["data engineering", "harry potter"]  # ← Changez ici
```