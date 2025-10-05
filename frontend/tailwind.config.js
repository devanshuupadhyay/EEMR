/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{vue,js,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./app.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}"
  ],
  theme: {
    extend: {
      colors: {
        secondary: "#17A2B8",
        primary: "#005A9C",
        neutral: {
          darkest: "#0B0C10",
          dark: "#1C1F26",
          medium: "#2C2F38",
          light: "#9CA3AF",
          lighter: "#D1D5DB",
          lightest: "#F3F4F6",
        },
      }
    },
  },
  plugins: [],
};