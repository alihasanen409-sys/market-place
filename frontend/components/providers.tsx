"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ThemeProvider } from "next-themes";
import { ReactNode, useState } from "react";
import { I18nProvider } from "./i18n-provider";
import { AccountProvider } from "./account-provider";

export function Providers({ children }: { children: ReactNode }) {
  const [queryClient] = useState(() => new QueryClient());

  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      <I18nProvider>
        <AccountProvider>
          <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
        </AccountProvider>
      </I18nProvider>
    </ThemeProvider>
  );
}
