"use client";

import { FormEvent, useState } from "react";

type ChatResponse = {
  message: string;
};

export default function Home() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setLoading(true);
    setError("");
    setReply("");

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message,
        }),
      });

      if (!response.ok) {
        const errorBody = await response.json();
      
        throw new Error(
          typeof errorBody.detail === "string"
            ? errorBody.detail
            : `Request failed with status ${response.status}`
        );
      }

      const data: ChatResponse = await response.json();

      setReply(data.message);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Unknown error");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold">
        AI Knowledge Assistant
      </h1>

      <form
        onSubmit={handleSubmit}
        className="mt-8 flex max-w-2xl gap-2"
      >
        <input
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder="Write a message..."
          className="flex-1 rounded border px-3 py-2"
        />

        <button
          type="submit"
          disabled={loading}
          className="rounded border px-4 py-2"
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </form>

      {reply && (
        <div className="mt-6">
          <strong>Assistant:</strong> {reply}
        </div>
      )}

      {error && (
        <div className="mt-6">
          <strong>Error:</strong> {error}
        </div>
      )}
    </main>
  );
}