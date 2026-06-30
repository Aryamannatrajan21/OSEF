"use client";

import React, { useRef, useEffect, useState, useCallback } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import ForceGraph3D from 'react-force-graph-3d';

// Domain color mapping
const DOMAIN_COLORS: Record<string, string> = {
  Software: '#3b82f6',
  Architecture: '#a855f7',
  Infrastructure: '#f97316',
  Security: '#ef4444',
  Runtime: '#22c55e',
  Enterprise: '#06b6d4',
  Documentation: '#eab308',
  default: '#888888'
};

const getDomainColor = (type: string) => {
  // Simple heuristic for now, we'll map EKG types to Domains
  if (['Class', 'Method', 'Function', 'Variable'].includes(type)) return DOMAIN_COLORS.Software;
  if (['Package', 'Module', 'Interface'].includes(type)) return DOMAIN_COLORS.Architecture;
  if (['Deployment', 'Pod', 'Container'].includes(type)) return DOMAIN_COLORS.Infrastructure;
  return DOMAIN_COLORS.default;
};

interface ForceGraphProps {
  data: any;
  onNodeClick?: (node: any) => void;
  searchQuery?: string;
  is3DMode?: boolean;
}

export default function ForceGraph({ data, onNodeClick, searchQuery = '', is3DMode = false }: ForceGraphProps) {
  const fgRef = useRef<any>(null);
  const fg3DRef = useRef<any>(null);
  const [dimensions, setDimensions] = useState({ width: 800, height: 600 });
  const containerRef = useRef<HTMLDivElement>(null);

  // Resize observer to make graph responsive
  useEffect(() => {
    if (!containerRef.current) return;
    
    const observer = new ResizeObserver(entries => {
      if (entries.length > 0) {
        setDimensions({
          width: entries[0].contentRect.width,
          height: entries[0].contentRect.height
        });
      }
    });
    
    observer.observe(containerRef.current);
    return () => observer.disconnect();
  }, []);

  // Format data for react-force-graph
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });

  useEffect(() => {
    if (!data || !data.nodes || !data.edges) return;
    
    // Map EKG nodes to react-force-graph format
    const nodes = Object.values(data.nodes).map((n: any) => ({
      id: n.id,
      name: n.name,
      val: 2,
      color: getDomainColor(n.type),
      ...n
    }));
    
    // Map EKG edges to links
    const links = data.edges.map((e: any) => ({
      source: e.source_id,
      target: e.target_id,
      name: e.relation_type
    }));
    
    setGraphData({ nodes, links } as any);
  }, [data]);

  const handleNodeClick = useCallback((node: any) => {
    if (onNodeClick) onNodeClick(node);
    
    // Center/zoom on node
    if (!is3DMode && fgRef.current) {
      fgRef.current.centerAt(node.x, node.y, 1000);
      fgRef.current.zoom(8, 2000);
    } else if (is3DMode && fg3DRef.current) {
      // 3D camera zoom
      const distance = 40;
      const distRatio = 1 + distance/Math.hypot(node.x, node.y, node.z);
      fg3DRef.current.cameraPosition(
        { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }, // new position
        node, // lookAt ({ x, y, z })
        3000  // ms transition duration
      );
    }
  }, [onNodeClick, is3DMode]);

  return (
    <div ref={containerRef} className="w-full h-full relative">
      {graphData.nodes.length > 0 ? (
        is3DMode ? (
          <ForceGraph3D
            ref={fg3DRef}
            width={dimensions.width}
            height={dimensions.height}
            graphData={graphData}
            nodeLabel="name"
            nodeColor={(node: any) => {
              if (!searchQuery) return node.color;
              const match = node.name.toLowerCase().includes(searchQuery.toLowerCase());
              return match ? node.color : 'rgba(255, 255, 255, 0.05)';
            }}
            nodeRelSize={4}
            linkColor={() => 'rgba(255, 255, 255, 0.2)'}
            linkDirectionalArrowLength={3.5}
            linkDirectionalArrowRelPos={1}
            onNodeClick={handleNodeClick}
            backgroundColor="#00000000" // transparent
          />
        ) : (
          <ForceGraph2D
            ref={fgRef}
            width={dimensions.width}
            height={dimensions.height}
            graphData={graphData}
            nodeLabel="name"
            nodeColor={(node: any) => {
              if (!searchQuery) return node.color;
              const match = node.name.toLowerCase().includes(searchQuery.toLowerCase());
              return match ? node.color : 'rgba(255, 255, 255, 0.05)';
            }}
            nodeRelSize={4}
            linkColor={() => 'rgba(255, 255, 255, 0.2)'}
            linkDirectionalArrowLength={3.5}
            linkDirectionalArrowRelPos={1}
            onNodeClick={handleNodeClick}
            backgroundColor="#00000000" // transparent
          />
        )
      ) : (
        <div className="absolute inset-0 flex items-center justify-center text-gray-500">
          Loading graph data...
        </div>
      )}
    </div>
  );
}

