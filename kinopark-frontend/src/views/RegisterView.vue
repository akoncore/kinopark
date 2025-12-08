<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="auth-card">
        <h1 class="auth-title">Регистрация</h1>
        
        <form @submit.prevent="handleRegister" class="auth-form">
          <!-- Имя -->
          <div class="form-group">
            <label for="first_name">Имя</label>
            <input
              id="first_name"
              v-model="formData.first_name"
              type="text"
              required
              placeholder="Введите ваше имя"
            />
          </div>

          <!-- Фамилия -->
          <div class="form-group">
            <label for="last_name">Фамилия</label>
            <input
              id="last_name"
              v-model="formData.last_name"
              type="text"
              required
              placeholder="Введите вашу фамилию"
            />
          </div>

          <!-- Email -->
          <div class="form-group">
            <label for="email">Email</label>
            <input
              id="email"
              v-model="formData.email"
              type="email"
              required
              placeholder="example@mail.com"
            />
          </div>

          <!-- Телефон (опционально) -->
          <div class="form-group">
            <label for="phone">Телефон</label>
            <input
              id="phone"
              v-model="formData.phone"
              type="tel"
              placeholder="+7 (___) ___-__-__"
            />
          </div>

          <!-- Пароль -->
          <div class="form-group">
            <label for="password">Пароль</label>
            <input
              id="password"
              v-model="formData.password"
              type="password"
              required
              placeholder="••••••••"
            />
          </div>

          <!-- Подтверждение пароля -->
          <div class="form-group">
            <label for="password2">Подтвердите пароль</label>
            <input
              id="password2"
              v-model="formData.password2"
              type="password"
              required
              placeholder="••••••••"
            />
          </div>

          <!-- Сообщение об ошибке -->
          <div v-if="error" class="error-message">
            {{ error }}
          </div>

          <!-- Кнопка регистрации -->
          <button 
            type="submit" 
            class="btn-submit"
            :disabled="loading"
          >
            <span v-if="loading">Загрузка...</span>
            <span v-else>Зарегистрироваться</span>
          </button>
        </form>

        <div class="auth-footer">
          <p>
            Уже есть аккаунт? 
            <router-link to="/login" class="link">Войти</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const router = useRouter()
const authStore = useAuthStore()

const formData = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
  password: '',
  password2: ''
})

const loading = ref(false)
const error = ref('')

const handleRegister = async () => {
  error.value = ''
  
  // Проверка паролей
  if (formData.value.password !== formData.value.password2) {
    error.value = 'Пароли не совпадают'
    return
  }

  loading.value = true

  try {
    await authStore.register(formData.value)
    router.push('/')
  } catch (err) {
    error.value = err.response?.data?.error || 'Ошибка регистрации'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.auth-container {
  width: 100%;
  max-width: 500px;
}

.auth-card {
  background: white;
  border-radius: 16px;
  padding: 3rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.auth-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 2rem;
  text-align: center;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
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

.form-group input {
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

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 0.875rem;
  border-radius: 8px;
  font-size: 0.9rem;
  text-align: center;
}

.btn-submit {
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

.btn-submit:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(229, 9, 20, 0.4);
}

.btn-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.auth-footer {
  margin-top: 2rem;
  text-align: center;
  color: #666;
}

.link {
  color: #e50914;
  text-decoration: none;
  font-weight: 600;
}

.link:hover {
  text-decoration: underline;
}

@media (max-width: 640px) {
  .auth-card {
    padding: 2rem;
  }
}
</style>