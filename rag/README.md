# RAG-ready output

این پوشه مرز میان پروژه ترجمه و **Book Ingestion فاز دوم RAG Finance** است.

## اصل معماری

فایل DOCX انگلیسی، منبع خام و تغییرناپذیر است. ترجمه فارسی یک لایه مشتق‌شده و قابل ردیابی است. در پروژه اصلی RAG، فایل خام باید جداگانه در `raw` نگهداری شود و این خروجی فارسی وارد مرحله Book Ingestion شود.

## فایل‌ها

- `book_manifest.json` — ساختار کتاب، ترتیب فصل‌ها و بازه صفحات منبع.
- `../scripts/build_rag_documents.py` — تولید رکوردهای استاندارد فصل‌محور با شناسه‌های قطعی و hash متن.
- `generated/book_documents.jsonl` — خروجی تولیدشده توسط اسکریپت؛ بهتر است Generated Data تلقی شود.

## اجرا

```bash
python scripts/build_rag_documents.py
```

## چرا فصل‌محور؟

در این مخزن هنوز Chunking نهایی انجام نمی‌شود. مطابق معماری فاز دوم، ابتدا Book Ingestion باید متن کامل، ساختار فصل و provenance را حفظ کند. Chunking تخصصی کتاب بعداً در RAG Finance و همراه با Website + Video انجام می‌شود.

هر رکورد فصل‌محور شامل این داده‌های مهم است:

- `document_id` قطعی
- `source_id`
- `source_type = book`
- عنوان و نویسنده
- `chapter` و `chapter_id`
- `page_start` و `page_end` منبع انگلیسی
- متن فارسی کامل همان بخش
- `processed_content_hash`
- provenance ترجمه

## Citation آینده

ساختار صفحه‌ای حفظ شده تا Chunker کتاب در پروژه RAG بتواند Citationهایی از جنس زیر ایجاد کند:

```text
پول و من
فصل ۱۳ — اصول سرمایه‌گذاری مؤثر
صفحات منبع 40–41
```

برای Citation دقیق‌تر در سطح صفحه، مرحله بعد می‌تواند alignment پاراگراف‌به‌صفحه را روی DOCX/PDF خام انجام دهد؛ بدون تغییر این ترجمه.
