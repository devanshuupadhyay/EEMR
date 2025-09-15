<template>
  <div class="max-w-md mx-auto mt-20 p-6 border rounded shadow">
    <h2 class="text-2xl font-bold mb-4">{{ isSignup ? "Sign Up" : "Login" }}</h2>

    <form @submit.prevent="handleSubmit">
      <input v-model="username" placeholder="Username" class="border p-2 w-full mb-4" required />
      <input v-model="email" placeholder="Email" v-if="isSignup" class="border p-2 w-full mb-4" required />
      <input v-model="password" type="password" placeholder="Password" class="border p-2 w-full mb-4" required />
      <button type="submit" class="bg-blue-500 text-white p-2 w-full mb-2">
        {{ isSignup ? "Sign Up" : "Login" }}
      </button>
    </form>

    <p class="text-center text-gray-600">
      <span @click="toggleForm" class="cursor-pointer text-blue-500">
        {{ isSignup ? "Already have an account? Login" : "Don't have an account? Sign Up" }}
      </span>
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const isSignup = ref(false);
const username = ref("");
const email = ref("");
const password = ref("");

// Toggle between login and signup
const toggleForm = () => {
  isSignup.value = !isSignup.value;
};

// Submit handler
const handleSubmit = async () => {
  try {
    if (isSignup.value) {
      // Sign up
      await axios.post("http://localhost:8000/signup", {
        username: username.value,
        email: email.value,
        password: password.value,
        role: "physician" // default role
      });
      alert("Signup successful! You can now log in.");
      isSignup.value = false; // switch to login
    } else {
      // Login
      const res = await axios.post("http://localhost:8000/token", {
        username: username.value,
        password: password.value
      });
      localStorage.setItem("token", res.data.access_token);
      alert("Login successful! Token saved to localStorage.");
    }
    username.value = "";
    email.value = "";
    password.value = "";
  } catch (err) {
    alert(err.response?.data?.detail || "An error occurred");
  }
};
</script>
