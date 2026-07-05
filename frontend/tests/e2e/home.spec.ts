import { expect, test } from "@playwright/test";

test("home page has marketplace search", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("textbox")).toBeVisible();
  await expect(page.getByRole("link", { name: /marketplace/i }).first()).toBeVisible();
});
