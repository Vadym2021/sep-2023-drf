const baseURL = '/api'
const socketBaseUrl = 'ws://localhost/api'
const auth = '/auth'
const cars = '/cars'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    },
    cars
}

export {
    baseURL,
    socketBaseUrl,
    urls
}