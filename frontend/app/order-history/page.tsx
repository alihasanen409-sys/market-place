export default function OrderHistoryPage() {
  return (
    <main className="mx-auto max-w-4xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">Order history</h1>
      <div className="rounded-md border border-ink/10 bg-white p-5 dark:border-white/10 dark:bg-white/10">
        <div className="grid grid-cols-3 gap-4 text-sm font-semibold"><span>Order</span><span>Status</span><span>Total</span></div>
        <div className="mt-3 grid grid-cols-3 gap-4 text-sm"><span>SIM-1001</span><span>Delivered</span><span>$29.00</span></div>
      </div>
    </main>
  );
}
