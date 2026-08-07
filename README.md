# Money and Me — Persian Translation

ترجمه، ویرایش و آماده‌سازی نسخه فارسی کتاب **Money and Me: A Personal Journey to Financial Literacy** نوشته **Komeil Roudi**.

## هدف مخزن

این مخزن برای چهار خروجی اصلی ساخته شده است:

1. ترجمه کامل و وفادار کتاب از انگلیسی به فارسی.
2. ویراستاری حرفه‌ای و یکدست‌سازی اصطلاحات مالی.
3. حفظ ساختار کتاب، فصل‌ها، جدول‌ها، اعداد و قابلیت ردیابی به منبع.
4. تولید داده ساختاریافته مناسب برای Book Ingestion در فاز دوم پروژه RAG Finance.

## اصول ترجمه

- هیچ بخش محتوایی عمداً خلاصه، حذف یا بازنویسی معنایی نمی‌شود.
- اعداد و ادعاهای منبع بدون اصلاح خاموش ترجمه می‌شوند؛ ابهام‌های احتمالی منبع در یادداشت‌های جداگانه ثبت می‌شوند.
- اصطلاحات مالی براساس واژه‌نامه ثابت ترجمه می‌شوند.
- نثر فارسی باید روان، کتابی و طبیعی باشد، نه ترجمه کلمه‌به‌کلمه.
- ساختار فصل‌ها و امکان ارجاع به صفحات/بخش‌های منبع حفظ می‌شود.

## ساختار

```text
book/
  metadata.json
  fa/
    00_front_matter.md
    01_financial_literacy.md
    02_unit_01.md
    ...
    18_unit_17.md

docs/
  translation_policy.md
  financial_glossary.md
  source_fidelity_notes.md
  translation_qa_report.md

rag/
  book_manifest.json
  README.md
  generated/
    book_documents.jsonl

scripts/
  build_rag_documents.py
```

## وضعیت

```text
Translation: COMPLETED
Persian Editorial Pass: COMPLETED
Terminology QA: PASS
Source Fidelity QA: PASS
DOCX RTL/BiDi Visual QA: PASS
RAG Phase 2 Handoff: READY
```

ترجمه کامل ۱۷ فصل به همراه بخش مقدماتی آماده شده و ساختار فصل/صفحه برای استفاده در Book Ingestion فاز دوم حفظ شده است. Chunking نهایی عمداً به پروژه اصلی RAG Finance واگذار شده تا پس از آماده‌شدن Website + Book + Video انجام شود.
