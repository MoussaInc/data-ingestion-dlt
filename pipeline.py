"""
Pipeline logic for Open Library data ingestion
"""

import dlt
from dlt.sources.rest_api import rest_api_source


def openlibrary_source(query: str, max_results: int = 100):
    """Configure Open Library API source"""
    return rest_api_source({
        "client": {
            "base_url": "https://openlibrary.org",
        },
        "resource_defaults": {
            "primary_key": "key",
            "write_disposition": "append",
        },
        "resources": [
            {
                "name": "books",
                "endpoint": {
                    "path": "search.json",
                    "params": {
                        "q": query,
                        "limit": max_results,
                    },
                    "data_selector": "docs",
                    "paginator": {
                        "type": "offset",
                        "limit": 100,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "numFound",
                    },
                },
            },
        ],
    })


def run_pipeline(query: str, max_results: int = 100):
    """Run the dlt pipeline"""
    # Create pipeline
    pipeline = dlt.pipeline(
        pipeline_name="open_library",
        destination="duckdb",
        dataset_name="library",
        dev_mode=False
    )
    
    # Load data
    pipeline.run(openlibrary_source(query=query, max_results=max_results))
    
    return pipeline


def analyze_data(db_path: str = "open_library.duckdb"):
    """Analyze loaded data"""
    import duckdb
    
    con = duckdb.connect(db_path)
    
    stats = con.execute("""
        SELECT 
            COUNT(*) as total_books,
            COUNT(DISTINCT title) as unique_titles,
            MIN(first_publish_year) as oldest_year,
            MAX(first_publish_year) as newest_year
        FROM library.books
        WHERE first_publish_year IS NOT NULL
    """).fetchdf().to_dict('records')[0]
    
    con.close()
    
    return stats