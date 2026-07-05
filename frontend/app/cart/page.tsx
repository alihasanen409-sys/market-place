"use client";

import Link from "next/link";
import { fallbackListings } from "@/lib/api";
import { useI18n } from "@/components/i18n-provider";

export default function CartPage() {
  const { t } = useI18n();
  const item = fallbackListings[0];
  return (
    <main className="mx-auto max-w-4xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">{t.cart}</h1>
      <div className="rounded-md border border-ink/10 bg-white p-5 dark:border-white/10 dark:bg-white/10">
        <div className="flex items-center justify-between gap-4 border-b border-ink/10 pb-4 dark:border-white/10">
          <div>
            <h2 className="font-semibold">{item.title}</h2>
            <p className="text-sm text-ink/65 dark:text-mist/65">{item.short_description}</p>
          </div>
          <strong>${item.price}</strong>
        </div>
        <div className="mt-4 flex items-center justify-between">
          <span>{t.total}</span>
          <strong>${item.price}</strong>
        </div>
        <Link className="mt-5 block rounded-md bg-coral px-4 py-3 text-center font-semibold text-white" href="/checkout">{t.checkout}</Link>
      </div>
    </main>
  );
}
