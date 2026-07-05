import { ListingCard } from "@/components/listing-card";
import { fallbackListings } from "@/lib/api";

export default function FavoritesPage() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">Favorites</h1>
      <div className="grid gap-5 md:grid-cols-3">{fallbackListings.slice(0, 2).map((item) => <ListingCard key={item.id} listing={item} />)}</div>
    </main>
  );
}
