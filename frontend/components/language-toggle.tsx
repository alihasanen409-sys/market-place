"use client";

import { Languages } from "lucide-react";
import { useI18n } from "./i18n-provider";

export function LanguageToggle() {
  const { locale, setLocale } = useI18n();
  const next = locale === "en" ? "ar" : "en";

  return (
    <button
      aria-label="Switch language"
      className="inline-flex h-10 items-center gap-2 rounded-md border border-ink/10 bg-white px-3 text-sm font-semibold text-ink shadow-sm transition hover:border-coral dark:border-white/10 dark:bg-white/10 dark:text-mist"
      onClick={() => setLocale(next)}
      type="button"
    >
      <Languages size={16} />
      {next.toUpperCase()}
    </button>
  );
}
