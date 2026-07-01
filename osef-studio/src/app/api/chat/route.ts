import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { message, history = [], api_config = {} } = body;

    let baseUrl = api_config.base_url || 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions';
    const apiKey = api_config.api_key || process.env.GEMINI_API_KEY || process.env.OPENAI_API_KEY;
    const model = api_config.model || 'gemini-2.5-flash';

    if (!apiKey) {
      return NextResponse.json({ 
        error: "No API Key provided. Please set it in the Studio settings (bottom left corner)." 
      }, { status: 400 });
    }

    // Ensure base URL points to chat/completions if using default OpenAI-compatible format
    if (!baseUrl.endsWith('/chat/completions')) {
        // Simple heuristic to append it if missing
        if (!baseUrl.endsWith('/')) {
            baseUrl += '/';
        }
        baseUrl += 'chat/completions';
    }

    // Convert history into the standard OpenAI messages format
    const messages = history.map((msg: any) => ({
      role: msg.role === 'assistant' ? 'assistant' : 'user',
      content: msg.content
    }));

    // Append the current message
    messages.push({ role: 'user', content: message });

    // Enforce system instruction by prepending it if not present
    if (messages.length > 0 && messages[0].role !== 'system') {
        messages.unshift({
            role: 'system',
            content: 'You are an expert AI Engineering Assistant for OSEF. Answer questions about the architecture, dependencies, and code structure helpfully.'
        });
    }

    const res = await fetch(baseUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
        'x-goog-api-key': apiKey // Fallback for some Gemini specific endpoints
      },
      body: JSON.stringify({
        model: model,
        messages: messages,
        temperature: 0.7,
      }),
    });

    if (!res.ok) {
      const errorText = await res.text();
      console.error('API Error:', errorText);
      return NextResponse.json({ error: `API request failed: ${res.status} ${res.statusText}` }, { status: res.status });
    }

    const data = await res.json();
    
    // Extract the reply depending on standard OpenAI format
    const reply = data.choices?.[0]?.message?.content || data.candidates?.[0]?.content?.parts?.[0]?.text || "Sorry, I couldn't understand the API response.";

    return NextResponse.json({ reply });
  } catch (err: any) {
    console.error('Chat API Error:', err);
    return NextResponse.json({ error: err.message || "Internal server error" }, { status: 500 });
  }
}
