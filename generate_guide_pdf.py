#!/usr/bin/env python3
"""Generate professional PDF user guide for Optik ZADA."""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

NAVY   = '#0f1f3d'
NAVY2  = '#1a3358'
GOLD   = '#c9952a'
GOLD2  = '#e8b84b'
LIGHT  = '#f5f7fc'
WHITE  = '#ffffff'
TEXT   = '#1a2540'
MUTED  = '#6b7a99'
BORDER = '#dde2ef'
GREEN  = '#1a8a4a'
RED    = '#c0392b'
ORANGE = '#c97d0a'

CSS_STYLE = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

@font-face {{
  font-family: 'Fallback';
  src: local('Segoe UI'), local('Arial');
}}

@page {{
  size: A4;
  margin: 20mm 18mm 22mm 18mm;
  @top-right {{
    content: "Optik ZADA · Panduan Pengguna";
    font-size: 8pt;
    color: {MUTED};
    font-family: 'Inter', 'Fallback', sans-serif;
  }}
  @bottom-center {{
    content: counter(page);
    font-size: 8pt;
    color: {MUTED};
    font-family: 'Inter', 'Fallback', sans-serif;
  }}
  @bottom-left {{
    content: "v8.9.52 · 20 Juni 2026";
    font-size: 8pt;
    color: {MUTED};
    font-family: 'Inter', 'Fallback', sans-serif;
  }}
}}

@page cover {{
  margin: 0;
  @top-right {{ content: none; }}
  @bottom-center {{ content: none; }}
  @bottom-left {{ content: none; }}
}}

* {{
  box-sizing: border-box;
}}

body {{
  font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
  font-size: 9.5pt;
  line-height: 1.65;
  color: {TEXT};
  margin: 0;
  padding: 0;
}}

/* ── COVER PAGE ── */
.cover {{
  page: cover;
  width: 210mm;
  height: 297mm;
  background: {NAVY};
  display: flex;
  flex-direction: column;
  page-break-after: always;
  position: relative;
}}
.cover-accent {{
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 80mm;
  background: linear-gradient(180deg, transparent 0%, {NAVY2} 100%);
}}
.cover-gold-bar {{
  height: 6mm;
  background: linear-gradient(90deg, {GOLD} 0%, {GOLD2} 100%);
}}
.cover-body {{
  padding: 28mm 22mm 0 22mm;
  flex: 1;
}}
.cover-logo-area {{
  margin-bottom: 16mm;
}}
.cover-logo-icon {{
  width: 22mm;
  height: 22mm;
  background: {GOLD};
  border-radius: 6mm;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 5mm;
}}
.cover-logo-text {{
  font-size: 28pt;
  font-weight: 800;
  color: {WHITE};
  letter-spacing: 1px;
  line-height: 1;
}}
.cover-logo-sub {{
  font-size: 10pt;
  color: {GOLD2};
  letter-spacing: 4px;
  text-transform: uppercase;
  margin-top: 2mm;
  font-weight: 500;
}}
.cover-title {{
  font-size: 24pt;
  font-weight: 700;
  color: {WHITE};
  line-height: 1.2;
  margin-bottom: 4mm;
}}
.cover-subtitle {{
  font-size: 12pt;
  color: rgba(255,255,255,0.6);
  margin-bottom: 16mm;
  font-weight: 400;
}}
.cover-divider {{
  width: 20mm;
  height: 1mm;
  background: {GOLD};
  margin-bottom: 10mm;
}}
.cover-meta {{
  font-size: 9pt;
  color: rgba(255,255,255,0.5);
  line-height: 2;
}}
.cover-meta span {{
  color: {GOLD2};
  font-weight: 600;
}}
.cover-bottom {{
  padding: 8mm 22mm;
  border-top: 0.5mm solid rgba(255,255,255,0.1);
  font-size: 8pt;
  color: rgba(255,255,255,0.35);
  margin-top: auto;
}}

