import React from 'react';
import { astryxTokens } from './tokens.js';

export interface CalloutProps {
  type?: 'mantra' | 'trap' | 'tip' | 'info';
  title: string;
  children: React.ReactNode;
  icon?: string;
}

export const Callout: React.FC<CalloutProps> = ({
  type = 'info',
  title,
  children,
  icon,
}) => {
  let bg = astryxTokens.colors.primaryLight;
  let border = astryxTokens.colors.primary;
  let titleColor = astryxTokens.colors.primary;
  let defaultIcon = '💡';

  if (type === 'mantra') {
    bg = astryxTokens.colors.amberBg;
    border = astryxTokens.colors.amber;
    titleColor = '#92400E';
    defaultIcon = '⚡';
  } else if (type === 'trap') {
    bg = astryxTokens.colors.roseBg;
    border = astryxTokens.colors.rose;
    titleColor = '#991B1B';
    defaultIcon = '⚠️';
  } else if (type === 'tip') {
    bg = astryxTokens.colors.emeraldBg;
    border = astryxTokens.colors.emerald;
    titleColor = '#166534';
    defaultIcon = '🎯';
  }

  return (
    <div
      style={{
        backgroundColor: bg,
        borderLeft: `4px solid ${border}`,
        borderRadius: `0 ${astryxTokens.radii.md} ${astryxTokens.radii.md} 0`,
        padding: '10px 14px',
        marginBottom: astryxTokens.spacing.md,
        fontSize: astryxTokens.fontSizes.sm,
        lineHeight: 1.5,
        pageBreakInside: 'avoid',
      }}
    >
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          fontWeight: 700,
          color: titleColor,
          marginBottom: '4px',
        }}
      >
        <span>{icon || defaultIcon}</span>
        <span>{title}</span>
      </div>
      <div>{children}</div>
    </div>
  );
};
