
import api from "./api";

export const AuthAPI = {
    register : (data) => api.post(
        'api/v1/auth/register/', data
    ), 
    login : (credentials) => api.post(
        'api/v1/auth/login/', credentials
    ),
    logout : () => api.post(
        'api/v1/auth/logout/'
    ),
    refreshToken : (refreshToken) => api.post(
        'api/v1/auth/refresh/', {refresh}
    ),
    verifyToken : (token) => api.post(
        'api/v1/auth/verify/', {token}
    ),
}