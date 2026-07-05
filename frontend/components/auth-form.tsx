"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { Role, useAccount } from "./account-provider";
import { useI18n } from "./i18n-provider";

export function AuthForm({ mode }: { mode: "login" | "register" | "forgot" | "reset" }) {
  const { t } = useI18n();
  const { signIn } = useAccount();
  const router = useRouter();
  const isRegister = mode === "register";
  const title = mode === "login" ? t.login : mode === "register" ? t.register : mode === "forgot" ? "Forgot password" : "Reset password";
  const handleAuth = (role: Role) => {
    signIn(role);
    router.push(role === "seller" ? "/seller-dashboard" : role === "admin" ? "/admin-dashboard" : "/buyer-dashboard");
  };

  return (
    <main className="mx-auto max-w-md px-4 py-10">
      <h1 className="mb-6 text-3xl font-semibold">{title}</h1>
      <form className="space-y-4 rounded-md border border-ink/10 bg-white p-5 shadow-sm dark:border-white/10 dark:bg-white/10">
        {isRegister ? <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.name} /> : null}
        <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.email} type="email" />
        {mode !== "forgot" ? <input className="w-full rounded-md border border-ink/10 bg-transparent px-3 py-3 dark:border-white/10" placeholder={t.password} type="password" /> : null}
        {mode === "forgot" || mode === "reset" ? (
          <button className="w-full rounded-md bg-coral px-4 py-3 font-semibold text-white" type="button">{title}</button>
        ) : (
          <div className="grid gap-2">
            <button className="w-full rounded-md bg-coral px-4 py-3 font-semibold text-white" onClick={() => handleAuth("buyer")} type="button">
              {title} as buyer
            </button>
            <button className="w-full rounded-md border border-ink/10 px-4 py-3 font-semibold dark:border-white/10" onClick={() => handleAuth("seller")} type="button">
              {title} as seller
            </button>
            <button className="w-full rounded-md border border-ink/10 px-4 py-3 font-semibold dark:border-white/10" onClick={() => handleAuth("admin")} type="button">
              {title} as administrator
            </button>
          </div>
        )}
        <div className="flex justify-between text-sm text-ink/70 dark:text-mist/70">
          <Link href="/login">{t.login}</Link>
          <Link href="/register">{t.register}</Link>
          <Link href="/forgot-password">Forgot</Link>
        </div>
      </form>
    </main>
  );
}
