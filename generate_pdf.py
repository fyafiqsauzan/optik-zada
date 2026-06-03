from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# ── Colors ────────────────────────────────────────────────────────────────────
NAVY    = HexColor('#0f1f3d')
NAVY2   = HexColor('#1a3260')
GOLD    = HexColor('#f0a500')
GOLD2   = HexColor('#ffd166')
GREEN   = HexColor('#22c55e')
DANGER  = HexColor('#ef4444')
MUTED   = HexColor('#94a3b8')
BG2     = HexColor('#f1f5f9')
BORDER  = HexColor('#e2e8f0')
TEXT    = HexColor('#0f172a')

OUT = '/home/user/optik-zada/Sistem Akuntansi Cash-Basis — Optik Zada.pdf'

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)

styles = getSampleStyleSheet()

def s(name, **kw):
    base = styles['Normal']
    return ParagraphStyle(name, parent=base, **kw)

title_style   = s('Title',   fontSize=20, textColor=NAVY,  leading=26, spaceAfter=4,  fontName='Helvetica-Bold')
sub_style     = s('Sub',     fontSize=11, textColor=MUTED,  leading=16, spaceAfter=16, fontName='Helvetica')
h1_style      = s('H1',     fontSize=13, textColor=NAVY,  leading=18, spaceBefore=18, spaceAfter=6, fontName='Helvetica-Bold')
h2_style      = s('H2',     fontSize=11, textColor=NAVY2, leading=16, spaceBefore=12, spaceAfter=4, fontName='Helvetica-Bold')
body_style    = s('Body',   fontSize=10, textColor=TEXT,   leading=15, spaceAfter=4,  fontName='Helvetica')
note_style    = s('Note',   fontSize=9,  textColor=MUTED,  leading=13, spaceAfter=2,  fontName='Helvetica-Oblique')
code_style    = s('Code',   fontSize=9,  textColor=NAVY2,  leading=13, spaceAfter=2,  fontName='Courier', backColor=BG2)
mono_style    = s('Mono',   fontSize=9,  textColor=TEXT,   leading=13, spaceAfter=2,  fontName='Courier')
check_style   = s('Check',  fontSize=10, textColor=GREEN,  leading=14, spaceAfter=2,  fontName='Helvetica-Bold')

def fmt(n):
    return f'Rp {n:,.0f}'.replace(',', '.')

def pct(a, b):
    return f'{a/b*100:.0f}%' if b else '0%'

# ── Data ──────────────────────────────────────────────────────────────────────
TOT    = 1_200_000
MODAL  = 900_000
PROFIT = 300_000
DP     = 300_000
LUNAS  = 900_000
DP_RATIO    = DP / TOT       # 25%
LUNAS_RATIO = LUNAS / TOT    # 75%
PROFIT_MEI  = int(PROFIT * DP_RATIO)    # 75.000
PROFIT_JUNI = int(PROFIT * LUNAS_RATIO) # 225.000

# ── Helper: section header box ────────────────────────────────────────────────
def section_box(label, color=NAVY):
    data = [[Paragraph(f'<font color="white"><b>{label}</b></font>', s('SH', fontSize=10, fontName='Helvetica-Bold', textColor=white, leading=14))]]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('ROWPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 0, color),
    ]))
    return t

