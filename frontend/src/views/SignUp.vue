<template>
  <div class="min-h-screen flex items-center justify-center px-4">
    <div class="w-full max-w-md bg-white shadow-md rounded-lg p-8">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Sign Up</h2>

      <form @submit.prevent="handleSignUp" class="space-y-4">
        <div>
          <label class="block text-gray-700 mb-1" for="username">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            required
            class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="yourusername"
          />
        </div>

        <div class="flex gap-4">
          <div class="flex-1">
            <label class="block text-gray-700 mb-1" for="firstName">First Name</label>
            <input
              v-model="firstName"
              id="firstName"
              type="text"
              required
              class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="John"
            />
          </div>

          <div class="flex-1">
            <label class="block text-gray-700 mb-1" for="lastName">Last Name</label>
            <input
              v-model="lastName"
              id="lastName"
              type="text"
              required
              class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Doe"
            />
          </div>
        </div>

        <div>
          <label class="block text-gray-700 mb-1" for="email">Email</label>
          <input
            v-model="email"
            id="email"
            type="email"
            required
            class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="you@example.com"
          />
        </div>

        <div>
          <label class="block text-gray-700 mb-1" for="password">Password</label>
          <input
            v-model="password"
            id="password"
            type="password"
            required
            class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
          />
        </div>

        <div>
          <label class="block text-gray-700 mb-1" for="confirmPassword">Confirm Password</label>
          <input
            v-model="confirmPassword"
            id="confirmPassword"
            type="password"
            required
            class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
          />
        </div>

        <div v-if="passwordMismatch" class="text-red-500 text-sm">
          Passwords do not match.
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
        >
          Sign Up
        </button>
      </form>

      <RouterLink
        to="/"
        class="block text-center mt-6 text-blue-600 hover:underline text-sm"
      >
        ← Back to Home
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const firstName = ref('')
const lastName = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const router = useRouter()

const passwordMismatch = computed(() => password.value !== confirmPassword.value)

const handleSignUp = async () => {
  if (passwordMismatch.value) {
    alert('Passwords do not match!')
    return
  }

  try {
    const response = await axios.post(
      'http://localhost:8000/signup',
      {
        username: username.value,
        email: email.value,
        password: password.value,
        first_name: firstName.value,
        last_name: lastName.value
      },
      {
        withCredentials: true,
      }
    )

    alert(response.data.message || 'Sign up successful')
    router.push('/signin')

  } catch (error: any) {
    alert(error.response?.data?.error || 'Sign up failed')
  }
}
</script>

