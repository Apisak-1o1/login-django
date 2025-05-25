<!-- src/views/Home.vue -->
<template>
  <div class="home">
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="100" height="100" />
    <h1>Welcome to My App</h1>
    <div class="button-group">
      <RouterLink to="/signin" class="btn">Sign In</RouterLink>
      <RouterLink to="/signup" class="btn">Sign Up</RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.logo {
  margin-bottom: 1rem;
}

h1 {
  margin-bottom: 1.5rem;
  font-size: 2rem;
  color: #2c3e50;
}

.button-group {
  display: flex;
  gap: 1rem;
}

.btn {
  background-color: #42b983;
  color: white;
  padding: 0.7rem 1.5rem;
  border: none;
  border-radius: 6px;
  text-decoration: none;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #36976b;
}
</style>
