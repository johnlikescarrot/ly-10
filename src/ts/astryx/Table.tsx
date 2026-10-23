import React from 'react';
import { astryxTokens } from './tokens.js';

export interface Column<T> {
  header: string;
  accessor: keyof T | ((row: T) => React.ReactNode);
  align?: 'left' | 'center' | 'right';
  width?: string;
}

export interface TableProps<T> {
  columns: Column<T>[];
  data: T[];
  title?: string;
  className?: string;
}

export function Table<T>({ columns, data, title, className = '' }: TableProps<T>) {
  return (
    <div
      className={`astryx-table-container ${className}`}
      style={{
        margin: `${astryxTokens.spacing.md} 0`,
        borderRadius: astryxTokens.radii.md,
        overflow: 'hidden',
        border: `1px solid ${astryxTokens.colors.border}`,
        pageBreakInside: 'avoid',
      }}
    >
      {title && (
        <div
          style={{
            backgroundColor: astryxTokens.colors.navy,
            color: astryxTokens.colors.white,
            padding: '8px 12px',
            fontSize: astryxTokens.fontSizes.sm,
            fontWeight: 700,
          }}
        >
          {title}
        </div>
      )}
      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: astryxTokens.fontSizes.sm }}>
        <thead>
          <tr style={{ backgroundColor: astryxTokens.colors.slateBg, borderBottom: `2px solid ${astryxTokens.colors.border}` }}>
            {columns.map((col, idx) => (
              <th
                key={idx}
                style={{
                  padding: '8px 10px',
                  textAlign: col.align || 'left',
                  fontWeight: 700,
                  color: astryxTokens.colors.navy,
                  width: col.width,
                  borderRight: idx < columns.length - 1 ? `1px solid ${astryxTokens.colors.border}` : 'none',
                }}
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, rIdx) => (
            <tr
              key={rIdx}
              style={{
                backgroundColor: rIdx % 2 === 0 ? astryxTokens.colors.white : '#F8FAFC',
                borderBottom: rIdx < data.length - 1 ? `1px solid ${astryxTokens.colors.border}` : 'none',
              }}
            >
              {columns.map((col, cIdx) => {
                const cellVal =
                  typeof col.accessor === 'function' ? col.accessor(row) : (row[col.accessor] as React.ReactNode);
                return (
                  <td
                    key={cIdx}
                    style={{
                      padding: '7px 10px',
                      textAlign: col.align || 'left',
                      borderRight: cIdx < columns.length - 1 ? `1px solid ${astryxTokens.colors.border}` : 'none',
                    }}
                  >
                    {cellVal}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
