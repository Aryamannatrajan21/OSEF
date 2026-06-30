"use client";

import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Cpu } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

interface ApiConfig {
  base_url: string;
  api_key: string;
  model: string;
}

export function AssistantTab({ apiConfig }: { apiConfig?: ApiConfig }) {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: 'Hello! I am the OSEF Architecture Assistant. Ask me anything about your codebase structure, dependencies, or policy violations.' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMsg = input.trim();
    setInput('');
    const newMessages: Message[] = [...messages, { role: 'user', content: userMsg }];
    setMessages(newMessages);
    setIsLoading(true);

    try {
      const payload = {
        message: userMsg,
        history: messages,
        api_config: apiConfig || undefined
      };
      
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      
      const data = await res.json();
      
      if (data.error) {
        setMessages([...newMessages, { role: 'assistant', content: `**Error:** ${data.error}` }]);
      } else {
        setMessages([...newMessages, { role: 'assistant', content: data.reply }]);
      }
    } catch (err) {
      setMessages([...newMessages, { role: 'assistant', content: 'Sorry, I encountered a network error while connecting to the assistant API.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col p-8 overflow-hidden h-full">
      <h2 className="text-2xl font-bold text-white mb-6 flex items-center shrink-0">
        <Cpu className="mr-3 text-purple-400" /> Engineering Assistant
      </h2>
      
      <div className="flex-1 glass-panel border border-[var(--panel-border)] rounded-xl flex flex-col overflow-hidden relative shadow-2xl bg-black/20">
        {/* Chat History */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`flex max-w-[80%] ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                <div className={`flex-shrink-0 h-10 w-10 rounded-full flex items-center justify-center ${msg.role === 'user' ? 'bg-[var(--accent)] ml-4' : 'bg-gray-800 border border-gray-700 mr-4'}`}>
                  {msg.role === 'user' ? <User size={20} className="text-white" /> : <Bot size={20} className="text-purple-400" />}
                </div>
                <div className={`px-5 py-3 rounded-2xl ${msg.role === 'user' ? 'bg-[var(--accent)] text-white rounded-tr-sm' : 'bg-gray-800/80 border border-gray-700 text-gray-200 rounded-tl-sm'}`}>
                  {msg.role === 'user' ? (
                    <p className="whitespace-pre-wrap text-sm leading-relaxed">{msg.content}</p>
                  ) : (
                    <div className="prose prose-sm prose-invert max-w-none text-gray-200">
                      <ReactMarkdown remarkPlugins={[remarkGfm]}>
                        {msg.content}
                      </ReactMarkdown>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div className="flex justify-start">
              <div className="flex max-w-[80%] flex-row">
                <div className="flex-shrink-0 h-10 w-10 rounded-full flex items-center justify-center bg-gray-800 border border-gray-700 mr-4">
                  <Bot size={20} className="text-purple-400 animate-pulse" />
                </div>
                <div className="px-5 py-4 rounded-2xl bg-gray-800/80 border border-gray-700 text-gray-200 rounded-tl-sm flex items-center space-x-2">
                  <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                  <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                  <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
        
        {/* Input Box */}
        <div className="p-4 bg-black/40 border-t border-[var(--panel-border)] shrink-0">
          <form onSubmit={handleSubmit} className="flex space-x-4 relative max-w-4xl mx-auto">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about your architecture..."
              className="flex-1 bg-gray-900/80 border border-gray-700 rounded-full px-6 py-3 text-gray-200 focus:outline-none focus:border-[var(--accent)] transition-colors placeholder-gray-500 shadow-inner"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={!input.trim() || isLoading}
              className={`absolute right-2 top-1/2 -translate-y-1/2 p-2 rounded-full transition-colors ${!input.trim() || isLoading ? 'text-gray-600' : 'text-white bg-[var(--accent)] hover:bg-blue-600'}`}
            >
              <Send size={18} />
            </button>
          </form>
          <div className="text-center mt-3">
            <span className="text-xs text-gray-600">The assistant has full access to the live OSEF Engine graph and policy engine.</span>
          </div>
        </div>
      </div>
    </div>
  );
}
