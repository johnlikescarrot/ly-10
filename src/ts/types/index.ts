export type CognitiveLevel = 'Nhận biết' | 'Thông hiểu' | 'Vận dụng' | 'Vận dụng cao';

export type QuestionType = 'mcq' | 'true_false' | 'short_answer' | 'essay';

export interface MCQOption {
  label: 'A' | 'B' | 'C' | 'D';
  text: string;
}

export interface MCQuestion {
  id: string;
  number: number;
  lessonId: string;
  lessonName: string;
  content: string;
  options: MCQOption[];
  correctOption: 'A' | 'B' | 'C' | 'D';
  explanation: string;
  level: CognitiveLevel;
  image?: string;
}

export interface TFStatement {
  key: 'a' | 'b' | 'c' | 'd';
  text: string;
  isCorrect: boolean;
  explanation: string;
}

export interface TFQuestion {
  id: string;
  number: number;
  code: string; // e.g. '2-I' or '2-II'
  lessonId: string;
  lessonName: string;
  title: string;
  scenario: string;
  statements: TFStatement[];
  level: string;
  image?: string;
}

export interface ShortAnswerQuestion {
  id: string;
  number: number;
  lessonId: string;
  lessonName: string;
  content: string;
  correctAnswer: string;
  unit?: string;
  calculationSteps: string;
  level: CognitiveLevel;
  image?: string;
}

export interface EssayPart {
  label: string;
  text: string;
  points: number;
}

export interface MarkSchemeStep {
  step: string;
  points: number;
}

export interface EssayQuestion {
  id: string;
  number: number;
  code: string;
  lessonId: string;
  lessonName: string;
  content: string;
  parts?: EssayPart[];
  totalPoints: number;
  detailedSolution: string;
  markScheme: MarkSchemeStep[];
  level: CognitiveLevel;
  image?: string;
}

export interface FormulaItem {
  category: string;
  name: string;
  symbolFormula: string;
  notes: string;
}

export interface MantraItem {
  index: number;
  title: string;
  mnemonic: string;
  application: string;
}

export interface LessonTheory {
  id: string;
  number: number;
  title: string;
  chapter: string;
  keyConcepts: string[];
  formulas: FormulaItem[];
  commonTraps: string[];
  visualAsset?: string;
}

export interface MatrixRow {
  lessonNumber: number;
  lessonName: string;
  chapter: string;
  mcqKnow: number;
  mcqUnderstand: number;
  tfKnow: number;
  tfUnderstand: number;
  saKnow: number;
  saUnderstand: number;
  essayUnderstand: number;
  essayApply: number;
  essayVdc: number;
  totalPoints: number;
}

export interface MockExam {
  id: string;
  title: string;
  code: string;
  durationMinutes: number;
  totalPoints: number;
  part1: MCQuestion[];
  part2: TFQuestion[];
  part3: ShortAnswerQuestion[];
  part4: EssayQuestion[];
}
