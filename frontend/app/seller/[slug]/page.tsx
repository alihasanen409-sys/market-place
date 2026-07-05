import { ListingCard } from "@/components/listing-card";
import { fallbackListings } from "@/lib/api";

export default function SellerProfilePage({ params }: { params: { slug: string } }) {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <section className="mb-8 rounded-md border border-ink/10 bg-white p-6 dark:border-white/10 dark:bg-white/10">
        <h1 className="text-3xl font-semibold">{params.slug.replaceAll("-", " ")}</h1>
        <p className="mt-2 text-ink/70 dark:text-mist/70">Independent creator selling polished digital products and services.</p>
      </section>
      <div className="grid gap-5 md:grid-cols-3">{fallbackListings.map((item) => <ListingCard key={item.id} listing={item} />)}</div>
    </main>
  );
}
