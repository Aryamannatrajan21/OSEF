"use client";

import React from 'react';
import { X, Info, Box, Code2, Link as LinkIcon, Network, ShieldAlert } from 'lucide-react';

interface NodeSidebarProps {
  node: any | null;
  onClose: () => void;
}

export default function NodeSidebar({ node, onClose }: NodeSidebarProps) {
  if (!node) return null;

  return (
    <div className="absolute top-0 right-0 h-full w-96 glass-panel border-l z-50 flex flex-col text-sm shadow-2xl transition-transform duration-300">
      
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b border-[var(--panel-border)]">
        <div>
          <span className="text-[var(--accent)] font-mono text-xs uppercase tracking-wider">{node.type}</span>
          <h2 className="text-lg font-semibold truncate text-white mt-1">{node.name}</h2>
        </div>
        <button 
          onClick={onClose}
          className="p-1 hover:bg-[var(--hover-bg)] rounded-md text-gray-400 hover:text-white transition-colors"
        >
          <X size={20} />
        </button>
      </div>

      {/* Scrollable Content */}
      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        
        {/* Semantic Facts */}
        <section>
          <h3 className="flex items-center text-xs font-semibold uppercase text-gray-400 mb-3 tracking-wide">
            <Info size={14} className="mr-2" /> Semantic Facts
          </h3>
          <div className="bg-black/30 rounded-lg p-3 border border-[var(--panel-border)] space-y-2 font-mono text-xs text-gray-300">
            <div className="flex justify-between">
              <span className="text-gray-500">ID</span>
              <span className="truncate ml-4" title={node.id}>{node.id}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-gray-500">Created</span>
              <span>{new Date(node.created_at).toLocaleString()}</span>
            </div>
            {Object.entries(node.metadata || {}).map(([k, v]) => (
              <div key={k} className="flex justify-between">
                <span className="text-gray-500">{k}</span>
                <span className="truncate ml-4">{String(v)}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Dependencies Placeholder */}
        <section>
          <h3 className="flex items-center text-xs font-semibold uppercase text-gray-400 mb-3 tracking-wide">
            <Network size={14} className="mr-2" /> Dependencies
          </h3>
          <div className="text-xs text-gray-500 italic px-2">
            Select node in graph to see incoming/outgoing edges.
          </div>
        </section>

        {/* Reasoner Context */}
        <section>
          <h3 className="flex items-center text-xs font-semibold uppercase text-[var(--accent)] mb-3 tracking-wide">
            <Box size={14} className="mr-2" /> Engineering Reasoner
          </h3>
          <div className="space-y-2">
            <button className="w-full text-left px-3 py-2 bg-black/20 hover:bg-[var(--hover-bg)] border border-[var(--panel-border)] rounded-md transition-colors text-gray-300 text-xs">
              What breaks if I delete this?
            </button>
            <button className="w-full text-left px-3 py-2 bg-black/20 hover:bg-[var(--hover-bg)] border border-[var(--panel-border)] rounded-md transition-colors text-gray-300 text-xs">
              Show blast radius
            </button>
            <button className="w-full text-left px-3 py-2 bg-black/20 hover:bg-[var(--hover-bg)] border border-[var(--panel-border)] rounded-md transition-colors text-gray-300 text-xs">
              Why is this violating policy?
            </button>
          </div>
        </section>

      </div>
    </div>
  );
}
