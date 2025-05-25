<template>
  <div class="min-h-screen flex items-center justify-center px-4">
    <div class="w-full max-w-md bg-white shadow-md rounded-lg p-8">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Sign In</h2>

      <form @submit.prevent="handleSignIn" class="space-y-4">
        <div>
          <label class="block text-gray-700 mb-1" for="username">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            required
            class="text-black w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Username"
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

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
        >
          Sign In
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
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const API_URL = 'http://localhost:8000/signin'

const handleSignIn = async () => {
  try {
    const response = await axios.post(
      API_URL,
      {
        username: username.value,
        password: password.value
      },
      {
        withCredentials: true,
      }
    )

    alert(response.data.message)
  } catch (error: any) {
    alert(error.response?.data?.error || 'Login failed')
  }
}
</script>
