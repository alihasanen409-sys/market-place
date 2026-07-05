import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#17201d",
        moss: "#4f6f52",
        coral: "#ff6b5f",
        gold: "#f6c85f",
        mist: "#edf5f0"
      },
      boxShadow: {
        soft: "0 18px 50px rgba(23, 32, 29, 0.12)"
      }
    }
  },
  plugins: []
};

export default config;
