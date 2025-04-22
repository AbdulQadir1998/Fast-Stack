"use client";

import { useSession } from "next-auth/react";

export default function TestPage() {
  const { data: session } = useSession();
  
  return (
    <div>
      <h1>Test Auth</h1>
      <pre>{JSON.stringify(session, null, 2)}</pre>
    </div>
  );
}
