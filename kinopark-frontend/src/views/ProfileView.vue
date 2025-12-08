<template>
  <div class="profile-page">
    <div class="profile-container">
      <!-- Sidebar -->
      <aside class="profile-sidebar">
        <div class="profile-header">
          <div class="avatar">
            {{ initials }}
          </div>
          <h2 class="user-name">{{ user?.first_name }} {{ user?.last_name }}</h2>
          <p class="user-email">{{ user?.email }}</p>
        </div>

        <nav class="profile-nav">
          <button 
            @click="activeTab = 'profile'" 
            :class="{ active: activeTab === 'profile' }"
            class="nav-item"
          >
            Профиль
          </button>
          <button 
            @click="activeTab = 'password'" 
            :class="{ active: activeTab === 'password' }"
            class="nav-item"
          >
            Изменить пароль
          </button>
          <button 
            @click="activeTab = 'danger'" 
            :class="{ active: activeTab === 'danger' }"
            class="nav-item danger"
          >
            Опасная зона
          </button>
          <button @click="handleLogout" class="nav-item logout">
            Выход
          </button>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="profile-content">
        <!-- Редактирование профиля -->
        <div v-if="activeTab === 'profile'" class="content-section">
          <h1 class="section-title">Редактировать профиль</h1>
          
          <form @submit.prevent="handleUpdateProfile" class="profile-form">
            <div class="form-row">
              <div class="form-group">
                <label>Имя</label>
                <input
                  v-model="profileData.first_name"
                  type="text"
                  required
                />
              </div>

              <div class="form-group">
                <label>Фамилия</label>
                <input
                  v-model="profileData.last_name"
                  type="text"
                  required
                />
              </div>
            </div>

            <div class="form-group">
              <label>Email</label>
              <input
                v-model="profileData.email"
                type="email"
                required
              />
            </div>

            <div class="form-group">
              <label>Телефон</label>
              <input
                v-model="profileData.phone"
                type="tel"
                placeholder="+7 (___) ___-__-__"
              />
            </div>

            <div v-if="successMessage" class="success-message">
              {{ successMessage }}
            </div>

            <div v-if="error" class="error-message">
              {{ error }}
            </div>

            <button type="submit" class="btn-primary" :disabled="loading">
              <span v-if="loading">Сохранение...</span>
              <span v-else>Сохранить изменения</span>
            </button>
          </form>
        </div>

        <!-- Изменение пароля -->
        <div v-if="activeTab === 'password'" class="content-section">
          <h1 class="section-title">Изменить пароль</h1>
          
          <form @submit.prevent="handleChangePassword" class="profile-form">
            <div class="form-group">
              <label>Текущий пароль</label>
              <input
                v-model="passwordData.old_password"
                type="password"
                required
              />
            </div>

            <div class="form-group">
              <label>Новый пароль</label>
              <input
                v-model="passwordData.new_password"
                type="password"
                required
              />
            </div>

            <div class="form-group">
              <label>Подтвердите новый пароль</label>
              <input
                v-model="passwordData.confirm_password"
                type="password"
                required
              />
            </div>

            <div v-if="successMessage" class="success-message">
              {{ successMessage }}
            </div>

            <div v-if="error" class="error-message">
              {{ error }}
            </div>

            <button type="submit" class="btn-primary" :disabled="loading">
              <span v-if="loading">Изменение...</span>
              <span v-else>Изменить пароль</span>
            </button>
          </form>
        </div>

        <!-- Опасная зона -->
        <div v-if="activeTab === 'danger'" class="content-section">
          <h1 class="section-title danger-title">Опасная зона</h1>
          
          <div class="danger-zone">
            <div class="danger-item">
              <div class="danger-info">
                <h3>Удалить аккаунт</h3>
                <p>Это действие необратимо. Все ваши данные будут удалены навсегда.</p>
              </div>
              <button @click="showDeleteModal = true" class="btn-danger">
                Удалить аккаунт
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>

    <!-- Модальное окно удаления -->
    <div v-if="showDeleteModal" class="modal-overlay" @click="showDeleteModal = false">
      <div class="modal" @click.stop>
        <h2 class="modal-title">Удалить аккаунт</h2>
        <p class="modal-text">
          Это действие необратимо. Для продолжения введите ваш пароль.
        </p>

        <form @submit.prevent="handleDeleteAccount" class="modal-form">
          <div class="form-group">
            <label>Пароль</label>
            <input
              v-model="deletePassword"
              type="password"
              required
              placeholder="Введите пароль"
            />
          </div>

          <div class="form-group checkbox-group">
            <label class="checkbox-label">
              <input
                v-model="deleteConfirm"
                type="checkbox"
                required
              />
              <span>Я подтверждаю, что хочу удалить свой аккаунт</span>
            </label>
          </div>

          <div v-if="error" class="error-message">
            {{ error }}
          </div>

          <div class="modal-actions">
            <button type="button" @click="closeDeleteModal" class="btn-secondary">
              Отмена
            </button>
            <button type="submit" class="btn-danger" :disabled="loading">
              <span v-if="loading">Удаление...</span>
              <span v-else>Удалить</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>

import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const router = useRouter()
const authStore = useAuthStore()

