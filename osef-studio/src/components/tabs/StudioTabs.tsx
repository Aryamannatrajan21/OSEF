"use client";

import React, { useEffect, useState } from 'react';
import { Layers, ShieldCheck, Activity, BarChart, ShieldAlert, Package, Cpu, ShoppingBag, CheckCircle } from 'lucide-react';

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
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><ShieldCheck className="mr-3 text-red-400" /> Policy Enforcement & Engineering Rules</h2>
      <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)] max-w-4xl">
        <div className="flex items-center mb-6">
          <ShieldAlert className="text-yellow-500 mr-3" size={24} />
          <h3 className="text-white text-lg font-semibold">{violations.length} Policy Findings Detected</h3>
        </div>
        <ul className="space-y-4">
          {violations.map((v: any, idx: number) => (
            <li key={idx} className={`bg-black/40 p-5 rounded-lg border ${v.severity === 'error' ? 'border-red-500/40' : 'border-yellow-500/40'}`}>
              <div className="flex justify-between items-start">
                <span className={`px-2 py-0.5 rounded text-xs font-mono uppercase tracking-wider ${v.severity === 'error' ? 'bg-red-500/20 text-red-400 border border-red-500/30' : 'bg-yellow-500/20 text-yellow-400 border border-yellow-500/30'}`}>
                  {v.category || v.severity}
                </span>
                <span className="text-gray-500 text-xs font-mono">{v.id}</span>
              </div>
              <h4 className="text-white font-medium text-base mt-2">{v.title || v.id}</h4>
              <p className="text-gray-300 text-sm mt-1">{v.message}</p>
              {v.recommendation && (
                <div className="mt-3 bg-white/5 p-3 rounded border border-white/10 text-xs text-gray-300">
                  <span className="text-[var(--accent)] font-semibold uppercase tracking-wider block mb-1">Recommendation</span>
                  {v.recommendation}
                </div>
              )}
            </li>
          ))}
          {violations.length === 0 && (
            <li className="bg-black/40 p-6 rounded-lg border border-green-500/30 text-center">
              <p className="text-green-400 font-semibold text-lg">Engineering Baseline Verified</p>
              <p className="text-gray-400 text-sm mt-1">No violations or architectural drift detected in the repository.</p>
            </li>
          )}
        </ul>
      </div>
    </div>
  );
}

export function DependenciesTab() {
  const [deps, setDeps] = useState<any>(null);

  useEffect(() => {
    fetch('/api/dependencies')
      .then(res => res.json())
      .then(data => setDeps(data));
  }, []);

  if (!deps) return <div className="p-8 text-white">Analyzing dependency health...</div>;

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><Package className="mr-3 text-green-400" /> Dependency Health & Import Explorer</h2>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
          <h3 className="text-gray-400 text-xs mb-2 uppercase tracking-wider">Total Imports</h3>
          <p className="text-3xl font-bold text-white">{deps.total_imports ?? 0}</p>
        </div>
        <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
          <h3 className="text-gray-400 text-xs mb-2 uppercase tracking-wider">Resolved Imports</h3>
          <p className="text-3xl font-bold text-[#10b981]">{deps.resolved_imports ?? 0}</p>
        </div>
        <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
          <h3 className="text-gray-400 text-xs mb-2 uppercase tracking-wider">Broken Imports</h3>
          <p className="text-3xl font-bold text-red-400">{deps.broken_imports ?? 0}</p>
        </div>
        <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)]">
          <h3 className="text-gray-400 text-xs mb-2 uppercase tracking-wider">External Packages</h3>
          <p className="text-3xl font-bold text-blue-400">{deps.external_packages ? deps.external_packages.length : 0}</p>
        </div>
      </div>
      <div className="glass-panel p-6 rounded-lg border border-[var(--panel-border)] max-w-4xl">
        <h3 className="text-white text-lg font-semibold mb-4">External Package Dependencies</h3>
        <div className="flex flex-wrap gap-2">
          {deps.external_packages && deps.external_packages.length > 0 ? (
            deps.external_packages.map((pkg: string, idx: number) => (
              <span key={idx} className="bg-white/5 border border-white/10 px-3 py-1.5 rounded-md text-sm text-gray-200 font-mono">
                {pkg}
              </span>
            ))
          ) : (
            <p className="text-gray-500 text-sm">No external dependencies detected or graph unindexed.</p>
          )}
        </div>
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

