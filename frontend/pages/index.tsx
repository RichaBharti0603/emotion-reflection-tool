import { useState } from 'react';
import styles from '../styles/Home.module.css';

export default function Home() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ emotion: string; confidence: number } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const res = await fetch('https://emotion-reflection-tool.onrender.com/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) throw new Error('API Error');

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError('Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>🧠 Emotion Reflection Tool</h1>
      <textarea
        placeholder="How are you feeling today?"
        className={styles.textarea}
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button className={styles.button} onClick={handleSubmit} disabled={loading || !text}>
        {loading ? 'Analyzing...' : 'Reflect Emotion'}
      </button>

      {result && (
        <div className={styles.result}>
          <p><strong>Emotion:</strong> {result.emotion}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(1)}%</p>
        </div>
      )}

      {error && <p className={styles.error}>{error}</p>}
    </div>
  );
}
