import React from 'react';
import { astryxTokens } from './tokens.js';

export interface BadgeProps {
  variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'danger' | 'info';
  children: React.ReactNode;
  size?: 'sm' | 'md';
}

export const Badge: React.FC<BadgeProps> = ({
  variant = 'primary',
  children,
  size = 'md',
}) => {
  let bg = astryxTokens.colors.primaryLight;
  let color = astryxTokens.colors.primary;
  let border = astryxTokens.colors.primaryBorder;

  if (variant === 'secondary') {
    bg = astryxTokens.colors.slateBg;
    color = astryxTokens.colors.slate;
    border = astryxTokens.colors.border;
  } else if (variant === 'success') {
    bg = astryxTokens.colors.emeraldBg;
    color = astryxTokens.colors.emerald;
    border = astryxTokens.colors.emeraldBorder;
  } else if (variant === 'warning') {
    bg = astryxTokens.colors.amberBg;
    color = astryxTokens.colors.amber;
    border = astryxTokens.colors.amberBorder;
  } else if (variant === 'danger') {
    bg = astryxTokens.colors.roseBg;
    color = astryxTokens.colors.rose;
    border = astryxTokens.colors.roseBorder;
  } else if (variant === 'info') {
    bg = '#F0FDFA';
    color = astryxTokens.colors.teal;
    border = '#99F6E4';
  }

  const padding = size === 'sm' ? '2px 6px' : '3px 9px';
  const fontSize = size === 'sm' ? astryxTokens.fontSizes.xs : astryxTokens.fontSizes.sm;

  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        backgroundColor: bg,
        color: color,
        border: `1px solid ${border}`,
        borderRadius: astryxTokens.radii.sm,
        padding: padding,
        fontSize: fontSize,
        fontWeight: 600,
        lineHeight: 1.2,
      }}
    >
      {children}
    </span>
  );
};
