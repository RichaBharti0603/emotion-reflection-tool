import { useState } from 'react';
import styles from '../styles/Home.module.css';

interface EmotionResult {
  emotion: string;
  confidence: number;
}

function getEmoji(emotion: string) {
  const map: Record<string, string> = {
    Happy: '😊',
    Sad: '😢',
    Angry: '😠',
    Excited: '🤩',
    Anxious: '😰',
  };
  return map[emotion] || '😶';
}

export default function Home() {
  const [text, setText] = useState('');
  const [result, setResult] = useState<EmotionResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError('');

    try {
      const res = await fetch('https://emotion-reflection-tool.onrender.com/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data);
    } catch{
      setError('Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className={styles.main}>
      <div className={styles.card}>
        <h1 className={styles.title}>🧠 Emotion Reflector</h1>
        <p className={styles.subtitle}>Reflect how you feel in words, we’ll tell you the vibe.</p>


<h2 className={styles.subheading}>How are you feeling today?</h2>
<div className={styles.moodSelector}>
  <span onClick={() => setText("I feel happy 😊")} className={styles.emoji}>😊</span>
  <span onClick={() => setText("I feel okay 😐")} className={styles.emoji}>😐</span>
  <span onClick={() => setText("I feel sad 😢")} className={styles.emoji}>😢</span>
</div>

        <form onSubmit={handleSubmit} className={styles.form}>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="I feel nervous about my first job interview..."
            required
            className={styles.textarea}
            rows={4}
          />
          <button type="submit" className={styles.button} disabled={loading}>
            {loading ? 'Analyzing...' : 'Reflect Emotion'}
          </button>
        </form>

        {error && <p className={styles.error}>{error}</p>}

        {result && (
          <div className={styles.resultBox}>
            <div className={styles.emoji}>{getEmoji(result.emotion)}</div>
            <h2 className={styles.resultText}>{result.emotion}</h2>
            <p className={styles.confidence}>Confidence: {(result.confidence * 100).toFixed(0)}%</p>
          </div>
        )}
      </div>
    </main>
  );
}
