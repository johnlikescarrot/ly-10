export const pageStyles = `
@page {
  size: A4;
  margin: 15mm 12mm 15mm 12mm;
  @top-center {
    content: "ĐỀ CƯƠNG ÔN TẬP KTGK I — VẬT LÍ 10 (2026–2027)";
    font-family: 'Be Vietnam Pro', system-ui, sans-serif;
    font-size: 8pt;
    color: #475569;
  }
  @bottom-right {
    content: "Trang " counter(page);
    font-family: 'Be Vietnam Pro', system-ui, sans-serif;
    font-size: 8pt;
    color: #475569;
  }
}

body {
  font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #0f172a;
  background-color: #ffffff;
  line-height: 1.5;
  font-size: 9.5pt;
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page-break {
  page-break-before: always;
}

.avoid-break {
  page-break-inside: avoid;
}

.header-banner {
  background-color: #0f172a;
  color: white;
  padding: 16px 20px;
  border-radius: 8px;
  margin-bottom: 16px;
}

.header-badge {
  display: inline-block;
  background-color: #1e3a8a;
  color: #93c5fd;
  border: 1px solid #60a5fa;
  border-radius: 12px;
  padding: 2px 10px;
  font-size: 8pt;
  font-weight: 700;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.section-title {
  background-color: #0f172a;
  color: #ffffff;
  padding: 10px 14px;
  border-radius: 6px;
  font-size: 13pt;
  font-weight: 800;
  margin-top: 20px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.subsection-title {
  background-color: #eff6ff;
  border-left: 4px solid #1d4ed8;
  color: #1e40af;
  padding: 6px 12px;
  font-size: 11pt;
  font-weight: 700;
  margin-top: 14px;
  margin-bottom: 8px;
}

.table-custom {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
  font-size: 8.8pt;
}

.table-custom th, .table-custom td {
  border: 1px solid #cbd5e1;
  padding: 6px 8px;
  text-align: left;
}

.table-custom th {
  background-color: #0f172a;
  color: #ffffff;
  font-weight: 700;
}

.table-custom tr:nth-child(even) {
  background-color: #f8fafc;
}

.card-box {
  border-radius: 6px;
  padding: 10px 12px;
  margin: 8px 0;
  border-left: 4px solid;
}

.card-blue {
  background-color: #eff6ff;
  border-color: #1d4ed8;
}

.card-teal {
  background-color: #f0fdfa;
  border-color: #0f766e;
}

.card-amber {
  background-color: #fffbeb;
  border-color: #b45309;
}

.card-red {
  background-color: #fef2f2;
  border-color: #b91c1c;
}

.mcq-item {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px 12px;
  margin-bottom: 8px;
  page-break-inside: avoid;
}

.mcq-options {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px;
  margin-top: 6px;
  font-size: 9pt;
}

.mcq-options-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  margin-top: 6px;
  font-size: 9pt;
}

.mcq-options-1 {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 6px;
  font-size: 9pt;
}

.tag-nb {
  background-color: #dbeafe;
  color: #1e40af;
  font-weight: 700;
  font-size: 7.5pt;
  padding: 1px 6px;
  border-radius: 4px;
  margin-right: 6px;
}

.tag-th {
  background-color: #ccfbf1;
  color: #0f766e;
  font-weight: 700;
  font-size: 7.5pt;
  padding: 1px 6px;
  border-radius: 4px;
  margin-right: 6px;
}

.tag-vd {
  background-color: #fef3c7;
  color: #b45309;
  font-weight: 700;
  font-size: 7.5pt;
  padding: 1px 6px;
  border-radius: 4px;
  margin-right: 6px;
}

.tag-vdc {
  background-color: #fee2e2;
  color: #b91c1c;
  font-weight: 700;
  font-size: 7.5pt;
  padding: 1px 6px;
  border-radius: 4px;
  margin-right: 6px;
}

.explanation-box {
  background-color: #f8fafc;
  border: 1px dashed #cbd5e1;
  border-radius: 4px;
  padding: 6px 10px;
  margin-top: 6px;
  font-size: 8.5pt;
  color: #334155;
}
`;
