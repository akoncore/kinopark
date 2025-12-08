// src/stores/authStore.js
import { defineStore } from 'pinia'
import { AuthAPI } from '@/services/AuthService'
import { userAPI } from '@/services/userService'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    loading: false,
    error: null,
  }),

  getters: {
    currentUser: (state) => state.user,
    isLoggedIn: (state) => state.isAuthenticated,
  },

  actions: {
    // Регистрация
    async register(userData) {
      this.loading = true
      this.error = null
      try {
        const response = await AuthAPI.register(userData)
        
        // Сохранение токенов
        localStorage.setItem('access_token', response.data.tokens.access)
        localStorage.setItem('refresh_token', response.data.tokens.refresh)
        
        this.user = response.data.user
        this.isAuthenticated = true
        
        return response.data
      } catch (error) {
        this.error = error.response?.data?.error || 'Ошибка регистрации'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Вход
    async login(credentials) {
      this.loading = true
      this.error = null
      try {
        const response = await AuthAPI.login(credentials)
        
        // Сохранение токенов
        localStorage.setItem('access_token', response.data.tokens.access)
        localStorage.setItem('refresh_token', response.data.tokens.refresh)
        
        this.user = response.data.user
        this.isAuthenticated = true
        
        return response.data
      } catch (error) {
        this.error = error.response?.data?.error || 'Ошибка входа'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Выход
    async logout() {
      this.loading = true
      try {
        const refreshToken = localStorage.getItem('refresh_token')
        await AuthAPI.logout({ refresh: refreshToken })
      } catch (error) {
        console.error('Logout error:', error)
      } finally {
        // Удаление токенов
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        
        this.user = null
        this.isAuthenticated = false
        this.loading = false
      }
    },

    // Получить текущего пользователя
    async fetchCurrentUser() {
      try {
        const response = await userAPI.getCurrentUser()
        this.user = response.data
        this.isAuthenticated = true
      } catch (error) {
        console.error('Fetch user error:', error)
        this.user = null
        this.isAuthenticated = false
      }
    },

    // Обновить профиль
    async updateProfile(data) {
      this.loading = true
      this.error = null
      try {
        const response = await userAPI.updateProfile(data)
        this.user = response.data.result
        return response.data
      } catch (error) {
        this.error = error.response?.data?.error || 'Ошибка обновления профиля'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Изменить пароль
    async changePassword(passwordData) {
      this.loading = true
      this.error = null
      try {
        const response = await userAPI.changePAssword(passwordData)
        
        // Обновить токены после смены пароля
        if (response.data.tokens) {
          localStorage.setItem('access_token', response.data.tokens.access)
          localStorage.setItem('refresh_token', response.data.tokens.refresh)
        }
        
        return response.data
      } catch (error) {
        this.error = error.response?.data?.error || 'Ошибка изменения пароля'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Удалить аккаунт
    async deleteAccount(password) {
      this.loading = true
      this.error = null
      try {
        await userAPI.deleteUser(password, 'DELETE')
        await this.logout()
      } catch (error) {
        this.error = error.response?.data?.error || 'Ошибка удаления аккаунта'
        throw error
      } finally {
        this.loading = false
      }
    },

    // Очистить ошибку
    clearError() {
      this.error = null
    },

    // Проверить аутентификацию
    checkAuth() {
      const token = localStorage.getItem('access_token')
      if (token) {
        this.isAuthenticated = true
        this.fetchCurrentUser()
      }
    }
  }
})