# ── Helper: stat row table ────────────────────────────────────────────────────
def stat_table(rows, col_w=None):
    col_w = col_w or [5*cm, 4*cm, 4*cm, 4*cm]
    t = Table(rows, colWidths=col_w)
    style = [
        ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',    (0,0), (-1,-1), 9),
        ('LEADING',     (0,0), (-1,-1), 13),
        ('TEXTCOLOR',   (0,0), (-1, 0), NAVY),
        ('BACKGROUND',  (0,0), (-1, 0), BG2),
        ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
        ('ROWPADDING',  (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING',(0,0), (-1,-1), 8),
        ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
    ]
    t.setStyle(TableStyle(style))
    return t

def colored_cell(text, color=TEXT, bold=False):
    fn = 'Helvetica-Bold' if bold else 'Helvetica'
    return Paragraph(f'<font color="#{color.hexval()[2:]}">{text}</font>', s('cc', fontSize=9, fontName=fn, leading=13))

# ── Build story ───────────────────────────────────────────────────────────────
story = []

# Header
story.append(Paragraph('Sistem Akuntansi Cash-Basis', title_style))
story.append(Paragraph('Optik Zada Management System · Simulasi &amp; Penjelasan Teknis', sub_style))
story.append(HRFlowable(width='100%', thickness=2, color=GOLD, spaceAfter=16))

# ── 1. Latar Belakang ─────────────────────────────────────────────────────────
story.append(section_box('1.  Latar Belakang'))
story.append(Spacer(1, 8))
story.append(Paragraph(
    'Optik Zada menggunakan sistem pembayaran <b>Down Payment (DP)</b> dimana customer '
    'membayar sebagian di awal saat invoice dibuat, dan melunasi sisa di kemudian hari '
    '— bisa di bulan yang sama atau bulan berikutnya.',
    body_style
))
story.append(Paragraph(
    'Masalah yang ada sebelumnya: sistem mencatat <b>semua uang (DP + pelunasan) di bulan '
    'invoice dibuat</b>, bukan di bulan uang benar-benar diterima. Ini menyebabkan laporan '
    'keuangan bulanan tidak mencerminkan kondisi kas yang sesungguhnya.',
    body_style
))
story.append(Spacer(1, 4))

# ── 2. Prinsip Cash-Basis ─────────────────────────────────────────────────────
story.append(section_box('2.  Prinsip yang Diterapkan'))
story.append(Spacer(1, 8))

rules = [
    ['#', 'Komponen', 'Dicatat di Bulan'],
    ['1', 'Uang Muka (DP)', 'Bulan invoice dibuat (tanggal transaksi)'],
    ['2', 'Pelunasan', 'Bulan pelunasan dilakukan (bukan bulan invoice)'],
    ['3', 'Profit dari DP', 'Proporsional → (DP ÷ Total) × Profit'],
    ['4', 'Profit dari Pelunasan', 'Proporsional → (Lunas ÷ Total) × Profit'],
]
t = Table(rules, colWidths=[1*cm, 4.5*cm, 11.5*cm])
t.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY2),
    ('BACKGROUND',  (0,1), (-1, 1), BG2),
    ('BACKGROUND',  (0,3), (-1, 3), BG2),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t)
story.append(Spacer(1, 4))

story.append(Paragraph(
    '<b>Catatan:</b> Sistem ini memastikan total kas dan total profit yang tersebar '
    'di semua bulan selalu sama dengan nilai invoice asli — tidak ada angka yang hilang atau dobel.',
    note_style
))

# ── 3. Simulasi ───────────────────────────────────────────────────────────────
story.append(section_box('3.  Simulasi Kasus: Invoice Tn. Abian'))
story.append(Spacer(1, 8))

story.append(Paragraph('<b>Data Invoice:</b>', h2_style))
inv_data = [
    ['Field', 'Nilai', 'Keterangan'],
    ['Tanggal Invoice', '09/05/2026', 'Invoice dibuat 9 Mei 2026'],
    ['Total Transaksi', fmt(TOT), 'Harga jual frame + lensa'],
    ['Modal (HPP)', fmt(MODAL), 'Biaya pokok produk'],
    ['Profit Invoice', fmt(PROFIT), f'= {fmt(TOT)} − {fmt(MODAL)}'],
    ['Uang Muka (DP)', fmt(DP), f'Dibayar 9 Mei 2026 ({pct(DP, TOT)} dari total)'],
    ['Sisa Tagihan', fmt(TOT - DP), 'Belum lunas'],
    ['Tanggal Lunas', '02/06/2026', 'Pelunasan dilakukan 2 Juni 2026'],
    ['Jumlah Pelunasan', fmt(LUNAS), f'Dibayar 2 Juni 2026 ({pct(LUNAS, TOT)} dari total)'],
]
t2 = Table(inv_data, colWidths=[4.5*cm, 4.5*cm, 8*cm])
t2.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY2),
    ('BACKGROUND',  (0,2), (-1, 2), BG2),
    ('BACKGROUND',  (0,4), (-1, 4), BG2),
    ('BACKGROUND',  (0,6), (-1, 6), BG2),
    ('BACKGROUND',  (0,8), (-1, 8), HexColor('#f0fdf4')),
    ('TEXTCOLOR',   (0,8), (-1, 8), GREEN),
    ('FONTNAME',    (0,8), (-1, 8), 'Helvetica-Bold'),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t2)

