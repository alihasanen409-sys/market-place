"use client";

import { useI18n } from "@/components/i18n-provider";
import { useState } from "react";

export default function CheckoutPage() {
  const { t } = useI18n();
  const [done, setDone] = useState(false);
  return (
    <main className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">{t.checkout}</h1>
      <form className="space-y-4 rounded-md border border-ink/10 bg-white p-5 dark:border-white/10 dark:bg-white/10">
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.name} />
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.email} />
        <p className="rounded-md bg-mist p-3 text-sm dark:bg-white/10">{t.simulatedPayment}: no real card is charged.</p>
        <button className="w-full rounded-md bg-coral px-4 py-3 font-semibold text-white" onClick={() => setDone(true)} type="button">{t.checkout}</button>
        {done ? <p className="rounded-md bg-mist p-3 text-sm dark:bg-white/10">Order confirmed. The payment was simulated.</p> : null}
      </form>
    </main>
  );
}
