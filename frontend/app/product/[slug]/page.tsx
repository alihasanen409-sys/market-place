import Image from "next/image";
import Link from "next/link";
import { fallbackListings } from "@/lib/api";

export default function ProductPage({ params }: { params: { slug: string } }) {
  const listing = fallbackListings.find((item) => item.slug === params.slug) || fallbackListings[0];
  const image = listing.images[0]?.image_url;

  return (
    <main className="mx-auto grid max-w-7xl gap-8 px-4 py-8 lg:grid-cols-[1fr_360px]">
      <section className="space-y-5">
        <div className="relative aspect-[16/10] overflow-hidden rounded-md border border-ink/10 bg-mist dark:border-white/10 dark:bg-white/10">
          {image ? <Image src={image} alt={listing.title} fill className="object-cover" /> : null}
        </div>
        <h1 className="text-3xl font-semibold">{listing.title}</h1>
        <p className="text-ink/75 dark:text-mist/75">{listing.description}</p>
      </section>
      <aside className="h-fit rounded-md border border-ink/10 bg-white p-5 shadow-sm dark:border-white/10 dark:bg-white/10">
        <div className="mb-4 flex items-center justify-between">
          <span className="text-sm text-ink/65 dark:text-mist/65">Price</span>
          <strong className="text-2xl">${listing.price}</strong>
        </div>
        <button className="mb-3 w-full rounded-md bg-coral px-4 py-3 font-semibold text-white">Add to cart</button>
        <Link className="block rounded-md border border-ink/10 px-4 py-3 text-center font-semibold dark:border-white/10" href="/chat">Contact seller</Link>
      </aside>
    </main>
  );
}
