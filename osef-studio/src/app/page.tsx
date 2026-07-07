"use client";

import React, { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import NodeSidebar from '@/components/sidebar/NodeSidebar';
import { Search, Activity, Layers, ShieldCheck, Box, Settings, X } from 'lucide-react';
import { ArchitectureTab, ReasoningTab, PoliciesTab, BenchmarksTab, AssistantTab, DependenciesTab, PluginsTab, MarketplaceTab } from '@/components/tabs/StudioTabs';

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

  // Settings State
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [is3DMode, setIs3DMode] = useState(false);
  const [autoRefresh, setAutoRefresh] = useState(true);

  // API Configuration State
  const [apiBaseUrl, setApiBaseUrl] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [apiModel, setApiModel] = useState('');

  // Load settings on mount
  useEffect(() => {
    const savedApiBaseUrl = localStorage.getItem('apiBaseUrl');
    const savedApiKey = localStorage.getItem('apiKey');
    const savedApiModel = localStorage.getItem('apiModel');
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (savedApiBaseUrl) setApiBaseUrl(savedApiBaseUrl);
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (savedApiKey) setApiKey(savedApiKey);
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (savedApiModel) setApiModel(savedApiModel);
  }, []);

  // Save settings
  const savePreferences = () => {
    localStorage.setItem('apiBaseUrl', apiBaseUrl);
    localStorage.setItem('apiKey', apiKey);
    localStorage.setItem('apiModel', apiModel);
    setIsSettingsOpen(false);
  };

  // Auto-refresh interval
  useEffect(() => {
    if (!autoRefresh) return;
    
    const fetchGraph = () => {
      fetch('http://localhost:8000/api/graph')
        .then(res => res.json())
        .then(data => {
          if (!data.error) setGraphData(data);
        })
        .catch(() => {});
    };

    const interval = setInterval(fetchGraph, 5000);
    return () => clearInterval(interval);
  }, [autoRefresh]);

  useEffect(() => {
    // Fetch EKG initially
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

  const TABS = ['Graph', 'Architecture', 'Reasoning', 'Policies', 'Dependencies', 'Plugins', 'Marketplace', 'Benchmarks', 'Assistant'];

  return (
    <main className={`w-screen h-screen relative overflow-hidden transition-colors duration-500 ${isDarkMode ? 'bg-[var(--background)]' : 'bg-gray-100 text-gray-900'}`}>
      
      {/* Top Navigation Bar */}
      <nav className={`absolute top-0 left-0 w-full h-14 border-b z-40 flex items-center justify-between px-6 ${isDarkMode ? 'glass-panel' : 'bg-white border-gray-300'}`}>
        <div className="flex items-center space-x-6">
          <div className={`flex items-center space-x-2 font-semibold tracking-wide ${isDarkMode ? 'text-white' : 'text-black'}`}>
            <Box size={20} className="text-[var(--accent)]" />
            <span>OSEF Studio</span>
          </div>
          <div className={`h-4 w-[1px] ${isDarkMode ? 'bg-white/20' : 'bg-gray-300'}`}></div>
          <div className={`flex items-center space-x-4 text-sm ${isDarkMode ? 'text-gray-400' : 'text-gray-500'}`}>
            {TABS.map(tab => (
              <button 
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`transition-colors ${activeTab === tab ? (isDarkMode ? 'text-white font-medium' : 'text-black font-medium') : (isDarkMode ? 'hover:text-white' : 'hover:text-black')}`}
              >
                {tab}
              </button>
            ))}
          </div>
        </div>

        {/* Global Search */}
        <div className="flex-1 max-w-md mx-8 relative">
          <Search size={16} className={`absolute left-3 top-1/2 -translate-y-1/2 ${isDarkMode ? 'text-gray-500' : 'text-gray-400'}`} />
          <input 
            type="text" 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search classes, policies, findings..." 
            className={`w-full rounded-md py-1.5 pl-9 pr-4 text-sm transition-colors focus:outline-none focus:border-[var(--accent)] ${isDarkMode ? 'bg-black/40 border border-[var(--panel-border)] text-gray-200 placeholder-gray-500' : 'bg-gray-100 border border-gray-300 text-gray-800 placeholder-gray-400'}`}
          />
        </div>

        <div className={`flex items-center space-x-4 ${isDarkMode ? 'text-gray-400' : 'text-gray-500'}`}>
          <button onClick={() => setIsHealthOpen(true)} className={`transition-colors ${isDarkMode ? 'hover:text-white' : 'hover:text-black'}`} title="System Health"><Activity size={18} /></button>
          <button onClick={() => setIsSettingsOpen(true)} className={`transition-colors ${isDarkMode ? 'hover:text-white' : 'hover:text-black'}`} title="Settings"><Settings size={18} /></button>
        </div>
      </nav>

      {/* Main Content Area */}
      <div className="absolute inset-0 pt-14 flex flex-col">
        {error ? (
          <div className="flex h-full items-center justify-center">
            <div className={`p-6 rounded-lg max-w-md text-center border ${isDarkMode ? 'glass-panel border-red-900/50' : 'bg-red-50 border-red-200'}`}>
              <ShieldCheck size={48} className="mx-auto text-red-500 mb-4" />
              <h3 className={`font-semibold mb-2 ${isDarkMode ? 'text-white' : 'text-red-900'}`}>Connection Refused</h3>
              <p className={`text-sm mb-4 ${isDarkMode ? 'text-gray-400' : 'text-red-700'}`}>{error}</p>
              <code className={`px-3 py-2 rounded text-[var(--accent)] text-xs font-mono ${isDarkMode ? 'bg-black/50' : 'bg-red-100'}`}>
                osef ui
              </code>
              <p className={`text-xs mt-4 ${isDarkMode ? 'text-gray-500' : 'text-red-600'}`}>Run the command above in your terminal to start the API.</p>
            </div>
          </div>
        ) : activeTab === 'Graph' ? (
          <ForceGraph data={graphData} onNodeClick={setSelectedNode} searchQuery={searchQuery} is3DMode={is3DMode} />
        ) : activeTab === 'Architecture' ? (
          <ArchitectureTab />
        ) : activeTab === 'Reasoning' ? (
          <ReasoningTab />
        ) : activeTab === 'Policies' ? (
          <PoliciesTab />
        ) : activeTab === 'Dependencies' ? (
          <DependenciesTab />
        ) : activeTab === 'Plugins' ? (
          <PluginsTab />
        ) : activeTab === 'Marketplace' ? (
          <MarketplaceTab />
        ) : activeTab === 'Benchmarks' ? (
          <BenchmarksTab />
        ) : activeTab === 'Assistant' ? (
          <AssistantTab apiConfig={{ base_url: apiBaseUrl, api_key: apiKey, model: apiModel }} />
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
          <div className={`w-96 rounded-xl overflow-hidden flex flex-col shadow-2xl ${isDarkMode ? 'glass-panel border border-[var(--panel-border)]' : 'bg-white border border-gray-200'}`}>
            <div className={`p-4 border-b flex justify-between items-center ${isDarkMode ? 'border-[var(--panel-border)] bg-black/40' : 'border-gray-200 bg-gray-50'}`}>
              <h3 className={`font-semibold flex items-center ${isDarkMode ? 'text-white' : 'text-gray-900'}`}><Activity size={16} className="mr-2 text-[var(--accent)]" /> System Health</h3>
              <button onClick={() => setIsHealthOpen(false)} className={`${isDarkMode ? 'text-gray-400 hover:text-white' : 'text-gray-500 hover:text-gray-900'}`}><X size={16} /></button>
            </div>
            <div className={`p-6 space-y-4 text-sm ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>
              <div className="flex justify-between items-center">
                <span>API Status</span>
                <span className="text-green-500 flex items-center"><div className="w-2 h-2 rounded-full bg-green-500 mr-2 animate-pulse"></div> Online</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Graph Engine</span>
                <span className="text-green-500">Stable</span>
              </div>
              <div className="flex justify-between items-center">
                <span>Last Sync</span>
                <span className={isDarkMode ? 'text-white' : 'text-gray-900'}>Just now</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Settings Modal */}
      {isSettingsOpen && (
        <div className="absolute inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
          <div className={`w-96 rounded-xl overflow-hidden flex flex-col shadow-2xl ${isDarkMode ? 'glass-panel border border-[var(--panel-border)]' : 'bg-white border border-gray-200'}`}>
            <div className={`p-4 border-b flex justify-between items-center ${isDarkMode ? 'border-[var(--panel-border)] bg-black/40' : 'border-gray-200 bg-gray-50'}`}>
              <h3 className={`font-semibold flex items-center ${isDarkMode ? 'text-white' : 'text-gray-900'}`}><Settings size={16} className="mr-2 text-gray-400" /> Settings</h3>
              <button onClick={() => setIsSettingsOpen(false)} className={`${isDarkMode ? 'text-gray-400 hover:text-white' : 'text-gray-500 hover:text-gray-900'}`}><X size={16} /></button>
            </div>
            <div className="p-6 space-y-4 text-sm">
              <div className="space-y-3">
                <label className={`flex justify-between items-center cursor-pointer ${isDarkMode ? 'text-gray-400' : 'text-gray-700'}`}>
                  <span>Dark Mode</span>
                  <input type="checkbox" checked={isDarkMode} onChange={(e) => setIsDarkMode(e.target.checked)} className={`rounded w-4 h-4 ${isDarkMode ? 'border-gray-600 bg-gray-700' : 'border-gray-300 bg-white'}`} />
                </label>
                <label className={`flex justify-between items-center cursor-pointer ${isDarkMode ? 'text-gray-400' : 'text-gray-700'}`}>
                  <span>Cinematic 3D Mode</span>
                  <input type="checkbox" checked={is3DMode} onChange={(e) => setIs3DMode(e.target.checked)} className={`rounded w-4 h-4 ${isDarkMode ? 'border-gray-600 bg-gray-700' : 'border-gray-300 bg-white'}`} />
                </label>
                <label className={`flex justify-between items-center cursor-pointer ${isDarkMode ? 'text-gray-400' : 'text-gray-700'}`}>
                  <span>Auto-Refresh Graph</span>
                  <input type="checkbox" checked={autoRefresh} onChange={(e) => setAutoRefresh(e.target.checked)} className={`rounded w-4 h-4 ${isDarkMode ? 'border-gray-600 bg-gray-700' : 'border-gray-300 bg-white'}`} />
                </label>
              </div>
              <div className={`pt-4 border-t mt-4 ${isDarkMode ? 'border-[var(--panel-border)]' : 'border-gray-200'} space-y-3`}>
                <h4 className={`font-semibold ${isDarkMode ? 'text-white' : 'text-gray-800'}`}>AI Assistant API (OpenAI Compatible)</h4>
                <div className="space-y-2">
                  <label className={`block text-xs ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>Base URL</label>
                  <input type="text" value={apiBaseUrl} onChange={(e) => setApiBaseUrl(e.target.value)} placeholder="https://integrate.api.nvidia.com/v1" className={`w-full px-3 py-2 rounded-md text-sm border focus:outline-none focus:ring-1 focus:ring-[var(--accent)] ${isDarkMode ? 'bg-black/50 border-[var(--panel-border)] text-white' : 'bg-white border-gray-300 text-gray-900'}`} />
                </div>
                <div className="space-y-2">
                  <label className={`block text-xs ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>API Key</label>
                  <input type="password" value={apiKey} onChange={(e) => setApiKey(e.target.value)} placeholder="nvapi-..." className={`w-full px-3 py-2 rounded-md text-sm border focus:outline-none focus:ring-1 focus:ring-[var(--accent)] ${isDarkMode ? 'bg-black/50 border-[var(--panel-border)] text-white' : 'bg-white border-gray-300 text-gray-900'}`} />
                </div>
                <div className="space-y-2">
                  <label className={`block text-xs ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>Model Name</label>
                  <input type="text" value={apiModel} onChange={(e) => setApiModel(e.target.value)} placeholder="nvidia/nemotron-3-ultra-550b-a55b" className={`w-full px-3 py-2 rounded-md text-sm border focus:outline-none focus:ring-1 focus:ring-[var(--accent)] ${isDarkMode ? 'bg-black/50 border-[var(--panel-border)] text-white' : 'bg-white border-gray-300 text-gray-900'}`} />
                </div>
              </div>
              <div className={`pt-4 border-t mt-4 ${isDarkMode ? 'border-[var(--panel-border)]' : 'border-gray-200'}`}>
                <button onClick={savePreferences} className="w-full py-2 bg-[var(--accent)] hover:bg-blue-600 text-white rounded-md transition-colors font-medium">Save Preferences</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </main>
  );
}
