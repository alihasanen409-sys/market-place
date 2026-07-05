"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Search } from "lucide-react";
import { ListingCard } from "@/components/listing-card";
import { fallbackListings } from "@/lib/api";
import { useI18n } from "@/components/i18n-provider";

export default function HomePage() {
  const { t } = useI18n();

  return (
    <main>
      <section className="border-b border-ink/10 px-4 py-12 dark:border-white/10">
        <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[1fr_420px] lg:items-center">
          <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} className="space-y-6">
            <h1 className="max-w-3xl text-4xl font-semibold leading-tight md:text-6xl">{t.heroTitle}</h1>
            <p className="max-w-2xl text-lg text-ink/70 dark:text-mist/75">{t.heroBody}</p>
            <form className="flex max-w-xl gap-2 rounded-md border border-ink/10 bg-white p-2 dark:border-white/10 dark:bg-white/10" action="/marketplace">
              <Search className="mx-2 mt-2 text-ink/50 dark:text-mist/60" size={20} />
              <input name="q" aria-label={t.search} className="min-w-0 flex-1 bg-transparent px-2 outline-none" placeholder={t.search} />
              <button className="rounded-md bg-coral px-4 py-2 font-semibold text-white" type="submit">{t.browse}</button>
            </form>
            <div className="flex flex-wrap gap-3">
              <Link className="rounded-md bg-ink px-4 py-2 font-semibold text-white dark:bg-mist dark:text-ink" href="/marketplace">{t.browse}</Link>
              <Link className="rounded-md border border-ink/15 px-4 py-2 font-semibold dark:border-white/15" href="/seller-dashboard">{t.becomeSeller}</Link>
            </div>
          </motion.div>
          <div className="rounded-md border border-ink/10 bg-white p-4 shadow-soft dark:border-white/10 dark:bg-white/10">
            <ListingCard listing={fallbackListings[0]} />
          </div>
        </div>
      </section>
      <section className="mx-auto max-w-7xl px-4 py-10">
        <h2 className="mb-5 text-2xl font-semibold">{t.featured}</h2>
        <div className="grid gap-5 md:grid-cols-3">
          {fallbackListings.map((listing) => <ListingCard key={listing.id} listing={listing} />)}
        </div>
      </section>
    </main>
  );
}
