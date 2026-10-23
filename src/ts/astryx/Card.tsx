import React from 'react';
import { astryxTokens } from './tokens.js';

export interface CardProps {
  variant?: 'default' | 'outlined' | 'callout' | 'trap' | 'accent';
  title?: React.ReactNode;
  icon?: string;
  badge?: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
}

export const Card: React.FC<CardProps> = ({
  variant = 'default',
  title,
  icon,
  badge,
  children,
  footer,
  className = '',
  style = {},
}) => {
  let bgColor = astryxTokens.colors.white;
  let borderColor = astryxTokens.colors.border;
  let titleBg = astryxTokens.colors.slateBg;
  let titleTextColor = astryxTokens.colors.navy;

  if (variant === 'callout') {
    bgColor = astryxTokens.colors.primaryLight;
    borderColor = astryxTokens.colors.primaryBorder;
    titleBg = '#DBEAFE';
    titleTextColor = '#1E40AF';
  } else if (variant === 'trap') {
    bgColor = astryxTokens.colors.roseBg;
    borderColor = astryxTokens.colors.roseBorder;
    titleBg = '#FEE2E2';
    titleTextColor = '#991B1B';
  } else if (variant === 'accent') {
    bgColor = astryxTokens.colors.amberBg;
    borderColor = astryxTokens.colors.amberBorder;
    titleBg = '#FEF3C7';
    titleTextColor = '#92400E';
  }

  return (
    <div
      className={`astryx-card astryx-card-${variant} ${className}`}
      style={{
        backgroundColor: bgColor,
        border: `1px solid ${borderColor}`,
        borderRadius: astryxTokens.radii.lg,
        overflow: 'hidden',
        marginBottom: astryxTokens.spacing.md,
        boxShadow: astryxTokens.shadows.sm,
        pageBreakInside: 'avoid',
        ...style,
      }}
    >
      {title && (
        <div
          style={{
            backgroundColor: titleBg,
            padding: '8px 14px',
            borderBottom: `1px solid ${borderColor}`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            fontWeight: 700,
            fontSize: astryxTokens.fontSizes.sm,
            color: titleTextColor,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            {icon && <span>{icon}</span>}
            <span>{title}</span>
          </div>
          {badge && (
            <span
              style={{
                backgroundColor: 'rgba(255,255,255,0.8)',
                padding: '2px 8px',
                borderRadius: astryxTokens.radii.sm,
                fontSize: astryxTokens.fontSizes.xs,
                fontWeight: 600,
              }}
            >
              {badge}
            </span>
          )}
        </div>
      )}
      <div style={{ padding: '12px 14px', fontSize: astryxTokens.fontSizes.sm, lineHeight: 1.5 }}>
        {children}
      </div>
      {footer && (
        <div
          style={{
            padding: '8px 14px',
            borderTop: `1px dashed ${borderColor}`,
            backgroundColor: 'rgba(0,0,0,0.02)',
            fontSize: astryxTokens.fontSizes.xs,
          }}
        >
          {footer}
        </div>
      )}
    </div>
  );
};
