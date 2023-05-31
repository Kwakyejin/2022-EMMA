const config = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
  ],

  theme: {
    extend: {
      colors: {
        bg: "#9CB7FF",
        point: "#7BA0FF",
        background: "#5C5C5C",
        border: "#C2C2DA",
        lightpoint: "#EAF0FF",
        scrollbar: "#D5D5E5",
        active: "#57589B",
      },
    },
  },

  plugins: [require("flowbite/plugin")],
  darkMode: "class",
};

module.exports = config;
