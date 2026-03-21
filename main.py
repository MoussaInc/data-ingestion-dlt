"""
Open Library Data Pipeline
"""

from pipeline import run_pipeline, analyze_data


def main():
    # Sujets à chercher
    queries = ["data engineering", "harry potter"]
    
    print("🚀 Open Library Pipeline\n")
    
    # Charger chaque sujet
    for query in queries:
        print(f"📚 Loading: {query}")
        run_pipeline(query=query)
    
    # Statistiques finales
    stats = analyze_data()
    
    print("\n" + "="*40)
    print("✅ Completed!")
    print("="*40)
    print(f"📚 Total books: {stats['total_books']}")
    print(f"📖 Unique titles: {stats['unique_titles']}")
    print(f"📅 Years: {stats['oldest_year']} - {stats['newest_year']}")


if __name__ == "__main__":
    main()