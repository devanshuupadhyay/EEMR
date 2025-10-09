// composables/theme.js
// Enterprise-grade futuristic theme for Easy EMR
// Centralized theme configuration for consistency

export const useTheme = () => {
  return {
    // 🎨 Color System
    colors: {
      primary: "#17A2B8", // Muted Teal
      secondary: "#17A2B8", // Muted Teal
      neutral: {
        darkest: "#0B0C10", // App background (dark mode foundation)
        dark: "#1C1F26", // Panels / cards
        medium: "#2C2F38", // Borders & subtle lines
        light: "#9CA3AF", // Secondary text
        lighter: "#D1D5DB", // Muted text
        lightest: "#F3F4F6", // Main text
      },
    },

    // 🔠 Typography
    typography: {
      fontFamily: "Inter, Poppins, sans-serif",
      headings: "font-semibold tracking-tight",
      body: "font-normal leading-relaxed",
      sizes: {
        h1: "text-3xl font-extrabold",
        h2: "text-2xl font-bold",
        h3: "text-xl font-semibold",
        body: "text-base md:text-lg",
        small: "text-sm",
      },
    },

    // 🧩 Components
    components: {
      button: {
        // --- UPDATED: Reduced vertical padding ---
        base: "px-4 py-1.5 rounded-lg font-semibold transition-all duration-300",
        primary:
          "bg-primary text-white hover:shadow-[0_0_15px_#00F5D4aa] hover:scale-105 active:scale-95",
        secondary:
          "bg-secondary text-black hover:shadow-[0_0_15px_#00F5D4aa] hover:scale-105 active:scale-95",
      },
      input: {
        // --- UPDATED: Reduced vertical padding ---
        base: "w-full px-4 py-1.5 rounded-md bg-neutral-dark border border-neutral-medium text-neutral-lightest placeholder-neutral-light focus:outline-none focus:ring-2 focus:ring-secondary",
        // --- NEW: Compact version for tables ---
        compact: "w-full px-2 py-1 rounded-md bg-neutral-dark border border-neutral-medium text-neutral-lightest placeholder-neutral-light focus:outline-none focus:ring-1 focus:ring-secondary",
        // --- NEW: Datepicker style with icon filter applied via arbitrary variants ---
        datepicker: "w-full px-2 py-1 rounded-md bg-neutral-dark border border-neutral-medium text-neutral-lightest focus:outline-none focus:ring-1 focus:ring-secondary [&::-webkit-calendar-picker-indicator]:(filter-none invert-70 sepia-1 saturate-5 hue-rotate-150)"
      },
      card: {
        // --- UPDATED: Reduced padding ---
        base: "rounded-2xl p-4 border border-neutral-medium bg-neutral-dark shadow-lg hover:shadow-[0_0_25px_-5px_rgba(0,245,212,0.25)] transition-all duration-300",
         // --- NEW: Compact version for less vertical space ---
        compact: "rounded-xl p-3 border border-neutral-medium bg-neutral-dark shadow-lg hover:shadow-[0_0_25px_-5px_rgba(0,245,212,0.25)] transition-all duration-300",
      },
      nav: {
        link: "flex items-center gap-2 px-3 py-2 rounded-md text-neutral-light hover:text-secondary hover:bg-neutral-medium transition",
        active: "text-secondary font-semibold border-l-4 border-secondary bg-neutral-medium",
      },
      table: {
        header: "border-b border-neutral-700",
        row: "border-b border-neutral-medium hover:bg-primary text-sm",
      },
    },

    // 📊 Data Viz Defaults
    charts: {
      line: { stroke: "#00F5D4", point: "#0F4C5C" },
      bar: { fill: "#0F4C5C" },
      accent: "#00F5D4",
    },
  }
}