story.append(Paragraph('<b>Perhitungan Rasio Profit:</b>', h2_style))
ratio_data = [
    ['Komponen', 'Rumus', 'Hasil'],
    ['DP Ratio',       f'{fmt(DP)} ÷ {fmt(TOT)}',   f'{pct(DP, TOT)} (25%)'],
    ['Lunas Ratio',    f'{fmt(LUNAS)} ÷ {fmt(TOT)}', f'{pct(LUNAS, TOT)} (75%)'],
    ['Profit DP',      f'{fmt(PROFIT)} × 25%',        fmt(PROFIT_MEI)],
    ['Profit Lunas',   f'{fmt(PROFIT)} × 75%',        fmt(PROFIT_JUNI)],
    ['Total Profit',   f'{fmt(PROFIT_MEI)} + {fmt(PROFIT_JUNI)}', fmt(PROFIT_MEI + PROFIT_JUNI) + '  ✓'],
]
t3 = Table(ratio_data, colWidths=[4*cm, 6.5*cm, 6.5*cm])
t3.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY2),
    ('BACKGROUND',  (0,2), (-1, 2), BG2),
    ('BACKGROUND',  (0,4), (-1, 4), BG2),
    ('BACKGROUND',  (0,5), (-1, 5), HexColor('#f0fdf4')),
    ('TEXTCOLOR',   (0,5), (-1, 5), GREEN),
    ('FONTNAME',    (0,5), (-1, 5), 'Helvetica-Bold'),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t3)

# ── 4. Hasil per Modul ────────────────────────────────────────────────────────
story.append(section_box('4.  Hasil di Setiap Modul'))
story.append(Spacer(1, 8))

# Mei
story.append(Paragraph('▌ Laporan &amp; Cashflow — Mei 2026', h2_style))
may_data = [
    ['Modul', 'Kas Masuk', 'Profit', 'Keterangan'],
    ['Laporan Mei',  fmt(DP), fmt(PROFIT_MEI),
     'DP diterima 9 Mei → masuk ke Mei'],
    ['Cashflow Mei', fmt(DP), fmt(PROFIT_MEI),
     'Kas Masuk = DP, bukan total billing'],
    ['Tabel Harian\n09/05/2026', fmt(DP), fmt(PROFIT_MEI),
     '1 txn, profit proporsional 25%'],
]
t4 = Table(may_data, colWidths=[3.5*cm, 3*cm, 3*cm, 7.5*cm])
t4.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY2),
    ('BACKGROUND',  (0,2), (-1, 2), BG2),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
    ('TEXTCOLOR',   (0,1), (2,-1), HexColor('#0f172a')),
    ('FONTNAME',    (1,1), (2,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',   (2,1), (2,-1), GREEN),
]))
story.append(t4)

story.append(Paragraph(
    '⚠  Pelunasan Rp 900.000 (lunasDate = 2 Juni) <b>tidak muncul</b> di laporan Mei. '
    'Ini benar — uang belum diterima di bulan Mei.',
    note_style
))
story.append(Spacer(1, 6))

# Juni
story.append(Paragraph('▌ Dashboard &amp; Laporan &amp; Cashflow — Juni 2026', h2_style))
jun_data = [
    ['Modul', 'Kas Masuk', 'Profit', 'Keterangan'],
    ['Dashboard Juni',  fmt(LUNAS), fmt(PROFIT_JUNI),
     'Pelunasan Abian masuk ke bulan berjalan'],
    ['Laporan Juni',    fmt(LUNAS), fmt(PROFIT_JUNI),
     'Invoice dibuat Mei, tapi uang masuk Juni'],
    ['Cashflow Juni',   fmt(LUNAS), fmt(PROFIT_JUNI),
     'Dropdown Juni muncul meski tanpa invoice baru'],
    ['Tabel Harian\n02/06/2026', fmt(LUNAS), fmt(PROFIT_JUNI),
     '0 txn baru, hanya pembayaran masuk'],
    ['Bar Chart\nDashboard', fmt(LUNAS), '—',
     'Bar tanggal 02/06 terangkat sebesar pelunasan'],
]
t5 = Table(jun_data, colWidths=[3.5*cm, 3*cm, 3*cm, 7.5*cm])
t5.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), HexColor('#166534')),
    ('BACKGROUND',  (0,2), (-1, 2), HexColor('#f0fdf4')),
    ('BACKGROUND',  (0,4), (-1, 4), HexColor('#f0fdf4')),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME',    (1,1), (2,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',   (1,1), (1,-1), NAVY),
    ('TEXTCOLOR',   (2,1), (2,-1), GREEN),
]))
story.append(t5)

