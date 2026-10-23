export interface MCQItem {
  num: number;
  tag: 'NB' | 'TH' | 'VD' | 'VDC';
  stem: string;
  a: string;
  b: string;
  c: string;
  d: string;
  cols?: 1 | 2 | 4;
}

export interface MCQAnswer {
  num: number;
  ans: string;
  explain: string;
}

export interface TFItem {
  num: number;
  meta: string;
  stem: string;
  svg?: string;
  a: string;
  b: string;
  c: string;
  d: string;
}

export interface ShortAnswerItem {
  num: number;
  tag: string;
  stem: string;
  ans: string;
  guide: string;
}

export interface EssayItem {
  num: number;
  tag: string;
  stem: string;
  solution: string;
}
