"use client";

import React, { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import NodeSidebar from '@/components/sidebar/NodeSidebar';
import { Search, Activity, Layers, ShieldCheck, Box, Settings, X } from 'lucide-react';
import { ArchitectureTab, ReasoningTab, PoliciesTab, BenchmarksTab } from '@/components/tabs/StudioTabs';

// ForceGraph must be dynamically imported with ssr: false because it uses canvas/window APIs
const ForceGraph = dynamic(() => import('@/components/graph/ForceGraph'), { 
  ssr: false,
  loading: () => (
    <div className="absolute inset-0 flex flex-col items-center justify-center text-[var(--accent)]">
      <div className="w-8 h-8 border-4 border-current border-t-transparent rounded-full animate-spin mb-4"></div>
      <p className="font-mono text-sm uppercase tracking-widest text-gray-400">Loading Engineering Intelligence Engine...</p>
    </div>
  )
});

export default function OsefStudio() {
  const [graphData, setGraphData] = useState<any>(null);
  const [selectedNode, setSelectedNode] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<string>('Graph');
  const [isHealthOpen, setIsHealthOpen] = useState(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    // Fetch EKG from local FastAPI server
    fetch('http://localhost:8000/api/graph')
      .then(res => {
        if (!res.ok) throw new Error('API server not running. Did you run `osef ui`?');
        return res.json();
      })
      .then(data => {
        if (data.error) throw new Error(data.error);
        setGraphData(data);
      })
      .catch(err => {
        console.error(err);
        setError(err.message);
      });
  }, []);

  const TABS = ['Graph', 'Architecture', 'Reasoning', 'Policies', 'Benchmarks'];

  return (
    <main className="w-screen h-screen relative bg-[var(--background)] overflow-hidden">
      
      {/* Top Navigation Bar */}
      <nav className="absolute top-0 left-0 w-full h-14 glass-panel border-b z-40 flex items-center justify-between px-6">
        <div className="flex items-center space-x-6">
          <div className="flex items-center space-x-2 text-white font-semibold tracking-wide">
            <Box size={20} className="text-[var(--accent)]" />
            <span>OSEF Studio</span>
          </div>
          <div className="h-4 w-[1px] bg-white/20"></div>
          <div className="flex items-center space-x-4 text-sm text-gray-400">
            {TABS.map(tab => (
              <button 
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`transition-colors ${activeTab === tab ? 'text-white font-medium' : 'hover:text-white'}`}
              >
                {tab}
              </button>
            ))}
          </div>
        </div>

        {/* Global Search */}
        <div className="flex-1 max-w-md mx-8 relative">
          <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500" />
          <input 
            type="text" 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search classes, policies, findings..." 
            className="w-full bg-black/40 border border-[var(--panel-border)] rounded-md py-1.5 pl-9 pr-4 text-sm text-gray-200 placeholder-gray-500 focus:outline-none focus:border-[var(--accent)] transition-colors"
          />
        </div>

        <div className="flex items-center space-x-4 text-gray-400">
          <button onClick={() => setIsHealthOpen(true)} className="hover:text-white transition-colors" title="System Health"><Activity size={18} /></button>
          <button onClick={() => setIsSettingsOpen(true)} className="hover:text-white transition-colors" title="Settings"><Settings size={18} /></button>
        </div>
      </nav>

      {/* Main Content Area */}
      <div className="absolute inset-0 pt-14 flex flex-col">
        {error ? (
          <div className="flex h-full items-center justify-center">
            <div className="glass-panel p-6 rounded-lg max-w-md text-center border-red-900/50">
              <ShieldCheck size={48} className="mx-auto text-red-500 mb-4" />
              <h3 className="text-white font-semibold mb-2">Connection Refused</h3>
              <p className="text-sm text-gray-400 mb-4">{error}</p>
              <code className="bg-black/50 px-3 py-2 rounded text-[var(--accent)] text-xs font-mono">
                osef ui
              </code>
              <p className="text-xs text-gray-500 mt-4">Run the command above in your terminal to start the API.</p>
            </div>
          </div>
        ) : activeTab === 'Graph' ? (
          <ForceGraph data={graphData} onNodeClick={setSelectedNode} searchQuery={searchQuery} />
        ) : activeTab === 'Architecture' ? (
          <ArchitectureTab />
        ) : activeTab === 'Reasoning' ? (
          <ReasoningTab />
        ) : activeTab === 'Policies' ? (
          <PoliciesTab />
        ) : activeTab === 'Benchmarks' ? (
          <BenchmarksTab />
        ) : (
          <div className="flex-1 flex flex-col items-center justify-center text-gray-500">
            <Layers size={48} className="mb-4 text-gray-600 opacity-50" />
            <p>Select a node to inspect or switch tabs</p>
          </div>
        )}
      </div>

      {/* Right Sidebar for Node Details (Only visible in Graph view) */}
      {activeTab === 'Graph' && (
        <NodeSidebar node={selectedNode} onClose={() => setSelectedNode(null)} />
      )}      

      {/* System Health Modal */}
      {isHealthOpen && (
        <div className="absolute inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
          <div className="glass-panel w-96 rounded-xl overflow-hidden flex flex-col border border-[var(--panel-border)] shadow-2xl">
            <div className="p-4 border-b border-[var(--panel-border)] flex justify-between items-center bg-black/40">
              <h3 className="text-white font-semibold flex items-center"><Activity size={16} className="mr-2 text-[var(--accent)]" /> System Health</h3>
              <button onClick={() => setIsHealthOpen(false)} className="text-gray-400 hover:text-white"><X size={16} /></button>
            </div>
            <div className="p-6 space-y-4 text-sm">
              <div className="flex justify-between items-center">
                <span className="text-gray-400">API Status</span>
                <span className="text-green-400 flex items-center"><div className="w-2 h-2 rounded-full bg-green-500 mr-2 animate-pulse"></div> Online</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-gray-400">Graph Engine</span>
                <span className="text-green-400">Stable</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-gray-400">Last Sync</span>
                <span className="text-white">Just now</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Settings Modal */}
      {isSettingsOpen && (
        <div className="absolute inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
          <div className="glass-panel w-96 rounded-xl overflow-hidden flex flex-col border border-[var(--panel-border)] shadow-2xl">
            <div className="p-4 border-b border-[var(--panel-border)] flex justify-between items-center bg-black/40">
              <h3 className="text-white font-semibold flex items-center"><Settings size={16} className="mr-2 text-gray-400" /> Settings</h3>
              <button onClick={() => setIsSettingsOpen(false)} className="text-gray-400 hover:text-white"><X size={16} /></button>
            </div>
            <div className="p-6 space-y-4 text-sm">
              <div className="space-y-3">
                <label className="text-gray-400 flex justify-between items-center cursor-pointer">
                  <span>Dark Mode</span>
                  <input type="checkbox" defaultChecked className="rounded border-gray-600 bg-gray-700 w-4 h-4" />
                </label>
                <label className="text-gray-400 flex justify-between items-center cursor-pointer">
                  <span>Cinematic 3D Mode</span>
                  <input type="checkbox" className="rounded border-gray-600 bg-gray-700 w-4 h-4" />
                </label>
                <label className="text-gray-400 flex justify-between items-center cursor-pointer">
                  <span>Auto-Refresh Graph</span>
                  <input type="checkbox" defaultChecked className="rounded border-gray-600 bg-gray-700 w-4 h-4" />
                </label>
              </div>
              <div className="pt-4 border-t border-[var(--panel-border)] mt-2">
                <button onClick={() => setIsSettingsOpen(false)} className="w-full py-2 bg-[var(--accent)] hover:bg-blue-600 text-white rounded-md transition-colors font-medium">Save Preferences</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </main>
  );
}
