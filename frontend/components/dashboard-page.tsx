"use client";

import { BarChart3, DollarSign, Package, Users } from "lucide-react";
import { DashboardPanel } from "./dashboard-panel";
import { useI18n } from "./i18n-provider";

export function DashboardPage({ role }: { role: "buyer" | "seller" | "admin" }) {
  const { t } = useI18n();
  const title = role === "buyer" ? `${t.buyer} ${t.dashboard}` : role === "seller" ? `${t.seller} ${t.dashboard}` : `${t.admin} ${t.dashboard}`;
  const metrics = role === "buyer"
    ? [["Open orders", "2", Package], ["Favorites", "8", Users], ["Unread messages", "3", BarChart3]]
    : role === "seller"
      ? [["Sales", "$1,240", DollarSign], ["Listings", "14", Package], ["Rating", "4.8", BarChart3]]
      : [["Users", "842", Users], ["Orders", "309", Package], ["Reports", "5", BarChart3]];

  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-semibold">{title}</h1>
      <div className="mb-6 grid gap-4 md:grid-cols-3">
        {metrics.map(([label, value, Icon]) => (
          <DashboardPanel title={label as string} key={label as string}>
            <div className="flex items-center justify-between">
              <strong className="text-3xl">{value as string}</strong>
              <Icon className="text-coral" />
            </div>
          </DashboardPanel>
        ))}
      </div>
      <DashboardPanel title="Recent activity">
        <div className="space-y-3 text-sm text-ink/75 dark:text-mist/75">
          <p>New order confirmed with simulated payment.</p>
          <p>Message thread updated.</p>
          <p>Listing performance refreshed.</p>
        </div>
      </DashboardPanel>
    </main>
  );
}
