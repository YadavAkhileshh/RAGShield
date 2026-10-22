from pathlib import Path
from app.services.ingestion import load_file, chunk_documents
from app.rag.vectorstore import add_documents
from app.core.config import get_settings

settings = get_settings()
kb_dir = Path(settings.sample_kb_dir)

for path in kb_dir.glob("*"):
    if path.suffix in {".md", ".txt", ".pdf", ".docx"}:
        docs   = load_file(path)
        chunks = chunk_documents(docs)
        ids    = add_documents(chunks)
        print(f"{path.name}: {len(chunks)} chunks indexed")