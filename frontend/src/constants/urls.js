const baseURL = '/api'
const socketBaseUrl = 'ws://localhost/api'
const auth = '/auth'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    }
}

export {
    baseURL,
    socketBaseUrl,
    urls
}