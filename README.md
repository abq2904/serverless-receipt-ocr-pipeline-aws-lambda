# Serverless OCR Receipt Processing Pipeline with AWS Lambda

## Project Overview

A cloud-native, **serverless pipeline** that converts unstructured receipt images into structured financial data for **reporting, ERP integration, and analytics automation**. Built using **Python, FastAPI, and AWS Lambda**, this project demonstrates **production-ready backend design**, **event-driven architecture**, and **cloud automation skills**.

## Architecture & Flow

![Pipeline Flow Diagram](showcase_pictures/01_pipeline_flow_diagram.png "Serverless OCR Receipt Pipeline Flow Diagram")

## Tech Stack

- **Backend / Serverless** : Python, FastAPI, AWS Lambda
- **Storage & Pipeline** : AWS S3, JSON
- **Data Extraction** : OCR (Tesseract / Custom)
- **Logging & Monitoring** : Python Logging
- **Optional Integration** : ERPNext, Analytics dashboards

## Key Features

- Fully **serverless, cloud-native architecture**
- OCR-based **text extraction from receipts**
- Automatic parsing of key fields: **merchant, date, subtotal, tax, total**
- Structured JSON output for **accounting, analytics, or ERP systems**
- Robust **error-handling, logging, and event-driven design**
- **Scalable pipeline** , handling hundreds of receipts per minute

## Workflow

This project showcases a **production-ready, serverless backend pipeline** for automated receipt processing. It demonstrates  **event-driven architecture** ,  **scalable AWS Lambda functions** , and **robust OCR-based data extraction** from unstructured images. Structured outputs integrate seamlessly with  **ERP systems, analytics dashboards, and automated reporting workflows** , highlighting expertise in  **Python, FastAPI, cloud automation, and financial data pipelines** .

With  **logging, error handling, and retry mechanisms** , this system is designed for  **reliability at scale** , processing hundreds of receipts per minute while maintaining clean, structured data. It reflects the  **design, implementation, and optimization skills expected from a senior backend developer** .

## API Example

Upload receipt via POST:

<pre class="overflow-visible! px-0!" data-start="1770" data-end="1943"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl -X POST </span><span>"http://127.0.0.1:8000/upload"</span><span> \
 -H </span><span>"accept: application/json"</span><span> \
 -H </span><span>"Content-Type: multipart/form-data"</span><span> \
 -F </span><span>"file=@receipt1.jpg;type=image/jpeg"</span><span>
</span></span></code></div></div></pre>

Sample response:

<pre class="overflow-visible! px-0!" data-start="1963" data-end="2080"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"merchant"</span><span>:</span><span></span><span>"SAFEWAY"</span><span>,</span><span>
  </span><span>"date"</span><span>:</span><span></span><span>"11/20/2019"</span><span>,</span><span>
  </span><span>"subtotal"</span><span>:</span><span></span><span>20.86</span><span>,</span><span>
  </span><span>"tax"</span><span>:</span><span></span><span>2.30</span><span>,</span><span>
  </span><span>"total"</span><span>:</span><span></span><span>23.16</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

## Local Setup

1. Clone the repo:

<pre class="overflow-visible! px-0!" data-start="2117" data-end="2258"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/abq2904/serverless-receipt-ocr-pipeline-aws-lambda.git
</span><span>cd</span><span> serverless-receipt-ocr-pipeline-aws-lambda
</span></span></code></div></div></pre>

2. Create virtual environment:

<pre class="overflow-visible! px-0!" data-start="2292" data-end="2377"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
</span></span></code></div></div></pre>

3. Run the API locally:

<pre class="overflow-visible! px-0!" data-start="2404" data-end="2463"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m uvicorn api_gateway.main:app --reload
</span></span></code></div></div></pre>

4. Open Swagger UI for testing: `http://127.0.0.1:8000/docs`

## Screenshots & Examples

1. **Pipeline Flow Diagram**

   `01_pipeline_flow_diagram.png` — Visual representation of the serverless receipt processing pipeline, showing upload, OCR, parsing, and storage.
2. **Terminal OCR Pipeline Logs**

   `02_terminal_ocr_pipeline.png` — Terminal output showing receipt upload, OCR processing, parsing, and structured JSON storage.
3. **Upload Receipt API**

   `03_upload_receipt_api.png` — Screenshot of API POST request and JSON response from receipt upload.
4. **Raw Receipt Input**

   `04_receipt_raw_input.png` — Example of a raw receipt image used for testing OCR extraction.

## License

MIT License

## Keywords

Serverless, AWS Lambda, OCR, Receipt Processing, Python, FastAPI, Data Parsing, ERP Integration, Cloud Automation, Event-Driven Architecture, Backend Development, Financial Automation, Analytics
