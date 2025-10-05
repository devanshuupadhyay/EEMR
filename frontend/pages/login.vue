<template>
  <div class="max-w-md mx-auto mt-20 p-4 border rounded shadow bg-neutral-dark border-neutral-medium">
    <h2 class="text-2xl font-bold mb-4 text-center">{{ isSignup ? "Sign Up" : "Login" }}</h2>

    <form @submit.prevent="handleSubmit" class="space-y-3">
      <input v-model="username" placeholder="Username" :class="theme.components.input.base" required />
      <input v-if="isSignup" v-model="email" placeholder="Email" :class="theme.components.input.base" required />
      <input v-model="password" type="password" placeholder="Password" :class="theme.components.input.base" required />
      <button type="submit" :class="[theme.components.button.base, theme.components.button.primary, 'w-full']">
        {{ isSignup ? "Sign Up" : "Login" }}
      </button>
    </form>

    <p class="text-center text-sm text-gray-400 mt-4">
      <span @click="toggleForm" class="cursor-pointer hover:text-primary transition">
        {{ isSignup ? "Already have an account? Login" : "Don't have an account? Sign Up" }}
      </span>
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const theme = useTheme();
const isSignup = ref(false);
const username = ref("");
const email = ref("");
const password = ref("");

const toggleForm = () => {
  isSignup.value = !isSignup.value;
};

const handleSubmit = async () => {
  try {
    if (isSignup.value) {
      await axios.post("http://localhost:8000/signup", {
        username: username.value,
        email: email.value,
        password: password.value,
        role: "physician"
      });
      alert("Signup successful! You can now log in.");
      isSignup.value = false;
    } else {
      const res = await axios.post("http://localhost:8000/token", new URLSearchParams({
        username: username.value,
        password: password.value
      }));
      localStorage.setItem("token", res.data.access_token);
      alert("Login successful! Token saved to localStorage.");
      // Here you would typically redirect the user, e.g., useRouter().push('/')
    }
  } catch (err) {
    alert(err.response?.data?.detail || "An error occurred");
  }
};
</script>