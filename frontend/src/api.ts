import axios from "axios";

const backendBaseUrl = 'http://localhost:8000';

export const api = axios.create({
    baseURL: backendBaseUrl,
    headers: {
        'Content-Type': 'application/json',
        // authentication headers can go here
    },
})

// example api functions:
export const createAccount: any = (userData: any) => api.post('/create-account', userData)
export const getUserAccounts: any = () => api.get('/accounts')