<template>
  <div class="flex items-center justify-center min-h-screen p-6 bg-slate-900 text-gray-200">
    <div class="max-w-4xl mx-auto backdrop-blur-xl bg-gray-800/50 rounded-3xl border border-gray-700 p-8 md:p-12 shadow-[0_0_60px_-15px_rgba(124,58,237,0.3)] text-center">
      <h1 class="text-5xl font-extrabold mb-4 font-mono tracking-tighter">
        <span class="bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-600">
          Easy EMR
        </span>
      </h1>
      <p class="text-lg text-gray-400 mb-10">
        Secure. Streamlined. Seamless.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <a
          href="http://localhost:3000/login"
          target="_blank"
          class="block p-6 bg-gray-800/70 rounded-2xl border border-gray-700 hover:border-cyan-400 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-purple-500 glass-card"
        >
          <div class="flex flex-col items-center justify-center h-full">
            <span class="text-xl font-bold mb-1 text-cyan-400">Frontend (Nuxt)</span>
            <span class="text-sm text-gray-500">Port 3000</span>
          </div>
        </a>

        <a
          href="http://localhost:8000/docs"
          target="_blank"
          class="block p-6 bg-gray-800/70 rounded-2xl border border-gray-700 hover:border-purple-500 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-purple-500 glass-card"
        >
          <div class="flex flex-col items-center justify-center h-full">
            <span class="text-xl font-bold mb-1 text-purple-400">Backend API (FastAPI)</span>
            <span class="text-sm text-gray-500">Port 8000</span>
          </div>
        </a>

        <a
          href="http://localhost:3001"
          target="_blank"
          class="block p-6 bg-gray-800/70 rounded-2xl border border-gray-700 hover:border-purple-500 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-purple-500 glass-card"
        >
          <div class="flex flex-col items-center justify-center h-full">
            <span class="text-xl font-bold mb-1 text-purple-400">Grafana</span>
            <span class="text-sm text-gray-500">Port 3001</span>
          </div>
        </a>

        <a
          href="http://localhost:9090"
          target="_blank"
          class="block p-6 bg-gray-800/70 rounded-2xl border border-gray-700 hover:border-cyan-400 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-purple-500 glass-card"
        >
          <div class="flex flex-col items-center justify-center h-full">
            <span class="text-xl font-bold mb-1 text-cyan-400">Prometheus</span>
            <span class="text-sm text-gray-500">Port 9090</span>
          </div>
        </a>

        <div
          class="p-6 bg-gray-800/70 rounded-2xl border border-gray-700 cursor-not-allowed glass-card"
        >
          <div class="flex flex-col items-center justify-center h-full">
            <span class="text-xl font-bold mb-1 text-gray-500">Redis</span>
            <span class="text-sm text-gray-600">Port 6379 (CLI/GUI access only)</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>