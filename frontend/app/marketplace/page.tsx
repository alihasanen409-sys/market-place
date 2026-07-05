"use client";

import { Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import { ListingCard } from "@/components/listing-card";
import { fallbackListings, getListings } from "@/lib/api";
import { useI18n } from "@/components/i18n-provider";

function MarketplaceContent() {
  const { t } = useI18n();
  const params = useSearchParams();
  const search = params.get("q") || "";
  const { data, isError } = useQuery({ queryKey: ["listings", search], queryFn: () => getListings(search), retry: 1 });
  const listings = isError || !data ? fallbackListings : data.results;

  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <h1 className="text-3xl font-semibold">{t.marketplace}</h1>
          <p className="mt-2 text-ink/70 dark:text-mist/70">{t.heroBody}</p>
        </div>
        <form className="flex min-w-0 rounded-md border border-ink/10 bg-white p-2 dark:border-white/10 dark:bg-white/10">
          <input name="q" defaultValue={search} className="min-w-0 flex-1 bg-transparent px-3 outline-none" placeholder={t.search} />
          <button className="rounded-md bg-coral px-4 py-2 font-semibold text-white">{t.search}</button>
        </form>
      </div>
      <div className="mb-6 flex flex-wrap gap-2 text-sm">
        {["Design", "Code", "Music", "Writing", "Video", "Photography"].map((item) => (
          <span className="rounded-md border border-ink/10 px-3 py-2 dark:border-white/10" key={item}>{item}</span>
        ))}
      </div>
      <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
        {listings.map((listing) => <ListingCard key={listing.id} listing={listing} />)}
      </div>
    </main>
  );
}

export default function MarketplacePage() {
  return (
    <Suspense fallback={<main className="mx-auto max-w-7xl px-4 py-8">Loading marketplace...</main>}>
      <MarketplaceContent />
    </Suspense>
  );
}
