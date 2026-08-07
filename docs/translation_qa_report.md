# گزارش کنترل کیفیت ترجمه فارسی

## وضعیت نهایی

```text
Translation Coverage: PASS
Terminology QA: PASS
Source Fidelity QA: PASS
DOCX Technical QA: PASS
DOCX RTL/BiDi QA: PASS
DOCX Visual QA: PASS
RAG Handoff Structure: PASS
RAG Document Builder Structural Test: PASS
```

## منبع

- عنوان: `Money and Me`
- نویسنده: `Komeil Roudi`
- فایل: `Money and ME By Komeil Roudi 040214.docx`
- SHA-256: `95cefc299f2c1bea76073e9a327d718601a4d8f651ae3060c3daa12851c828e5`
- صفحات منبع: 53
- فصل‌های اصلی: 17
- پاراگراف‌های منبع: 341
- پاراگراف‌های غیرخالی: 232
- جدول‌ها: 4
- نمودارهای جاسازی‌شده: 4

## پوشش ترجمه

ترجمه شامل موارد زیر است:

- جلد و اطلاعات اولیه
- بخش مقدماتی سواد مالی
- فصل‌های 1 تا 17
- تمام جدول‌های متنی منبع
- اعداد و نسبت‌های مالی موجود در منبع
- توضیح و حفظ چهار نمودار فصل 13
- ضرب‌المثل‌ها و جمله‌های پایانی فصل‌ها

صفحات 6 و 20 فایل منبع فاقد متن محتوایی‌اند و در Manifest به‌عنوان صفحات خالی ثبت شده‌اند.

## وفاداری به منبع

موارد مبهم یا ناسازگار منبع به‌صورت خاموش اصلاح نشده‌اند و در `source_fidelity_notes.md` ثبت شده‌اند. نمونه‌ها:

- برچسب مبهم `Money in Money` در نمودار صفحه 5
- چارچوب جنسیتی الگوهای خرید در فصل 4
- نرخ بازده ماهانه 20 درصد و اعداد مثال فصل 13
- جدول راهبردهای ریسک فصل 14
- ناسازگاری «شش عامل» در برابر هفت مورد فهرست‌شده در فصل 9

## اصطلاحات

واژه‌های کلیدی مالی با `financial_glossary.md` یکدست شده‌اند؛ از جمله:

- Financial Literacy → سواد مالی
- Financial Capability → توانمندی مالی
- Financial Security → امنیت مالی
- Financial Freedom → آزادی مالی
- Compound Interest → بهره مرکب
- Bounded Rationality → عقلانیت محدود
- Sunk Cost Fallacy → مغالطه هزینه غرق‌شده

## DOCX فارسی

نسخه نهایی DOCX با RTL واقعی و مدیریت BiDi ساخته شد.

کنترل فنی:

- فایل DOCX سالم و قابل بازشدن
- 1 Section
- 4 Table
- 4 Inline Chart/Image
- 18 Heading 1 و Headingهای ساختاریافته سطوح بعدی
- همه 4 جدول دارای RTL table direction
- جایگزین Unicode خراب (`�`) وجود ندارد

کنترل بصری:

- نسخه نهایی به 55 صفحه Render شد.
- تمام 55 صفحه به‌صورت تصویری بررسی شدند.
- Cover، Headingها، متن فارسی، Bulletها، Numbering، 4 جدول، 4 نمودار، Header، Footer، متن‌های فارسی/انگلیسی و صفحه آخر بررسی شدند.
- Blank Page ناخواسته، Crop، Overflow، شکستگی حروف فارسی یا جدول LTR ناخواسته مشاهده نشد.

## RAG Phase 2

`rag/book_manifest.json` ترتیب فصل‌ها و بازه صفحات منبع را نگه می‌دارد.

`scripts/build_rag_documents.py` رکوردهای فصل‌محور با شناسه قطعی، Hash منبع خام، Hash متن پردازش‌شده و provenance ترجمه تولید می‌کند.

تست ساختاری Builder روی یک Mirror محلی از همین ساختار انجام شد و نتیجه چنین بود:

```text
records: 19
unique_document_ids: 19
missing_text: 0
source_type_book: PASS
language_fa: PASS
raw_content_hash_consistent: PASS
last_record: unit-17 / source pages 50-53
```

Chunking نهایی عمداً در این مخزن انجام نشده است تا مطابق معماری Phase 2، پس از آماده‌شدن Website + Book + Video در پروژه اصلی RAG Finance انجام شود.
