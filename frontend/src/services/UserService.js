import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

export const getUsersList = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/users/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching Users:', error);
        throw new Error('Failed to fetch Users');
    }
};