/* ── TOC PAGE ── */
.toc-page {{
  page-break-after: always;
  padding: 0 0 8mm 0;
}}
.toc-title {{
  font-size: 16pt;
  font-weight: 700;
  color: {NAVY};
  margin-bottom: 6mm;
  padding-bottom: 3mm;
  border-bottom: 0.5mm solid {GOLD};
}}
.toc-item {{
  display: flex;
  align-items: baseline;
  padding: 2.5mm 0;
  border-bottom: 0.3mm dotted {BORDER};
  font-size: 9.5pt;
}}
.toc-num {{
  font-weight: 700;
  color: {GOLD};
  width: 8mm;
  flex-shrink: 0;
}}
.toc-label {{
  flex: 1;
  color: {TEXT};
}}
.toc-dots {{
  border-bottom: 0.3mm dotted {MUTED};
  flex: 1;
  margin: 0 3mm 1mm 3mm;
  min-width: 10mm;
}}
.toc-page-num {{
  color: {MUTED};
  font-size: 8.5pt;
  font-weight: 500;
}}

/* ── SECTION PAGES ── */
.section {{
  page-break-before: always;
}}
.section:first-of-type {{
  page-break-before: avoid;
}}

/* ── HEADINGS ── */
h1 {{
  font-size: 16pt;
  font-weight: 700;
  color: {NAVY};
  margin: 0 0 5mm 0;
  padding-bottom: 3mm;
  border-bottom: 0.5mm solid {GOLD};
  line-height: 1.2;
}}
h2 {{
  font-size: 11pt;
  font-weight: 700;
  color: {NAVY};
  margin: 6mm 0 3mm 0;
  padding: 2mm 4mm;
  background: {LIGHT};
  border-left: 1mm solid {GOLD};
  border-radius: 0 2mm 2mm 0;
}}
h3 {{
  font-size: 9.5pt;
  font-weight: 700;
  color: {NAVY2};
  margin: 4mm 0 2mm 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 8.5pt;
}}

/* ── PARAGRAPH & LISTS ── */
p {{
  margin: 0 0 3mm 0;
  text-align: justify;
  orphans: 3;
  widows: 3;
}}
ul, ol {{
  margin: 2mm 0 3mm 5mm;
  padding: 0;
}}
li {{
  margin-bottom: 1.5mm;
  padding-left: 1mm;
}}
ul li::marker {{ color: {GOLD}; font-size: 10pt; }}
ol li::marker {{ color: {GOLD}; font-weight: 700; }}

/* ── TABLES ── */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 3mm 0 4mm 0;
  font-size: 8.5pt;
}}
thead tr {{
  background: {NAVY};
  color: {WHITE};
}}
thead th {{
  padding: 2.5mm 3mm;
  text-align: left;
  font-weight: 600;
  font-size: 8pt;
  letter-spacing: 0.3px;
}}
tbody tr:nth-child(even) {{
  background: {LIGHT};
}}
tbody tr:nth-child(odd) {{
  background: {WHITE};
}}
tbody td {{
  padding: 2.2mm 3mm;
  border-bottom: 0.3mm solid {BORDER};
  vertical-align: top;
  line-height: 1.5;
}}
tbody tr:last-child td {{
  border-bottom: 0.5mm solid {NAVY};
}}

/* ── CALLOUT BOXES ── */
blockquote {{
  margin: 3mm 0;
  padding: 3mm 4mm 3mm 5mm;
  border-left: 1.5mm solid {ORANGE};
  background: #fff8ee;
  border-radius: 0 2mm 2mm 0;
  font-size: 8.5pt;
  color: #5a3a00;
}}
blockquote p {{
  margin: 0;
  text-align: left;
}}

/* ── INLINE CODE ── */
code {{
  background: {LIGHT};
  border: 0.3mm solid {BORDER};
  border-radius: 1mm;
  padding: 0.2mm 1.5mm;
  font-family: 'Courier New', monospace;
  font-size: 8pt;
  color: {NAVY2};
}}

