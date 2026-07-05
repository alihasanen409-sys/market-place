import Link from "next/link";

export default function NotFound() {
  return (
    <main className="mx-auto max-w-xl px-4 py-20 text-center">
      <h1 className="text-4xl font-semibold">404</h1>
      <p className="mt-3 text-ink/70 dark:text-mist/70">This page could not be found.</p>
      <Link className="mt-6 inline-block rounded-md bg-coral px-4 py-2 font-semibold text-white" href="/">Go home</Link>
    </main>
  );
}
