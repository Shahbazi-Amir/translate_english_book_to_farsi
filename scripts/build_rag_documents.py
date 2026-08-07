from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PROJECT_ROOT / "rag" / "book_manifest.json"
OUTPUT_PATH = PROJECT_ROOT / "rag" / "generated" / "book_documents.jsonl"


def stable_id(*parts: str) -> str:
    payload = "|".join(parts).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def clean_markdown(text: str) -> str:
    text = re.sub(r"</?div[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    source_id = manifest["book_id"]
    raw_content_hash = manifest["source_sha256"]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as output_file:
        for item in manifest["documents"]:
            source_path = PROJECT_ROOT / item["file"]
            markdown_text = source_path.read_text(encoding="utf-8")
            text = clean_markdown(markdown_text)
            processed_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            chapter_id = item["chapter_id"]

            record = {
                "schema_version": "1.0",
                "document_id": stable_id("book", source_id, chapter_id),
                "source_id": source_id,
                "source_type": "book",
                "title": manifest["title_fa"],
                "title_en": manifest["title_en"],
                "author": manifest["author"],
                "publisher": None,
                "knowledge_owner": manifest["author"],
                "category": ["financial_literacy"],
                "tags": ["book", "financial_literacy", "persian_translation"],
                "language": "fa",
                "source_language": manifest["source_language"],
                "translation_language": manifest["translation_language"],
                "url": "",
                "canonical_url": "",
                "file_name": manifest["source_filename"],
                "chapter": item["title_fa"],
                "chapter_id": chapter_id,
                "section": "",
                "page": None,
                "page_start": item["page_start"],
                "page_end": item["page_end"],
                "timestamp_start": None,
                "timestamp_end": None,
                "text": text,
                "raw_content_hash": raw_content_hash,
                "processed_content_hash": processed_hash,
                "source_revision": "user-provided-docx",
                "version": 1,
                "published_at": None,
                "updated_at": None,
                "crawled_at": None,
                "ingested_at": None,
                "pipeline_version": "book-translation-v1",
                "extractor_version": "markdown-chapter-v1",
                "rights_status": "user_provided_source; no additional rights metadata supplied",
                "translation_provenance": {
                    "type": "english_to_persian",
                    "fidelity_policy": "preserve source meaning, structure, numbers and claims",
                    "source_file": manifest["source_filename"],
                    "source_sha256": raw_content_hash,
                },
            }
            output_file.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(manifest['documents'])} documents to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