const user = computed(() => authStore.user)
const loading = computed(() => authStore.loading)

const activeTab = ref('profile')
const error = ref('')
const successMessage = ref('')

// Данные профиля
const profileData = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
})

// Данные пароля
const passwordData = ref({
  old_password: '',
  new_password: '',
  confirm_password: ''
})

// Данные удаления
const showDeleteModal = ref(false)
const deletePassword = ref('')
const deleteConfirm = ref(false)

// Инициалы
const initials = computed(() => {
  if (!user.value) return 'U'
  const first = user.value.first_name?.[0] || ''
  const last = user.value.last_name?.[0] || ''
  return (first + last).toUpperCase() || 'U'
})

// Обновить профиль
const handleUpdateProfile = async () => {
  error.value = ''
  successMessage.value = ''

  try {
    await authStore.updateProfile(profileData.value)
    successMessage.value = 'Профиль успешно обновлен'
    setTimeout(() => successMessage.value = '', 3000)
  } catch (err) {
    error.value = err.response?.data?.error || 'Произошла ошибка'
  }
}

// Изменить пароль
const handleChangePassword = async () => {
  error.value = ''
  successMessage.value = ''

  if (passwordData.value.new_password !== passwordData.value.confirm_password) {
    error.value = 'Новые пароли не совпадают'
    return
  }

  try {
    await authStore.changePassword({
      old_password: passwordData.value.old_password,
      new_password: passwordData.value.new_password
    })
    
    successMessage.value = 'Пароль успешно изменен'
    passwordData.value = { old_password: '', new_password: '', confirm_password: '' }
    setTimeout(() => successMessage.value = '', 3000)
  } catch (err) {
    error.value = err.response?.data?.error || 'Произошла ошибка'
  }
}

// Удалить аккаунт
const handleDeleteAccount = async () => {
  error.value = ''

  if (!deleteConfirm.value) {
    error.value = 'Подтвердите удаление аккаунта'
    return
  }

  try {
    await authStore.deleteAccount(deletePassword.value)
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.error || 'Произошла ошибка'
  }
}

// Закрыть модальное окно
const closeDeleteModal = () => {
  showDeleteModal.value = false
  deletePassword.value = ''
  deleteConfirm.value = false
  error.value = ''
}

// Выход
const handleLogout = async () => {
  await authStore.logout()
  router.push('/login')
}

// Загрузить данные
onMounted(() => {
  if (user.value) {
    profileData.value = {
      first_name: user.value.first_name || '',
      last_name: user.value.last_name || '',
      email: user.value.email || '',
      phone: user.value.phone || ''
    }
  }
})
</script>

<style scoped>
.profile-page {
  min-height: 100vh;
  background-color: #f5f7fa;
  padding: 2rem;
}

.profile-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 2rem;
}

/* Sidebar */
.profile-sidebar {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  height: fit-content;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #e0e0e0;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1a1a2e 0%, #e50914 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 700;
  margin: 0 auto 1rem;
}

.user-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.user-email {
  font-size: 0.9rem;
  color: #666;
}

.profile-nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav-item {
  padding: 0.875rem 1rem;
  background: transparent;
  border: none;
  border-radius: 8px;
  text-align: left;
  font-size: 1rem;
  color: #333;
  cursor: pointer;
  transition: all 0.2s;
}

.nav-item:hover {
  background-color: #f5f5f5;
}

.nav-item.active {
  background-color: #e50914;
  color: white;
}

.nav-item.danger {
  color: #e53e3e;
}

.nav-item.danger:hover {
  background-color: #fee;
}

.nav-item.logout {
  margin-top: 1rem;
  color: #666;
  border-top: 1px solid #e0e0e0;
  padding-top: 1.5rem;
}

/* Content */
.profile-content {
  background: white;
  border-radius: 16px;
  padding: 2.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 2rem;
}

.danger-title {
  color: #e53e3e;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-width: 600px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="tel"],
.form-group input[type="password"] {
  padding: 0.875rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #e50914;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
}

.checkbox-label input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.success-message {
  background-color: #d4edda;
  color: #155724;
  padding: 0.875rem;
  border-radius: 8px;
  font-size: 0.9rem;
}

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 0.875rem;
  border-radius: 8px;
  font-size: 0.9rem;
}

.btn-primary {
  background-color: #e50914;
  color: white;
  border: none;
  padding: 1rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(229, 9, 20, 0.4);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Danger Zone */
.danger-zone {
  border: 2px solid #e53e3e;
  border-radius: 12px;
  padding: 2rem;
}

.danger-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.danger-info h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.danger-info p {
  color: #666;
  font-size: 0.9rem;
}

.btn-danger {
  background-color: #e53e3e;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background-color 0.3s;
}

.btn-danger:hover:not(:disabled) {
  background-color: #c53030;
}

.btn-danger:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  max-width: 500px;
  width: 90%;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.modal-text {
  color: #666;
  margin-bottom: 1.5rem;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.btn-secondary {
  flex: 1;
  background-color: #e0e0e0;
  color: #333;
  border: none;
  padding: 0.875rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-secondary:hover {
  background-color: #d0d0d0;
}

@media (max-width: 768px) {
  .profile-container {
    grid-template-columns: 1fr;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .danger-item {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>