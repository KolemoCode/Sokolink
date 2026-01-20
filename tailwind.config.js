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
        jungle:'#0B5D1E',
        jungleDark: '#084516',
        jungleLight: "#2ea88a",
        brandYellow: "#facc15",
        yellow: '#FACC15',
      },
    },
  },
  plugins: [],
}

