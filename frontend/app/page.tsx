"use client";

import { useState } from "react";

export default function Home() {
  const [backendStatus, setBackendStatus] = useState<string>("unknown");
  const [backendName, setBackendName] = useState<string>("unknown");
  const [backendVersion, setBackendVersion] = useState<string>("unknown");

  async function checkBackend() {
    try {
      const healthResponse = await fetch("http://localhost:8000/health");
      const healthData = await healthResponse.json();

      const response = await fetch("http://localhost:8000");
      const rootData = await response.json();

      setBackendStatus(healthData.status);
      setBackendName(rootData.name);
      setBackendVersion(rootData.version);
    } catch {
      setBackendStatus("error");
      setBackendName("unknown");
      setBackendVersion("unknown");
    }
  }

  return (
    <main className="min-h-screen p-8">

      <div className="mt-4">
        <p>API: {backendName}</p>
        <p>Version: {backendVersion}</p>
        <p>Status: {backendStatus}</p>
      </div>

      <button
        onClick={checkBackend}
        className="mt-4 rounded border px-4 py-2"
      >
        Check backend
      </button>
    </main>
  );
}