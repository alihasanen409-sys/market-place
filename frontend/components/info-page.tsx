export function InfoPage({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <main className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-5 text-3xl font-semibold">{title}</h1>
      <div className="space-y-4 rounded-md border border-ink/10 bg-white p-5 leading-7 text-ink/75 dark:border-white/10 dark:bg-white/10 dark:text-mist/75">
        {children}
      </div>
    </main>
  );
}