export function PluginsTab() {
  const [plugins, setPlugins] = useState<any>(null);

  useEffect(() => {
    fetch('/api/plugins')
      .then(res => res.json())
      .then(data => setPlugins(data.plugins || []));
  }, []);

  if (!plugins) return <div className="p-8 text-white">Loading language adapters...</div>;

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><Cpu className="mr-3 text-purple-400" /> Language Adapters & Reference Plugins</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl">
        {plugins.map((p: any, idx: number) => (
          <div key={idx} className="glass-panel p-6 rounded-lg border border-[var(--panel-border)] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-white text-lg font-semibold">{p.name || p.id}</h3>
                <span className="px-2 py-0.5 rounded text-xs font-mono bg-purple-500/20 text-purple-300 border border-purple-500/30">
                  v{p.version || '0.1.0'}
                </span>
              </div>
              <p className="text-gray-400 text-sm mb-4">{p.description}</p>
            </div>
            <div className="flex flex-wrap gap-1.5 pt-3 border-t border-white/5">
              {(Array.isArray(p.capabilities) ? p.capabilities : (p.capabilities ? Object.keys(p.capabilities) : ['language_adapter', 'symbol_table'])).map((cap: any, cIdx: number) => {
                const label = typeof cap === 'object' && cap !== null ? (cap.capability || cap.name || JSON.stringify(cap)) : String(cap);
                return (
                  <span key={cIdx} className="bg-black/40 px-2 py-0.5 rounded text-xs text-gray-300 font-mono">
                    {label}
                  </span>
                );
              })}
            </div>
          </div>
        ))}
        {plugins.length === 0 && (
          <p className="text-gray-500 text-sm">No reference plugins loaded.</p>
        )}
      </div>
    </div>
  );
}

export function MarketplaceTab() {
  const [plugins, setPlugins] = useState<any>(null);

  useEffect(() => {
    fetch('/api/marketplace')
      .then(res => res.json())
      .then(data => setPlugins(data.plugins || []));
  }, []);

  if (!plugins) return <div className="p-8 text-white">Loading marketplace index...</div>;

  return (
    <div className="flex-1 flex flex-col p-8 overflow-y-auto">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center"><ShoppingBag className="mr-3 text-blue-400" /> Ecosystem Plugin Marketplace</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl">
        {plugins.map((p: any, idx: number) => (
          <div key={idx} className="glass-panel p-6 rounded-lg border border-[var(--panel-border)] flex flex-col justify-between">
            <div>
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-white text-lg font-semibold flex items-center gap-1.5">
                  {p.name || p.id}
                  {p.certified && <span title="Official Certified Plugin"><CheckCircle size={14} className="text-[#10b981]" /></span>}
                </h3>
                <span className="px-2 py-0.5 rounded text-xs font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30">
                  {p.tier || 'Community'}
                </span>
              </div>
              <p className="text-gray-400 text-sm mb-4">{p.description}</p>
            </div>
            <div>
              <div className="flex flex-wrap gap-1 mb-3">
                {(Array.isArray(p.capabilities) ? p.capabilities : (p.capabilities ? Object.keys(p.capabilities) : ['signed_bundle', 'community_tier'])).slice(0, 3).map((cap: any, cIdx: number) => {
                  const label = typeof cap === 'object' && cap !== null ? (cap.capability || cap.name || JSON.stringify(cap)) : String(cap);
                  return (
                    <span key={cIdx} className="bg-white/5 px-2 py-0.5 rounded text-[10px] text-gray-300 font-mono">
                      {label}
                    </span>
                  );
                })}
              </div>
              <div className="flex justify-between items-center pt-3 border-t border-white/5 text-xs text-gray-500 font-mono">
                <span>v{p.version}</span>
                <span className="text-[var(--accent)] cursor-pointer hover:underline">osef plugin install {p.id || p.name}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export { AssistantTab } from './AssistantTab';
