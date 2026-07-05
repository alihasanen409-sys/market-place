"use client";

import { useI18n } from "@/components/i18n-provider";

export default function ChatPage() {
  const { t } = useI18n();
  return (
    <main className="mx-auto grid max-w-7xl gap-4 px-4 py-8 md:grid-cols-[280px_1fr]">
      <aside className="rounded-md border border-ink/10 bg-white p-4 dark:border-white/10 dark:bg-white/10">
        <h1 className="mb-4 text-xl font-semibold">{t.chat}</h1>
        {["Brand kit order", "Portfolio review", "Music license"].map((item) => <button className="block w-full rounded-md px-3 py-2 text-left hover:bg-mist dark:hover:bg-white/10" key={item}>{item}</button>)}
      </aside>
      <section className="rounded-md border border-ink/10 bg-white p-4 dark:border-white/10 dark:bg-white/10">
        <div className="mb-4 space-y-3">
          <p className="max-w-lg rounded-md bg-mist p-3 dark:bg-white/10">Hi, can you customize this package?</p>
          <p className="ml-auto max-w-lg rounded-md bg-coral p-3 text-white">Yes, I can deliver a custom version this week.</p>
        </div>
        <div className="flex gap-2">
          <input className="min-w-0 flex-1 rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.chat} />
          <button className="rounded-md bg-ink px-4 py-2 font-semibold text-white dark:bg-mist dark:text-ink">{t.send}</button>
        </div>
      </section>
    </main>
  );
}
