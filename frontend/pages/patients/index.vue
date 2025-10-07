<template>
  <div :class="[theme.components.card.compact, 'w-full min-h-[350px]']">
    <p class="text-sm" :style="{ color: theme.colors.primary }">View All Patients</p>
    <p :class="[theme.colors.neutral.light, 'text-xs mt-1']">Display a list of all patient records.</p>
    
    <div v-if="isLoading || successMessage || error" class="my-1 p-1 rounded-lg text-xs"
          :class="{'bg-neutral-dark animate-pulse': isLoading, 'bg-green-900/50 text-green-300': successMessage, 'bg-red-900/50 text-red-300': error}">
        <p v-if="isLoading">Loading...</p>
        <p v-if="successMessage">{{ successMessage }}</p>
        <p v-if="error"><strong>Error:</strong> {{ error }}</p>
    </div>

    <div class="mt-3 border-t border-neutral-700 pt-3 overflow-x-auto">
        <table class="w-full text-left">
            <thead>
                <tr :class="['border-b', { 'border-neutral-700': true }]">
                    <th class="px-1">ID</th>
                    <th class="px-1">Name</th>
                    <th class="px-1">Gender</th>
                    <th class="px-1">Birth Date</th>
                    <th class="px-1">MRN</th>
                    <th class="px-1">Phone</th>
                    <th class="px-1">Address</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="allPatients.length === 0 && !isLoading"><td colspan="7" class="text-center p-1">No patients found.</td></tr>
                <tr v-else v-for="p in allPatients" :key="p.id" :class="['border-b', { 'border-neutral-800': true }, 'hover:bg-neutral-800']">
                    <td class="p-1 font-mono">{{ p.id }}</td>
                    <td class="p-1">{{ p.name?.[0]?.given?.[0] }} {{ p.name?.[0]?.family }}</td>
                    <td class="p-1">{{ p.gender }}</td>
                    <td class="p-1">{{ p.birthDate }}</td>
                    <td class="p-1 font-mono">{{ p.identifier?.[0]?.value }}</td>
                    <td class="p-1">{{ p.telecom?.[0]?.value }}</td>
                    <td class="p-1">{{ p.address?.[0]?.line?.[0] }}, {{ p.address?.[0]?.city }}</td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const theme = useTheme();

const allPatients = ref([]);
const isLoading = ref(false);
const error = ref(null);
const successMessage = ref('');

const getAllPatients = async () => {
    isLoading.value = true;
    error.value = null;
    successMessage.value = '';
    try {
        const response = await axios.get('http://localhost:8000/api/v1/Patient');
        allPatients.value = response.data;
        if (response.data.length === 0) {
            successMessage.value = 'No patients found in the database.';
        }
    } catch (err) {
        error.value = err.response?.data?.detail || 'An unexpected error occurred.';
    } finally {
        isLoading.value = false;
    }
};

onMounted(getAllPatients);
</script>