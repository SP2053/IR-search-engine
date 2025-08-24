# app/main.py
import sys, os, math
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search_engine import SearchEngine, load_publications

ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = ROOT / "frontend" / "index.html"

# Let the loader use its defaults:
# primary = data/publications.json, fallback = data/publications_detailed.json
all_publications = load_publications()
search_system = SearchEngine(all_publications)

app = FastAPI(
    title="IRxRahul Search Engine",
    description="A vertical search engine for Coventry University publications.",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(content=INDEX_HTML.read_text(encoding="utf-8"), status_code=200)

@app.get("/publications/")
def get_all_publications(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1)):
    start, end = (page - 1) * page_size, page * page_size
    total = len(all_publications)
    return {
        "page": page,
        "page_size": page_size,
        "total_pages": math.ceil(total / page_size),
        "total_publications": total,
        "publications": all_publications[start:end],
    }

@app.get("/search/")
def search_publications(query: str = Query(..., min_length=2)):
    results = search_system.search(query)
    return {"query": query, "results_count": len(results), "results": results}
