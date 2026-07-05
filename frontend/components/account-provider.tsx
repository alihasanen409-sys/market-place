"use client";

import { createContext, ReactNode, useContext, useEffect, useMemo, useState } from "react";

export type Role = "buyer" | "seller" | "admin";

type AccountContextValue = {
  role: Role;
  signedIn: boolean;
  signIn: (role: Role) => void;
  signOut: () => void;
};

const AccountContext = createContext<AccountContextValue | null>(null);

export function AccountProvider({ children }: { children: ReactNode }) {
  const [role, setRole] = useState<Role>("buyer");
  const [signedIn, setSignedIn] = useState(false);

  useEffect(() => {
    const savedRole = window.localStorage.getItem("role") as Role | null;
    const savedSignedIn = window.localStorage.getItem("signedIn") === "true";
    if (savedRole === "buyer" || savedRole === "seller" || savedRole === "admin") {
      setRole(savedRole);
    }
    setSignedIn(savedSignedIn);
  }, []);

  const value = useMemo<AccountContextValue>(
    () => ({
      role,
      signedIn,
      signIn: (nextRole) => {
        setRole(nextRole);
        setSignedIn(true);
        window.localStorage.setItem("role", nextRole);
        window.localStorage.setItem("signedIn", "true");
      },
      signOut: () => {
        setSignedIn(false);
        window.localStorage.setItem("signedIn", "false");
      }
    }),
    [role, signedIn]
  );

  return <AccountContext.Provider value={value}>{children}</AccountContext.Provider>;
}

export function useAccount() {
  const value = useContext(AccountContext);
  if (!value) {
    throw new Error("useAccount must be used inside AccountProvider");
  }
  return value;
}
