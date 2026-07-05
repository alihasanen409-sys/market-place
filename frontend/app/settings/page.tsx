"use client";

import { useI18n } from "@/components/i18n-provider";

export default function SettingsPage() {
  const { t } = useI18n();
  return (
    <main className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">{t.settings}</h1>
      <form className="space-y-4 rounded-md border border-ink/10 bg-white p-5 dark:border-white/10 dark:bg-white/10">
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.name} />
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.email} />
        <button className="rounded-md bg-coral px-4 py-2 font-semibold text-white" type="button">{t.save}</button>
      </form>
    </main>
  );
}
