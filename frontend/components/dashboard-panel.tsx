import { ReactNode } from "react";

export function DashboardPanel({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section className="rounded-md border border-ink/10 bg-white p-5 shadow-sm dark:border-white/10 dark:bg-white/10">
      <h2 className="mb-4 text-lg font-semibold">{title}</h2>
      {children}
    </section>
  );
}
