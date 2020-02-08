module.exports = {
    theme: {
        colors: {
            green: '#619F21',
            black: '#263238', //text
            black_p: '#37474f', // text description or long text
            lightGray: '#afbcc2',
            white: '#FFFFFF',
            red: '#e24c48',
            orange: '#EF6C00',
            gray: '#707070', // textfield
            gray_bg: '#e3e4e3',
            unHilight: '#f5f5f5'
        },
        fontFamily: {
            display: ['Kanit', 'sans-serif'],
            body: ['Kanit', 'sans-serif'],
        },
        extend: {
            colors: {
                maingreen: '#619F21'
            },
            width: {
                '4/1':'400%',
                '2/1':'200%',
                '16/10':'160%',
                '266per':'266%'
            },
            screens: {
                'sc-1400':'1400px',
                'sc-480':{'min': '480px', 'max': '640px'}
            }
        },
    },
    variants: {},
    plugins: []
}
