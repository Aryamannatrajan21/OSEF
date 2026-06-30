"use client";

import React, { useEffect, useState } from 'react';
import { Layers, ShieldCheck, Activity, BarChart, ShieldAlert } from 'lucide-react';

export function ArchitectureTab() {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    fetch('/api/stats')
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><Layers className="mr-3 text-[var(--accent)]" /> Architecture Overview</h2>
      
      {stats ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
            <h3 className="text-gray-400 text-sm mb-2 uppercase tracking-wider">Total Nodes</h3>
            <p className="text-4xl font-bold text-white">{stats.node_count}</p>
          </div>
          <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
            <h3 className="text-gray-400 text-sm mb-2 uppercase tracking-wider">Total Edges</h3>
            <p className="text-4xl font-bold text-white">{stats.edge_count}</p>
          </div>
          <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
            <h3 className="text-gray-400 text-sm mb-2 uppercase tracking-wider">Overall Confidence</h3>
            <p className="text-4xl font-bold text-[#10b981]">{(stats.overall_confidence * 100).toFixed(1)}%</p>
          </div>
        </div>
      ) : (
        <div className="animate-pulse flex space-x-4">
          <div className="flex-1 h-32 bg-white/5 rounded-lg"></div>
          <div className="flex-1 h-32 bg-white/5 rounded-lg"></div>
          <div className="flex-1 h-32 bg-white/5 rounded-lg"></div>
        </div>
      )}
    </div>
  );
}

export function ReasoningTab() {
  const [reasoning, setReasoning] = useState<any>(null);

  useEffect(() => {
    fetch('/api/reasoning')
      .then(res => res.json())
      .then(data => setReasoning(data));
  }, []);

  if (!reasoning) return <div className="p-8 text-white">Loading reasoning engine...</div>;

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><Activity className="mr-3 text-purple-400" /> Engineering Confidence Scores</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(reasoning).map(([key, value]: [string, any]) => {
          if (key === 'overall_confidence') return null;
          return (
            <div key={key} className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
              <h3 className="text-gray-300 text-lg capitalize mb-4">{key}</h3>
              <div className="flex items-center justify-between mb-2">
                <span className="text-gray-400 text-sm">{value.reasoning}</span>
                <span className={`text-xl font-bold ${value.score >= 0.9 ? 'text-green-400' : value.score >= 0.8 ? 'text-yellow-400' : 'text-red-400'}`}>
                  {(value.score * 100).toFixed(0)}%
                </span>
              </div>
              <div className="w-full bg-black/50 rounded-full h-2">
                <div 
                  className={`h-2 rounded-full ${value.score >= 0.9 ? 'bg-green-500' : value.score >= 0.8 ? 'bg-yellow-500' : 'bg-red-500'}`} 
                  style={{ width: `${value.score * 100}%` }}
                ></div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export function PoliciesTab() {
  const [violations, setViolations] = useState<any>(null);

  useEffect(() => {
    fetch('/api/policies')
      .then(res => res.json())
      .then(data => setViolations(data.violations || []));
  }, []);

  if (!violations) return <div className="p-8 text-white">Evaluating policies...</div>;

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><ShieldCheck className="mr-3 text-red-400" /> Policy Enforcement</h2>
      <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)] max-w-2xl">
        <div className="flex items-center mb-4">
          <ShieldAlert className="text-yellow-500 mr-3" size={24} />
          <h3 className="text-white text-lg">{violations.length} Policy Violations Detected</h3>
        </div>
        <ul className="space-y-4">
          {violations.map((v: any, idx: number) => (
            <li key={idx} className={`bg-black/40 p-4 rounded-md border ${v.severity === 'error' ? 'border-red-500/30' : 'border-yellow-500/30'}`}>
              <p className={`${v.severity === 'error' ? 'text-red-400' : 'text-yellow-400'} font-medium`}>{v.id}</p>
              <p className="text-gray-400 text-sm mt-1">{v.message}</p>
            </li>
          ))}
          {violations.length === 0 && (
            <li className="bg-black/40 p-4 rounded-md border border-green-500/30">
              <p className="text-green-400 font-medium">All Clear!</p>
              <p className="text-gray-400 text-sm mt-1">No violations found in the engineering baseline.</p>
            </li>
          )}
        </ul>
      </div>
    </div>
  );
}

export function BenchmarksTab() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<any>(null);

  const runBenchmarks = () => {
    setLoading(true);
    setResults(null); // Clear previous results so the UI flips back
    
    // Artificial delay so the benchmark feels like it's doing work (since the API returns in 1ms)
    setTimeout(() => {
      fetch('/api/benchmark')
        .then(res => res.json())
        .then(data => {
          setResults(data.metrics);
          setLoading(false);
        });
    }, 800);
  };

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><BarChart className="mr-3 text-blue-400" /> Benchmarks</h2>
      
      {!results ? (
        <div className="glass-panel p-8 rounded-lg border border-[var(--panel-border)] flex flex-col items-center justify-center h-64 text-center">
          <BarChart className={`text-gray-500 mb-4 ${loading ? 'animate-pulse text-blue-400' : ''}`} size={48} />
          <h3 className="text-white text-xl mb-2">{loading ? 'Running Suite...' : 'Benchmark Suite'}</h3>
          <p className="text-gray-400">Run the OSEF benchmark suite to populate this tab with latency and throughput metrics.</p>
          <button 
            onClick={runBenchmarks}
            disabled={loading}
            className={`mt-6 px-6 py-2 bg-[var(--accent)] hover:bg-blue-600 text-white rounded-md transition-colors ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {loading ? 'Profiling Engine...' : 'Run Benchmarks'}
          </button>
        </div>
      ) : (
        <div className="glass-panel p-8 rounded-lg border border-[var(--panel-border)]">
          <h3 className="text-white text-xl mb-6">Latest Benchmark Results</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {Object.entries(results).map(([key, val]: [string, any]) => (
              <div key={key} className="bg-black/30 p-4 rounded-md border border-white/5 flex justify-between items-center">
                <span className="text-gray-400 capitalize">{key.replace('_', ' ')}</span>
                <span className="text-white font-mono text-lg">{val}</span>
              </div>
            ))}
          </div>
          <button 
            onClick={runBenchmarks}
            disabled={loading}
            className={`mt-8 px-6 py-2 border border-[var(--accent)] text-[var(--accent)] hover:bg-[var(--accent)] hover:text-white rounded-md transition-colors ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {loading ? 'Profiling Engine...' : 'Run Again'}
          </button>
        </div>
      )}
    </div>
  );
}

export { AssistantTab } from './AssistantTab';
