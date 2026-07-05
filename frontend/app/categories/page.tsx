"use client";

import Link from "next/link";
import { useI18n } from "@/components/i18n-provider";

const categories = ["Design", "Development", "Illustration", "Writing", "Music", "Video", "Photography", "Business"];

export default function CategoriesPage() {
  const { t } = useI18n();
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">{t.categories}</h1>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {categories.map((category) => (
          <Link className="rounded-md border border-ink/10 bg-white p-5 font-semibold shadow-sm hover:border-coral dark:border-white/10 dark:bg-white/10" href={`/marketplace?q=${category}`} key={category}>
            {category}
          </Link>
        ))}
      </div>
    </main>
  );
}
