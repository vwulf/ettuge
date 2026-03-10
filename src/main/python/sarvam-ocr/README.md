# sarvam-ocr

OCR pipeline for old WX-encoded Kannada PDFs using the [Sarvam Vision API](https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-vision).

## Problem

The DNS Bhat PDF collection includes books published with old Ghostscript/PageMaker using
proprietary WX Kannada font encoding (pre-Unicode era). `pdfminer` extracts garbled text like
`¨sÁµÉAiÀÄ` instead of `ಭಾಷೆಯ`. These PDFs need OCR to recover the actual Unicode Kannada text.

## Solution

Sarvam Vision is a 3B multimodal model with 84.3% accuracy on olmOCR-Bench, supporting
Kannada (`kn-IN`) natively. It accepts PDF/PNG/JPG input and outputs Markdown.

## PDFs to process

All live in `~/Library/CloudStorage/GoogleDrive-vishwasms@gmail.com/My Drive/Books/DNS-Bhat/`:

| File | Book | Pages | Target output |
|------|------|-------|---------------|
| `KannadaPadagalaOlarachane.pdf` | 03 | 239 | `03-...-book.md` |
| `KannadaVakyagalaOlaracane.pdf` | 25 | 289 | `25-...-book.md` |
| `baasheyaBagge.pdf` | 27 | 208 | `27-...-book.md` |
| `kannada-nudi-nadedu-banda-dari.pdf` | 17 | 405 | `17-...-book.md` |
| `kannadakkeBeku.pdf` | 28 | 253 | `28-...-book.md` |
| `kannadavyakaranayaakebeku.pdf` | 29 | 260 | `29-...-book.md` |
| `sollarime-1.pdf` | 07 vol.1 | 327 | `07-...-vol1-book.md` |
| `sollarime-2.pdf` | 07 vol.2 | 301 | `07-...-vol2-book.md` |

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Sarvam API key
export SARVAM_API_KEY="your_key_here"
# Or add to ~/.zshrc / ~/.bashrc

# 3. Get a key at https://dashboard.sarvam.ai
```

## Usage

```bash
# Process a single PDF
python ocr.py --pdf path/to/book.pdf --lang kn-IN --out output.md

# Process all WX-encoded DNS Bhat PDFs
python ocr_dnsbhat.py

# Process one book by number
python ocr_dnsbhat.py --book 03
python ocr_dnsbhat.py --book 27
```

## Output

OCR results are written to the ettuge repository:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/{NN}-{slug}-book.md`

Existing garbled files are overwritten with clean Unicode Kannada text.

## API notes

- **Model**: Sarvam Vision (3B VLM)
- **Language code**: `kn-IN`
- **Output format**: `md` (Markdown)
- **Workflow**: create job → upload PDF → start → poll → download ZIP → extract MD
- **SDK**: `sarvamai` Python package (`pip install sarvamai`)
- **Docs**: https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-vision
- **Dashboard**: https://dashboard.sarvam.ai
