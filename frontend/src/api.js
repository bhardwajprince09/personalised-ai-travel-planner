import axios from 'axios'


const API_BASE = import.meta.env.VITE_API_BASE || '/api'


export const createTrip = (payload) => axios.post(`${API_BASE}/trips`, payload)
