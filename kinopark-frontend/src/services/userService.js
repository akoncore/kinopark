import api from "./api";

export const userAPI = {
    getALL: () => api.get('api/v1/users/'),

    retreive: (userId) => api.get(`api/v1/users/${userId}/`),   

    getCurrentUser: () => api.get('api/v1/users/me/'),

    updateProfile: (data) => api.put('api/v1/users/me/update', data),

    changePAssword: (data) => api.post('api/v1/users/change-password', data),

    deactivate: (password) => api.delete('api/v1/users/deactivate/',{password: password}),

    deleteUser: (password,confirm) => api.delete(`api/v1/users/delete/`,{password:password, confirm: confirm}),
}