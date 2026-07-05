import Image from "next/image";
import Link from "next/link";
import { Heart, Star } from "lucide-react";
import { Listing } from "@/lib/types";

export function ListingCard({ listing }: { listing: Listing }) {
  const image = listing.images[0]?.image_url;

  return (
    <article className="overflow-hidden rounded-md border border-ink/10 bg-white shadow-sm transition hover:-translate-y-0.5 hover:shadow-soft dark:border-white/10 dark:bg-white/10">
      <Link href={`/product/${listing.slug}`}>
        <div className="relative aspect-[4/3] bg-mist dark:bg-ink">
          {image ? (
            <Image src={image} alt={listing.images[0]?.alt_text || listing.title} fill className="object-cover" sizes="(min-width: 1024px) 33vw, 100vw" />
          ) : null}
        </div>
      </Link>
      <div className="space-y-3 p-4">
        <div className="flex items-start justify-between gap-3">
          <Link href={`/product/${listing.slug}`} className="font-semibold leading-snug hover:text-coral">
            {listing.title}
          </Link>
          <button aria-label="Favorite listing" className="rounded-md p-1 text-ink/60 hover:text-coral dark:text-mist/70">
            <Heart size={18} />
          </button>
        </div>
        <p className="line-clamp-2 text-sm text-ink/70 dark:text-mist/70">{listing.short_description}</p>
        <div className="flex items-center justify-between text-sm">
          <span className="flex items-center gap-1 text-ink/75 dark:text-mist/75">
            <Star size={16} className="fill-gold text-gold" /> {listing.rating_avg}
          </span>
          <strong>${listing.price}</strong>
        </div>
      </div>
    </article>
  );
}
