<template>
  <div class="bg-neutral-darkest text-neutral-lightest min-h-screen flex flex-col font-sans">
    <header class="bg-neutral-dark border-b border-neutral-medium p-4 flex justify-between items-center shadow-md">
      
      <NuxtLink to="/" class="flex items-center gap-x-1 cursor-pointer">
        <img src="/icons/eemr_icon.png" alt="Easy EMR Logo" class="h-8 w-8 hexagon-img" />
        <div class="text-xl font-bold text-secondary">Easy EMR</div>
      </NuxtLink>

      <nav class="flex gap-4">
        <a
          href="http://localhost:3000/login"
          target="_blank"
          class="hover:text-secondary transition"
        >
          Frontend
        </a>
        <a
          href="http://localhost:8000/docs"
          target="_blank"
          class="hover:text-secondary transition"
        >
          Backend
        </a>
        <a
          href="https://sentry.io/organizations/test-4ze/issues/"
          target="_blank"
          class="hover:text-secondary transition"
        >
          Sentry
        </a>
        <a
          href="http://localhost:3001"
          target="_blank"
          class="hover:text-secondary transition"
        >
          Grafana
        </a>
        <a
          href="http://localhost:9090"
          target="_blank"
          class="hover:text-secondary transition"
        >
          Prometheus
        </a>
        <span class="text-neutral-light cursor-not-allowed">Redis</span>
      </nav>
    </header>

    <main class="flex-1 p-6 animate-fadeIn">
      <slot />
    </main>

    <footer class="bg-neutral-dark border-t border-neutral-medium p-4 text-sm text-neutral-light text-center">
      © 2025 Easy EMR — Futuristic Care Simplified
    </footer>
  </div>
</template>

<script setup>
// Default layout applies global theme classes
</script>

<style>
/* 🎞️ Subtle animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.5s ease-in-out;
}
</style>