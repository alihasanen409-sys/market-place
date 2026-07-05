export default function NotificationsPage() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">Notifications</h1>
      <div className="space-y-3">{["Order confirmed", "Seller replied", "New review received"].map((item) => <p className="rounded-md border border-ink/10 bg-white p-4 dark:border-white/10 dark:bg-white/10" key={item}>{item}</p>)}</div>
    </main>
  );
}
