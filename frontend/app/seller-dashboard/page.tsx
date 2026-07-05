import { DashboardPage } from "@/components/dashboard-page";
import Link from "next/link";

export default function SellerDashboardPage() {
  return (
    <>
      <DashboardPage role="seller" />
      <div className="mx-auto -mt-4 mb-8 max-w-7xl px-4">
        <Link className="inline-block rounded-md bg-coral px-4 py-3 font-semibold text-white" href="/create-listing">Add product</Link>
      </div>
    </>
  );
}
