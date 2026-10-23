import React from 'react';
import { astryxTokens } from './tokens.js';

export interface HeadingProps {
  level: 1 | 2 | 3 | 4;
  visualRole?: 'hero' | 'section' | 'subsection' | 'card' | 'badge-title';
  children: React.ReactNode;
  subtitle?: string;
  badgeText?: string;
  className?: string;
}

export const Heading: React.FC<HeadingProps> = ({
  level,
  visualRole = 'section',
  children,
  subtitle,
  badgeText,
  className = '',
}) => {
  if (level === 1 || visualRole === 'hero') {
    return (
      <div
        className={`astryx-heading-hero ${className}`}
        style={{
          backgroundColor: astryxTokens.colors.navy,
          color: astryxTokens.colors.white,
          borderRadius: astryxTokens.radii.lg,
          padding: `${astryxTokens.spacing.md} ${astryxTokens.spacing.lg}`,
          marginBottom: astryxTokens.spacing.md,
          boxShadow: astryxTokens.shadows.md,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <div>
          <h1
            style={{
              margin: 0,
              fontSize: astryxTokens.fontSizes['2xl'],
              fontWeight: 800,
              color: '#FACC15', // Gold yellow
              letterSpacing: '-0.01em',
              lineHeight: 1.2,
            }}
          >
            {children}
          </h1>
          {subtitle && (
            <div style={{ fontSize: astryxTokens.fontSizes.sm, color: '#CBD5E1', marginTop: '4px' }}>
              {subtitle}
            </div>
          )}
        </div>
        {badgeText && (
          <span
            style={{
              backgroundColor: astryxTokens.colors.primary,
              color: astryxTokens.colors.white,
              fontSize: astryxTokens.fontSizes.xs,
              fontWeight: 700,
              padding: '4px 10px',
              borderRadius: astryxTokens.radii.full,
              textTransform: 'uppercase',
              letterSpacing: '0.05em',
            }}
          >
            {badgeText}
          </span>
        )}
      </div>
    );
  }

  if (level === 2 || visualRole === 'section') {
    return (
      <div
        className={`astryx-heading-section ${className}`}
        style={{
          borderLeft: `5px solid ${astryxTokens.colors.primary}`,
          borderBottom: `1px solid ${astryxTokens.colors.primaryBorder}`,
          backgroundColor: astryxTokens.colors.primaryLight,
          padding: `8px 14px`,
          borderRadius: `0 ${astryxTokens.radii.md} ${astryxTokens.radii.md} 0`,
          marginTop: astryxTokens.spacing.lg,
          marginBottom: astryxTokens.spacing.md,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          pageBreakAfter: 'avoid',
        }}
      >
        <h2
          style={{
            margin: 0,
            fontSize: astryxTokens.fontSizes.lg,
            fontWeight: 700,
            color: astryxTokens.colors.navy,
          }}
        >
          {children}
        </h2>
        {badgeText && (
          <span
            style={{
              backgroundColor: astryxTokens.colors.teal,
              color: astryxTokens.colors.white,
              fontSize: astryxTokens.fontSizes.xs,
              fontWeight: 600,
              padding: '3px 8px',
              borderRadius: astryxTokens.radii.sm,
            }}
          >
            {badgeText}
          </span>
        )}
      </div>
    );
  }

  return (
    <h3
      style={{
        fontSize: astryxTokens.fontSizes.base,
        fontWeight: 700,
        color: astryxTokens.colors.teal,
        marginTop: astryxTokens.spacing.md,
        marginBottom: astryxTokens.spacing.xs,
        pageBreakAfter: 'avoid',
      }}
    >
      ▸ {children}
    </h3>
  );
};
