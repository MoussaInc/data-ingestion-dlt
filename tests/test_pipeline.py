
import duckdb
from pipeline import run_pipeline, analyze_data


def test_run_pipeline():
    pipeline = run_pipeline(query="python", max_results=10)
    assert pipeline is not None


def test_analyze_data():
    stats = analyze_data()
    assert stats['total_books'] > 0
    assert stats['unique_titles'] > 0


def test_database_structure():
    """Test that database has correct structure"""
    con = duckdb.connect("open_library.duckdb")
    
    # Check table exists
    tables = con.execute("SHOW TABLES FROM library").fetchall()
    table_names = [t[0] for t in tables]
    assert 'books' in table_names
    
    # Check books table has data
    count = con.execute("SELECT COUNT(*) FROM library.books").fetchone()[0]
    assert count > 0
    
    con.close()