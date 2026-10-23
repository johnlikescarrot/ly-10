import React from 'react';
import { astryxTokens } from './tokens.js';
import { FormulaItem, MantraItem } from '../types/index.js';

export interface FormulaSheetProps {
  formulas: FormulaItem[];
  mantras: MantraItem[];
}

export const FormulaSheet: React.FC<FormulaSheetProps> = ({ formulas, mantras }) => {
  return (
    <div style={{ pageBreakInside: 'avoid' }}>
      <div
        style={{
          backgroundColor: astryxTokens.colors.navy,
          color: astryxTokens.colors.white,
          borderRadius: astryxTokens.radii.md,
          padding: '10px 14px',
          marginBottom: '12px',
          textAlign: 'center',
        }}
      >
        <h2 style={{ margin: 0, fontSize: astryxTokens.fontSizes.xl, fontWeight: 800, color: '#FACC15' }}>
          TỜ CÔNG THỨC VÀNG 1 TRANG — GIỮA HỌC KÌ I VẬT LÍ 10
        </h2>
        <div style={{ fontSize: astryxTokens.fontSizes.xs, color: '#CBD5E1', marginTop: '2px' }}>
          In rời tra cứu thần tốc | Chuẩn 100% Bộ SGK Kết nối tri thức với cuộc sống
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '14px' }}>
        {formulas.map((item, idx) => (
          <div
            key={idx}
            style={{
              border: `1px solid ${astryxTokens.colors.primaryBorder}`,
              borderRadius: astryxTokens.radii.md,
              backgroundColor: astryxTokens.colors.white,
              padding: '8px 10px',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '4px' }}>
              <span style={{ fontSize: astryxTokens.fontSizes.xs, fontWeight: 700, color: astryxTokens.colors.primary }}>
                {item.category}
              </span>
              <span style={{ fontSize: astryxTokens.fontSizes.xs, fontWeight: 600, color: astryxTokens.colors.navy }}>
                {item.name}
              </span>
            </div>
            <div
              style={{
                backgroundColor: astryxTokens.colors.primaryLight,
                padding: '6px 8px',
                borderRadius: '4px',
                fontFamily: astryxTokens.fonts.mono,
                fontWeight: 700,
                fontSize: astryxTokens.fontSizes.sm,
                color: astryxTokens.colors.navy,
                textAlign: 'center',
                marginBottom: '4px',
              }}
            >
              {item.symbolFormula}
            </div>
            <div style={{ fontSize: astryxTokens.fontSizes.xs, color: astryxTokens.colors.textMuted }}>
              {item.notes}
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          backgroundColor: astryxTokens.colors.amberBg,
          border: `1px solid ${astryxTokens.colors.amberBorder}`,
          borderRadius: astryxTokens.radii.md,
          padding: '10px 12px',
        }}
      >
        <div style={{ fontWeight: 800, color: '#92400E', fontSize: astryxTokens.fontSizes.base, marginBottom: '8px' }}>
          ⚡ 10 KHẨU QUYẾT SIÊU TRÍ NHỚ — BẬT NAY ĐÁP ÁN TRONG 3 GIÂY
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', fontSize: astryxTokens.fontSizes.xs }}>
          {mantras.map((m) => (
            <div key={m.index} style={{ backgroundColor: astryxTokens.colors.white, padding: '6px 8px', borderRadius: '4px', border: `1px solid ${astryxTokens.colors.border}` }}>
              <strong style={{ color: astryxTokens.colors.amber }}>#{m.index}. {m.title}:</strong>{' '}
              <span style={{ fontWeight: 700, color: astryxTokens.colors.navy }}>"{m.mnemonic}"</span> — {m.application}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
