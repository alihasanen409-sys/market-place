import { ApiPage, Category, Listing } from "./types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers || {})
    },
    cache: "no-store"
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export async function getListings(search = "") {
  const query = search ? `?search=${encodeURIComponent(search)}` : "";
  return apiFetch<ApiPage<Listing>>(`/listings/${query}`);
}

export async function getCategories() {
  return apiFetch<ApiPage<Category>>("/categories/");
}

export const fallbackListings: Listing[] = [
  {
    id: "sample-brand-kit",
    title: "Launch-ready brand identity kit",
    slug: "launch-ready-brand-identity-kit",
    short_description: "Logos, color system, social templates, and brand guide for new creator businesses.",
    description: "A polished digital brand kit with editable source files and a concise style guide.",
    price: "29.00",
    status: "published",
    product_type: "digital",
    rating_avg: "4.90",
    sales_count: 128,
    images: [
      {
        image_url: "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1200&q=80",
        alt_text: "Creative desk with brand materials",
        is_primary: true
      }
    ]
  },
  {
    id: "sample-portfolio-review",
    title: "Portfolio critique for designers",
    slug: "portfolio-critique-for-designers",
    short_description: "Actionable video review for landing better creative work.",
    description: "A service listing for designers who want concrete portfolio feedback.",
    price: "45.00",
    status: "published",
    product_type: "service",
    rating_avg: "4.80",
    sales_count: 74,
    images: [
      {
        image_url: "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=80",
        alt_text: "Team reviewing a creative portfolio",
        is_primary: true
      }
    ]
  },
  {
    id: "sample-music-pack",
    title: "Indie video intro music pack",
    slug: "indie-video-intro-music-pack",
    short_description: "Royalty-free loops for reels, courses, trailers, and product videos.",
    description: "A bundle of short intro tracks exported in multiple formats.",
    price: "18.00",
    status: "published",
    product_type: "digital",
    rating_avg: "4.70",
    sales_count: 211,
    images: [
      {
        image_url: "https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=1200&q=80",
        alt_text: "Music production workspace",
        is_primary: true
      }
    ]
  }
];
