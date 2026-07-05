"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAccount } from "@/components/account-provider";

export default function CreateListingPage() {
  const { role, signedIn } = useAccount();
  const router = useRouter();
  const [created, setCreated] = useState(false);

  if (!signedIn) {
    return (
      <main className="mx-auto max-w-xl px-4 py-10">
        <h1 className="mb-4 text-3xl font-semibold">Create listing</h1>
        <p className="mb-4 text-ink/70 dark:text-mist/70">Sign in as a seller to add a product.</p>
        <button className="rounded-md bg-coral px-4 py-2 font-semibold text-white" onClick={() => router.push("/login")} type="button">Login</button>
      </main>
    );
  }

  if (role !== "seller" && role !== "admin") {
    return (
      <main className="mx-auto max-w-xl px-4 py-10">
        <h1 className="mb-4 text-3xl font-semibold">Create listing</h1>
        <p className="rounded-md bg-mist p-4 dark:bg-white/10">Only seller or administrator accounts can add products.</p>
      </main>
    );
  }

  return (
    <main className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">Create listing</h1>
      <form className="space-y-4 rounded-md border border-ink/10 bg-white p-5 dark:border-white/10 dark:bg-white/10">
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder="Product title" />
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder="Price" />
        <textarea className="min-h-32 w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder="Description" />
        <button className="rounded-md bg-coral px-4 py-3 font-semibold text-white" onClick={() => setCreated(true)} type="button">Publish product</button>
        {created ? <p className="rounded-md bg-mist p-3 text-sm dark:bg-white/10">Product saved as a seller listing.</p> : null}
      </form>
    </main>
  );
}