/* ── SECTION HEADER BADGE ── */
.section-badge {{
  display: inline-block;
  background: {GOLD};
  color: {WHITE};
  font-size: 7pt;
  font-weight: 700;
  padding: 0.5mm 2mm;
  border-radius: 1mm;
  letter-spacing: 0.5px;
  margin-bottom: 2mm;
  text-transform: uppercase;
}}

/* ── FAQ ITEMS ── */
.faq-q {{
  font-weight: 700;
  color: {NAVY};
  margin-top: 3mm;
}}
.faq-a {{
  color: {TEXT};
  margin-left: 3mm;
  padding-left: 3mm;
  border-left: 0.5mm solid {BORDER};
}}
"""

def md_to_html(text):
    return markdown.markdown(
        text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )

def build_cover():
    return f"""
    <div class="cover">
      <div class="cover-gold-bar"></div>
      <div class="cover-body">
        <div class="cover-logo-area">
          <div class="cover-logo-text">OPTIK ZADA</div>
          <div class="cover-logo-sub">Management System</div>
        </div>
        <div class="cover-title">Panduan<br>Pengguna</div>
        <div class="cover-subtitle">Petunjuk Operasional Lengkap</div>
        <div class="cover-divider"></div>
        <div class="cover-meta">
          Versi &nbsp;<span>8.9.52</span><br>
          Tanggal &nbsp;<span>20 Juni 2026</span><br>
          Dokumen &nbsp;<span>Panduan Pengguna — Operasional Harian</span>
        </div>
      </div>
      <div class="cover-bottom">
        Dokumen ini bersifat internal. Harap tidak disebarluaskan.
      </div>
    </div>
    """

def build_toc():
    sections = [
        ("1", "Mengenal Sistem & Hak Akses"),
        ("2", "Instalasi Aplikasi (PWA)"),
        ("3", "Login"),
        ("4", "Dashboard"),
        ("5", "Membuat Invoice Baru"),
        ("6", "Riwayat Transaksi"),
        ("7", "Melunasi DP"),
        ("8", "Data Customer"),
        ("9", "Master Data Produk & Stok"),
        ("10", "Pengaturan Toko"),
        ("11", "Manajemen Pengguna"),
        ("12", "Backup Data"),
        ("13", "FAQ & Masalah Umum"),
    ]
    items = ''.join(f"""
        <div class="toc-item">
          <span class="toc-num">{num}.</span>
          <span class="toc-label">{label}</span>
          <span class="toc-dots"></span>
        </div>""" for num, label in sections)

    return f"""
    <div class="toc-page">
      <div class="toc-title">Daftar Isi</div>
      {items}
    </div>
    """

def build_content():
    with open('/home/user/optik-zada/PANDUAN_PENGGUNA.md', 'r') as f:
        raw = f.read()

    # Remove the title and TOC (we have custom ones)
    lines = raw.split('\n')
    # Skip first line (# title) and the TOC block
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('---') and i > 5:
            content_start = i + 1
            break

    content = '\n'.join(lines[content_start:])

    # Split into sections by ## heading
    import re
    sections = re.split(r'\n(?=## \d+\.)', content)

    html_sections = []
    for sec in sections:
        if not sec.strip():
            continue
        html_sections.append(f'<div class="section">{md_to_html(sec)}</div>')

    return '\n'.join(html_sections)

def main():
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<style>{CSS_STYLE}</style>
</head>
<body>
{build_cover()}
{build_toc()}
{build_content()}
</body>
</html>"""

    font_config = FontConfiguration()
    doc = HTML(string=html, base_url='/home/user/optik-zada/')
    css = CSS(string=CSS_STYLE, font_config=font_config)

    output = '/home/user/optik-zada/Panduan_Pengguna_OptikZADA.pdf'
    doc.write_pdf(output, font_config=font_config)
    print(f'✅ PDF generated: {output}')

    import os
    size = os.path.getsize(output)
    print(f'   Size: {size/1024:.0f} KB')

if __name__ == '__main__':
    main()
