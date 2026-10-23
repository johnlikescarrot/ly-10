import React from 'react';
import { astryxTokens } from './tokens.js';
import { Badge } from './Badge.js';
import { MCQuestion, TFQuestion, ShortAnswerQuestion, EssayQuestion } from '../types/index.js';

export interface MCQCardProps {
  question: MCQuestion;
  showSolution?: boolean;
}

export const MCQCard: React.FC<MCQCardProps> = ({ question, showSolution = true }) => {
  return (
    <div
      style={{
        border: `1px solid ${astryxTokens.colors.border}`,
        borderRadius: astryxTokens.radii.md,
        padding: '10px 12px',
        marginBottom: '10px',
        backgroundColor: astryxTokens.colors.white,
        pageBreakInside: 'avoid',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontWeight: 700, color: astryxTokens.colors.primary, fontSize: astryxTokens.fontSizes.sm }}>
            Câu {question.number}.
          </span>
          <Badge variant="info" size="sm">{question.lessonName}</Badge>
        </div>
        <Badge variant={question.level === 'Nhận biết' ? 'success' : question.level === 'Thông hiểu' ? 'primary' : 'warning'} size="sm">
          {question.level}
        </Badge>
      </div>

      <div style={{ fontSize: astryxTokens.fontSizes.sm, marginBottom: '8px', fontWeight: 500, color: astryxTokens.colors.textDark }}>
        {question.content}
      </div>

      {question.image && (
        <div style={{ textAlign: 'center', margin: '8px 0' }}>
          <img src={question.image} alt={`Hình câu ${question.number}`} style={{ maxWidth: '100%', maxHeight: '180px', borderRadius: '4px' }} />
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px 12px', fontSize: astryxTokens.fontSizes.sm, marginBottom: '8px' }}>
        {question.options.map((opt) => {
          const isCorrect = showSolution && opt.label === question.correctOption;
          return (
            <div
              key={opt.label}
              style={{
                padding: '4px 8px',
                borderRadius: astryxTokens.radii.sm,
                backgroundColor: isCorrect ? astryxTokens.colors.emeraldBg : 'transparent',
                border: isCorrect ? `1px solid ${astryxTokens.colors.emeraldBorder}` : '1px solid transparent',
                fontWeight: isCorrect ? 700 : 400,
                color: isCorrect ? astryxTokens.colors.emerald : astryxTokens.colors.textDark,
              }}
            >
              <strong>{opt.label}.</strong> {opt.text}
            </div>
          );
        })}
      </div>

      {showSolution && (
        <div
          style={{
            backgroundColor: '#F8FAFC',
            borderTop: `1px dashed ${astryxTokens.colors.border}`,
            paddingTop: '6px',
            marginTop: '6px',
            fontSize: astryxTokens.fontSizes.xs,
            color: astryxTokens.colors.textMuted,
          }}
        >
          <span style={{ fontWeight: 700, color: astryxTokens.colors.emerald }}>
            ✓ Đáp án: {question.correctOption}
          </span>
          <span style={{ margin: '0 6px' }}>|</span>
          <span>{question.explanation}</span>
        </div>
      )}
    </div>
  );
};

export interface TFCardProps {
  question: TFQuestion;
  showSolution?: boolean;
}

export const TFCard: React.FC<TFCardProps> = ({ question, showSolution = true }) => {
  return (
    <div
      style={{
        border: `1px solid ${astryxTokens.colors.primaryBorder}`,
        borderRadius: astryxTokens.radii.md,
        padding: '12px',
        marginBottom: '12px',
        backgroundColor: astryxTokens.colors.white,
        pageBreakInside: 'avoid',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontWeight: 700, color: astryxTokens.colors.navy, fontSize: astryxTokens.fontSizes.sm }}>
            Câu {question.number} [{question.code}]: {question.title}
          </span>
          <Badge variant="info" size="sm">{question.lessonName}</Badge>
        </div>
        <Badge variant="primary" size="sm">{question.level}</Badge>
      </div>

      <div style={{ fontSize: astryxTokens.fontSizes.sm, marginBottom: '8px', color: astryxTokens.colors.textDark, fontStyle: 'italic' }}>
        {question.scenario}
      </div>

      {question.image && (
        <div style={{ textAlign: 'center', margin: '8px 0' }}>
          <img src={question.image} alt={`Hình câu ${question.number}`} style={{ maxWidth: '100%', maxHeight: '200px', borderRadius: '4px' }} />
        </div>
      )}

      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: astryxTokens.fontSizes.sm, marginTop: '8px' }}>
        <thead>
          <tr style={{ backgroundColor: astryxTokens.colors.primaryLight, borderBottom: `1px solid ${astryxTokens.colors.primaryBorder}` }}>
            <th style={{ padding: '6px', textAlign: 'left', width: '70%' }}>Mệnh đề</th>
            <th style={{ padding: '6px', textAlign: 'center', width: '15%' }}>Đ/S</th>
            <th style={{ padding: '6px', textAlign: 'left', width: '15%' }}>Ghi chú giải thích</th>
          </tr>
        </thead>
        <tbody>
          {question.statements.map((stmt) => (
            <tr key={stmt.key} style={{ borderBottom: `1px solid ${astryxTokens.colors.border}` }}>
              <td style={{ padding: '6px 8px' }}>
                <strong>{stmt.key})</strong> {stmt.text}
              </td>
              <td style={{ padding: '6px', textAlign: 'center' }}>
                {showSolution ? (
                  <span
                    style={{
                      fontWeight: 800,
                      color: stmt.isCorrect ? astryxTokens.colors.emerald : astryxTokens.colors.rose,
                      backgroundColor: stmt.isCorrect ? astryxTokens.colors.emeraldBg : astryxTokens.colors.roseBg,
                      padding: '2px 8px',
                      borderRadius: '4px',
                    }}
                  >
                    {stmt.isCorrect ? 'ĐÚNG' : 'SAI'}
                  </span>
                ) : (
                  '[  ]'
                )}
              </td>
              <td style={{ padding: '6px', fontSize: astryxTokens.fontSizes.xs, color: astryxTokens.colors.textMuted }}>
                {showSolution ? stmt.explanation : ''}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export interface SACardProps {
  question: ShortAnswerQuestion;
  showSolution?: boolean;
}

export const SACard: React.FC<SACardProps> = ({ question, showSolution = true }) => {
  return (
    <div
      style={{
        border: `1px solid ${astryxTokens.colors.amberBorder}`,
        borderRadius: astryxTokens.radii.md,
        padding: '10px 12px',
        marginBottom: '10px',
        backgroundColor: astryxTokens.colors.white,
        pageBreakInside: 'avoid',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontWeight: 700, color: astryxTokens.colors.amber, fontSize: astryxTokens.fontSizes.sm }}>
            Câu {question.number} (Trả lời ngắn).
          </span>
          <Badge variant="warning" size="sm">{question.lessonName}</Badge>
        </div>
        <Badge variant="warning" size="sm">{question.level}</Badge>
      </div>

      <div style={{ fontSize: astryxTokens.fontSizes.sm, marginBottom: '6px', color: astryxTokens.colors.textDark }}>
        {question.content}
      </div>

      {showSolution && (
        <div style={{ backgroundColor: astryxTokens.colors.amberBg, padding: '8px 10px', borderRadius: '4px', fontSize: astryxTokens.fontSizes.xs }}>
          <span style={{ fontWeight: 700, color: '#92400E' }}>
            ► Đáp số điền phiếu: {question.correctAnswer} {question.unit ? question.unit : ''}
          </span>
          <div style={{ marginTop: '4px', color: astryxTokens.colors.textDark }}>
            <em>Các bước tính toán:</em> {question.calculationSteps}
          </div>
        </div>
      )}
    </div>
  );
};

export interface EssayCardProps {
  question: EssayQuestion;
  showSolution?: boolean;
}

export const EssayCard: React.FC<EssayCardProps> = ({ question, showSolution = true }) => {
  return (
    <div
      style={{
        border: `1px solid ${astryxTokens.colors.teal}`,
        borderRadius: astryxTokens.radii.lg,
        padding: '12px 14px',
        marginBottom: '14px',
        backgroundColor: astryxTokens.colors.white,
        pageBreakInside: 'avoid',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontWeight: 700, color: astryxTokens.colors.teal, fontSize: astryxTokens.fontSizes.base }}>
            Bài {question.number} [{question.code}] ({question.totalPoints.toFixed(2)} điểm)
          </span>
          <Badge variant="info" size="sm">{question.lessonName}</Badge>
        </div>
        <Badge variant="info" size="sm">{question.level}</Badge>
      </div>

      <div style={{ fontSize: astryxTokens.fontSizes.sm, marginBottom: '8px', color: astryxTokens.colors.textDark }}>
        {question.content}
      </div>

      {question.parts && (
        <div style={{ marginLeft: '12px', fontSize: astryxTokens.fontSizes.sm, marginBottom: '8px' }}>
          {question.parts.map((p, idx) => (
            <div key={idx} style={{ marginBottom: '4px' }}>
              <strong>{p.label})</strong> {p.text} <em>({p.points.toFixed(2)} đ)</em>
            </div>
          ))}
        </div>
      )}

      {showSolution && (
        <div style={{ backgroundColor: astryxTokens.colors.tealBg, borderLeft: `3px solid ${astryxTokens.colors.teal}`, padding: '10px 12px', borderRadius: '4px', marginTop: '8px' }}>
          <div style={{ fontWeight: 700, color: astryxTokens.colors.teal, fontSize: astryxTokens.fontSizes.sm, marginBottom: '4px' }}>
            Lời giải chi tiết & Biểu điểm chấm:
          </div>
          <div style={{ fontSize: astryxTokens.fontSizes.xs, whiteSpace: 'pre-line', lineHeight: 1.5 }}>
            {question.detailedSolution}
          </div>
          <div style={{ marginTop: '8px', borderTop: `1px dashed ${astryxTokens.colors.border}`, paddingTop: '6px' }}>
            <span style={{ fontWeight: 700, fontSize: astryxTokens.fontSizes.xs }}>Thang điểm từng bước:</span>
            <ul style={{ margin: '4px 0 0 16px', padding: 0, fontSize: astryxTokens.fontSizes.xs }}>
              {question.markScheme.map((ms, idx) => (
                <li key={idx}>
                  {ms.step} — <strong style={{ color: astryxTokens.colors.teal }}>[{ms.points.toFixed(2)} đ]</strong>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
