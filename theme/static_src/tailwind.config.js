/** @type {import('tailwindcss').Config} */

module.exports = {
    mode: "jit",
    content: [
      '../../**/templates/**/*.html',
    ],
    theme: {
      extend: {
        textColor: {
          'green': 'rgb(27, 42, 38)',
          'brown': 'rgb(242,212,53)',
          'violet': 'rgb(10,16,53)',
        },
        backgroundColor: {
          'lime': 'rgb(38, 105, 89)',
        },
        boxShadow: {
          '0_9px_0_rgb(0,0,0)': '0 9px 0 rgba(0, 0, 0, 0.1)',
          '0_4px_0px_rgb(0,0,0)': '0 4px 0 rgba(0, 0, 0, 0.1)',
        },
        fontFamily: {
          'font-Viga': ['Viga', 'sans-serif'],
          'font-IM':['IM Fell English SC', 'serif'],
          'bungee': ['Bungee Spice', 'cursive'],
          'im-fell': ['IM Fell English SC', 'serif'],
          'paytone': ['Paytone One', 'sans-serif'],
        },
      },
      screens: {
        'sm': '740px',  // Personnalisez la taille pour sm comme vous le souhaitez
        'md': '1000px',
        'lg': '1600px',
        'xl': '2280px',
      },
    },
    variants: {
      extend: {
        overflowX: ['responsive', 'hover'], // Ajout de la propriété overflowX
      },
    },
    plugins: [],
  }
  