# ── 5. Cross-check ────────────────────────────────────────────────────────────
story.append(section_box('5.  Verifikasi — Tidak Ada Angka Hilang atau Dobel'))
story.append(Spacer(1, 8))

xcheck = [
    ['Komponen', 'Mei 2026', 'Juni 2026', 'Total', 'Invoice Asli', 'Status'],
    ['Kas Masuk',
     fmt(DP), fmt(LUNAS),
     fmt(DP + LUNAS), fmt(TOT), '✓'],
    ['Profit',
     fmt(PROFIT_MEI), fmt(PROFIT_JUNI),
     fmt(PROFIT_MEI + PROFIT_JUNI), fmt(PROFIT), '✓'],
]
t6 = Table(xcheck, colWidths=[3*cm, 2.5*cm, 2.5*cm, 3*cm, 3*cm, 3*cm])
t6.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY2),
    ('BACKGROUND',  (0,1), (-1, 1), BG2),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME',    (3,1), (3,-1), 'Helvetica-Bold'),
    ('FONTNAME',    (5,1), (5,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',   (5,1), (5,-1), GREEN),
    ('ALIGN',       (1,0), (-1,-1), 'CENTER'),
]))
story.append(t6)
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Total Kas Masuk (Mei + Juni) = ' + fmt(DP + LUNAS) + ' = Total Invoice ✓     '
    'Total Profit (Mei + Juni) = ' + fmt(PROFIT_MEI + PROFIT_JUNI) + ' = Total Profit Invoice ✓',
    s('XC', fontSize=9, fontName='Helvetica-Bold', textColor=GREEN, leading=13)
))

# ── 6. Perbandingan Sebelum vs Sesudah ───────────────────────────────────────
story.append(section_box('6.  Perbandingan: Sistem Lama vs Sistem Baru'))
story.append(Spacer(1, 8))

comp = [
    ['', 'Sistem Lama (Salah)', 'Sistem Baru (Cash-Basis)'],
    ['Laporan Mei\nKas Masuk',
     fmt(TOT) + '\n(DP + Pelunasan digabung)',
     fmt(DP) + '\n(DP saja)'],
    ['Laporan Mei\nProfit',
     fmt(PROFIT) + '\n(100% profit di Mei)',
     fmt(PROFIT_MEI) + '\n(25% proporsional)'],
    ['Laporan Juni\nKas Masuk',
     'Rp 0\n(tidak terdeteksi)',
     fmt(LUNAS) + '\n(pelunasan masuk)'],
    ['Laporan Juni\nProfit',
     'Rp 0\n(tidak terdeteksi)',
     fmt(PROFIT_JUNI) + '\n(75% proporsional)'],
    ['Cashflow Mei\nKas Masuk',
     fmt(TOT) + '\n(total billing, bukan kas)',
     fmt(DP) + '\n(kas sesungguhnya)'],
    ['Cashflow Juni\nDropdown',
     'Tidak muncul\n(tidak ada invoice baru)',
     'Muncul\n(ada pelunasan masuk)'],
]
t7 = Table(comp, colWidths=[4*cm, 6.5*cm, 6.5*cm])
t7.setStyle(TableStyle([
    ('FONTNAME',    (0,0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 9),
    ('LEADING',     (0,0), (-1,-1), 13),
    ('TEXTCOLOR',   (0,0), (-1, 0), white),
    ('BACKGROUND',  (0,0), (-1, 0), NAVY),
    ('BACKGROUND',  (1,1), (1,-1), HexColor('#fef2f2')),
    ('TEXTCOLOR',   (1,1), (1,-1), DANGER),
    ('BACKGROUND',  (2,1), (2,-1), HexColor('#f0fdf4')),
    ('TEXTCOLOR',   (2,1), (2,-1), HexColor('#166534')),
    ('GRID',        (0,0), (-1,-1), 0.4, BORDER),
    ('ROWPADDING',  (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ('VALIGN',      (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME',    (0,1), (0,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',   (0,1), (0,-1), NAVY),
]))
story.append(t7)

# ── Footer ────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 20))
story.append(HRFlowable(width='100%', thickness=1, color=BORDER))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Optik Zada Management System · v8.9.16 Beta · Dokumen ini dibuat otomatis dari sistem',
    s('Footer', fontSize=8, textColor=MUTED, leading=12, alignment=TA_CENTER)
))

doc.build(story)
print(f'PDF dibuat: {OUT}')
