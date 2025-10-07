<template>
  <div :class="[theme.components.card.compact, 'w-full min-h-[350px]']">
    <p class="text-sm" :style="{ color: theme.colors.primary }">Find Patient by ID</p>
    <p :class="[theme.colors.neutral.light, 'text-xs mt-1']">Search for an individual patient record.</p>

    <div v-if="isLoading || successMessage || error" class="my-1 p-1 rounded-lg text-xs"
          :class="{'bg-neutral-dark animate-pulse': isLoading, 'bg-green-900/50 text-green-300': successMessage, 'bg-red-900/50 text-red-300': error}">
        <p v-if="isLoading">Loading...</p>
        <p v-if="successMessage">{{ successMessage }}</p>
        <p v-if="error"><strong>Error:</strong> {{ error }}</p>
    </div>

    <div class="mt-3 border-t border-neutral-700 pt-3">
        <div class="flex items-center gap-4">
            <input v-model="searchId" placeholder="Enter Patient ID" :class="theme.components.input.base" @keyup.enter="getPatientById" />
            <button @click="getPatientById" :class="[theme.components.button.base, 'bg-secondary text-neutral-lightest']">Search</button>
        </div>
        <div v-if="foundPatient" class="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div><p :class="theme.colors.neutral.light">ID</p><p class="text-lg font-semibold">{{ foundPatient.id }}</p></div>
            <div><p :class="theme.colors.neutral.light">Name</p><p class="text-lg font-semibold">{{ foundPatient.name?.[0]?.given?.[0] }} {{ foundPatient.name?.[0]?.family }}</p></div>
            <div><p :class="theme.colors.neutral.light">Gender</p><p class="text-lg font-semibold">{{ foundPatient.gender }}</p></div>
            <div><p :class="theme.colors.neutral.light">Date of Birth</p><p class="text-lg font-semibold">{{ foundPatient.birthDate }}</p></div>
            <div><p :class="theme.colors.neutral.light">MRN</p><p class="text-lg font-semibold">{{ foundPatient.identifier?.[0]?.value }}</p></div>
            <div><p :class="theme.colors.neutral.light">Phone</p><p class="text-lg font-semibold">{{ foundPatient.telecom?.[0]?.value }}</p></div>
            <div><p :class="theme.colors.neutral.light">Address</p><p class="text-lg font-semibold">{{ foundPatient.address?.[0]?.line?.[0] }}, {{ foundPatient.address?.[0]?.city }}, {{ foundPatient.address?.[0]?.state }} {{ foundPatient.address?.[0]?.postalCode }}</p></div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const theme = useTheme();
const searchId = ref('');
const foundPatient = ref(null);
const isLoading = ref(false);
const error = ref(null);
const successMessage = ref('');

const getPatientById = async () => {
    if (!searchId.value) {
        error.value = 'Please enter a Patient ID to search.';
        return;
    }
    isLoading.value = true;
    error.value = null;
    successMessage.value = '';
    foundPatient.value = null;
    try {
        const response = await axios.get(`http://localhost:8000/api/v1/Patient/${searchId.value}`);
        foundPatient.value = response.data;
        successMessage.value = `Successfully found patient ${searchId.value}.`;
    } catch (err) {
        error.value = err.response?.data?.detail || 'An unexpected error occurred.';
    } finally {
        isLoading.value = false;
    }
};
</script>