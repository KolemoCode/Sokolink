/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
        colors: {
        jungle: "#1f7a63",
        jungleDark: "#155e4a",
        jungleLight: "#2ea88a",
        brandYellow: "#facc15",
      },
    },
  },
  plugins: [],
}

