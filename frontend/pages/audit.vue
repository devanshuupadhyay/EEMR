<script setup>
import { ref, reactive, onMounted, watch, computed } from 'vue';
import axios from 'axios';

definePageMeta({
  layout: "default",
});

const theme = useTheme();

// --- Reactive State ---
const auditLogs = ref([]);
const isLoading = ref(false);
const error = ref(null);

const filters = reactive({
  path: '',
  method: '',
  status: ''
});

// --- Pagination State ---
const currentPage = ref(1);
const totalLogs = ref(0);
const limit = ref(10); 
const totalPages = computed(() => Math.ceil(totalLogs.value / limit.value));

const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};

const getAuditLogs = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const params = {
      search_path: filters.path,
      search_method: filters.method,
      search_status: filters.status,
      page: currentPage.value,
      limit: limit.value,
    };
    const response = await axios.get('http://localhost:8000/api/v1/audit', { params });
    auditLogs.value = response.data.logs.map(log => ({
      ...log,
      duration: `${(log.duration * 1000).toFixed(2)} ms`
    }));
    totalLogs.value = response.data.total;
  } catch (err) {
    error.value = err.response?.data?.detail || 'An unexpected error occurred.';
  } finally {
    isLoading.value = false;
  }
};

watch(filters, debounce(() => {
  currentPage.value = 1; 
  getAuditLogs();
}, 350));

const nextPage = () => { if (currentPage.value < totalPages.value) { currentPage.value++; getAuditLogs(); } };
const prevPage = () => { if (currentPage.value > 1) { currentPage.value--; getAuditLogs(); } };

onMounted(getAuditLogs);

const statusColorClass = (statusCode) => {
  if (statusCode >= 500) return 'text-red-400';
  if (statusCode >= 400) return 'text-yellow-400';
  if (statusCode >= 200) return 'text-green-400';
  return 'text-neutral-light';
};
</script>

<template>
  <div>
    <h2 :class="[theme.typography.h2, theme.typography.headings]">Audit Log</h2>
    <p :class="[theme.colors.neutral.light, 'mt-2']">Review of all API requests and system activities.</p>

    <div :class="[theme.components.card.compact, 'mt-4']">
      <div v-if="error" class="p-3 bg-red-900/50 text-red-300 rounded-lg mb-3"><strong>Error:</strong> {{ error }}</div>

      <div class="overflow-x-auto">
        <table class="w-full text-left">
          <thead>
            <tr :class="['border-b', { 'border-neutral-700': true }]">
              <th class="p-2 w-24">Method</th>
              <th class="p-2">Path</th>
              <th class="p-2 w-28">Status</th>
              <th class="p-2 w-32 text-right">Duration</th>
            </tr>
            <tr :class="['border-b', { 'border-neutral-700': true }]">
              <th class="p-1"><input v-model="filters.method" placeholder="Filter..." :class="theme.components.input.compact" /></th>
              <th class="p-1"><input v-model="filters.path" placeholder="Filter..." :class="theme.components.input.compact" /></th>
              <th class="p-1"><input v-model="filters.status" placeholder="Filter..." :class="theme.components.input.compact" /></th>
              <th class="p-1"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="isLoading"><td colspan="4" class="text-center p-4 animate-pulse">Loading...</td></tr>
            <tr v-else-if="auditLogs.length === 0"><td colspan="4" class="text-center p-4">No audit logs match your search.</td></tr>
            <tr v-else v-for="(log, index) in auditLogs" :key="index" :class="['border-b', { 'border-neutral-800': true }, 'hover:bg-neutral-800 text-sm']">
              <td class="p-2 font-mono font-semibold" :class="{'text-cyan-400': log.method === 'GET', 'text-green-400': log.method === 'POST', 'text-yellow-400': log.method === 'OPTIONS'}">{{ log.method }}</td>
              <td class="p-2 font-mono">{{ log.path }}</td>
              <td class="p-2 font-semibold" :class="statusColorClass(log.status_code)">{{ log.status_code }}</td>
              <td class="p-2 text-right font-mono">{{ log.duration }}</td>
            </tr>
          </tbody>
        </table>
      </div>

       <div class="flex justify-between items-center mt-3 pt-3 border-t border-neutral-700">
        <button @click="prevPage" :disabled="currentPage <= 1" :class="[theme.components.button.base, 'bg-neutral-dark hover:bg-neutral-medium disabled:opacity-50']">
          Previous
        </button>
        <span class="text-sm text-neutral-light">
          Page {{ currentPage }} of {{ totalPages }} ({{ totalLogs }} total)
        </span>
        <button @click="nextPage" :disabled="currentPage >= totalPages" :class="[theme.components.button.base, 'bg-neutral-dark hover:bg-neutral-medium disabled:opacity-50']">
          Next
        </button>
      </div>
    </div>
  </div>
</template>