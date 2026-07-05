"use client";

import Link from "next/link";
import { ReactNode } from "react";
import { ShoppingBag, Store, UserRound } from "lucide-react";
import { ThemeToggle } from "./theme-toggle";
import { LanguageToggle } from "./language-toggle";
import { useI18n } from "./i18n-provider";

export function SiteShell({ children }: { children: ReactNode }) {
  const { t } = useI18n();
  const nav = [
    [t.marketplace, "/marketplace"],
    [t.categories, "/categories"],
    [t.dashboard, "/buyer-dashboard"],
    [t.chat, "/chat"],
    [t.faq, "/faq"]
  ];

  return (
    <div className="min-h-screen bg-[#f8fbf8] text-ink dark:bg-[#101512] dark:text-mist">
      <header className="sticky top-0 z-40 border-b border-ink/10 bg-[#f8fbf8]/90 backdrop-blur dark:border-white/10 dark:bg-[#101512]/90">
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3">
          <Link className="flex items-center gap-2 font-semibold" href="/">
            <span className="flex h-9 w-9 items-center justify-center rounded-md bg-coral text-white">
              <Store size={18} />
            </span>
            {t.brand}
          </Link>
          <nav className="hidden items-center gap-5 text-sm font-medium md:flex">
            {nav.map(([label, href]) => (
              <Link className="text-ink/75 transition hover:text-coral dark:text-mist/75" href={href} key={href}>
                {label}
              </Link>
            ))}
          </nav>
          <div className="flex items-center gap-2">
            <Link className="inline-flex h-10 w-10 items-center justify-center rounded-md border border-ink/10 bg-white dark:border-white/10 dark:bg-white/10" href="/cart" aria-label="Cart">
              <ShoppingBag size={18} />
            </Link>
            <Link className="inline-flex h-10 w-10 items-center justify-center rounded-md border border-ink/10 bg-white dark:border-white/10 dark:bg-white/10" href="/login" aria-label="Account">
              <UserRound size={18} />
            </Link>
            <LanguageToggle />
            <ThemeToggle />
          </div>
        </div>
      </header>
      {children}
      <footer className="border-t border-ink/10 px-4 py-8 text-sm dark:border-white/10">
        <div className="mx-auto flex max-w-7xl flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <p>{t.brand} helps buyers discover digital products and services from independent creators.</p>
          <div className="flex gap-4">
            <Link href="/privacy-policy">{t.privacy}</Link>
            <Link href="/terms-of-service">{t.terms}</Link>
            <Link href="/contact">{t.contact}</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
