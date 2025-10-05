<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';

definePageMeta({
  layout: "default",
});

const theme = useTheme();

// --- Section Management ---
const sections = [
  { id: 'create', title: 'Create New Patient', description: 'Add a new patient to the EMR.' },
  { id: 'find', title: 'Find Patient by ID', description: 'Search for an individual patient record.' },
  { id: 'all', title: 'View All Patients', description: 'Display a list of all patient records.' },
];
const currentSectionIndex = ref(0);
const activeSection = computed(() => sections[currentSectionIndex.value]);

const resetState = () => {
  error.value = null;
  successMessage.value = '';
  foundPatient.value = null;
};

const navigate = (direction) => {
  const newIndex = (currentSectionIndex.value + direction + sections.length) % sections.length;
  currentSectionIndex.value = newIndex;
  handleSectionChange();
};

const jumpToSection = (index) => {
  currentSectionIndex.value = index;
  handleSectionChange();
};

const handleSectionChange = () => {
  resetState();
  if (activeSection.value.id === 'all') {
    getAllPatients();
  }
}

// --- Reactive State ---
const searchId = ref('');
const foundPatient = ref(null);
const newPatient = ref({ id: '', givenName: '', familyName: '', birthDate: '', gender: 'female' });
const allPatients = ref([]);

// UI State
const isLoading = ref(false);
const error = ref(null);
const successMessage = ref('');

// --- API Functions ---
const getPatientById = async () => {
  if (!searchId.value) {
    error.value = 'Please enter a Patient ID to search.';
    return;
  }
  await performRequest(async () => {
    const response = await axios.get(`http://localhost:8000/api/v1/Patient/${searchId.value}`);
    foundPatient.value = response.data;
    successMessage.value = `Successfully found patient ${searchId.value}.`;
  });
};

const getAllPatients = async () => {
  await performRequest(async () => {
    const response = await axios.get('http://localhost:8000/api/v1/Patient');
    allPatients.value = response.data;
    if (response.data.length === 0) {
      successMessage.value = 'No patients found in the database.';
    }
  });
};

const createPatient = async () => {
  if (!newPatient.value.id || !newPatient.value.givenName || !newPatient.value.familyName || !newPatient.value.birthDate) {
    error.value = 'Please fill out all fields to create a patient.';
    return;
  }
  await performRequest(async () => {
    const fhirPayload = {
      resourceType: "Patient",
      id: newPatient.value.id,
      name: [{ use: "official", family: newPatient.value.familyName, given: [newPatient.value.givenName] }],
      gender: newPatient.value.gender,
      birthDate: newPatient.value.birthDate
    };
    const response = await axios.post('http://localhost:8000/api/v1/Patient', fhirPayload);
    successMessage.value = `Successfully created patient ${response.data.id}.`;
    if (activeSection.value.id === 'all') await getAllPatients();
    Object.keys(newPatient.value).forEach(k => newPatient.value[k] = '');
    newPatient.value.gender = 'female';
  });
};

const performRequest = async (apiCall) => {
  isLoading.value = true;
  resetState();
  try {
    await apiCall();
  } catch (err) {
    error.value = err.response?.data?.detail || 'An unexpected error occurred.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div>
    <h3 :class="[theme.typography.h3, theme.typography.headings]">Patient Management</h3>

    <div class="mt-1 flex items-center justify-center gap-1 p-1 rounded-lg bg-neutral-dark border border-neutral-medium">
      <button v-for="(section, index) in sections" :key="section.id" @click="jumpToSection(index)"
              :class="['px-1 py-1.5 rounded-md text-sm font-medium transition-colors',
                       currentSectionIndex === index ? 'bg-secondary text-neutral-lightest' : 'text-neutral-light hover:bg-neutral-medium']">
        {{ section.title }}
      </button>
    </div>

    <div class="relative mt-4">
      <button @click="navigate(-1)" class="absolute left-0 top-1/2 -translate-y-1/2 p-2 rounded-full bg-neutral-dark hover:bg-secondary z-10 transition-all">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-neutral-lightest" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" /></svg>
      </button>
      <button @click="navigate(1)" class="absolute right-0 top-1/2 -translate-y-1/2 p-2 rounded-full bg-neutral-dark hover:bg-secondary z-10 transition-all">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-neutral-lightest" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7" /></svg>
      </button>

      <div class="w-full max-w-4xl mx-auto">
        <div v-for="(section, index) in sections" :key="section.id">
          <div v-if="index === currentSectionIndex" :class="[theme.components.card.base, 'w-full min-h-[350px]']">
            <p class="text-sm" :style="{ color: theme.colors.primary }">{{ section.title }}</p>
            <p :class="[theme.colors.neutral.light, 'text-sm']">{{ section.description }}</p>

            <div v-if="isLoading || successMessage || error" class="my-1 p-1 rounded-lg text-sm"
                 :class="{'bg-neutral-dark animate-pulse': isLoading, 'bg-green-900/50 text-green-300': successMessage, 'bg-red-900/50 text-red-300': error}">
                <p v-if="isLoading">Loading...</p>
                <p v-if="successMessage">{{ successMessage }}</p>
                <p v-if="error"><strong>Error:</strong> {{ error }}</p>
            </div>

            <div class="mt-3 border-t border-neutral-700 pt-3">
              <div v-if="section.id === 'create'" class="space-y-3">
                <input v-model="newPatient.id" placeholder="Patient ID (e.g., p3)" :class="theme.components.input.base" />
                <input v-model="newPatient.givenName" placeholder="Given Name" :class="theme.components.input.base" />
                <input v-model="newPatient.familyName" placeholder="Family Name" :class="theme.components.input.base" />
                <input v-model="newPatient.birthDate" type="date" :class="theme.components.input.base" />
                <select v-model="newPatient.gender" :class="theme.components.input.base">
                    <option value="female">Female</option><option value="male">Male</option><option value="other">Other</option><option value="unknown">Unknown</option>
                </select>
                <button @click="createPatient" :class="[theme.components.button.base, theme.components.button.primary, 'w-full text-neutral-darkest']">Create</button>
              </div>

              <div v-if="section.id === 'find'">
                <div class="flex items-center gap-4">
                    <input v-model="searchId" placeholder="Enter Patient ID" :class="theme.components.input.base" @keyup.enter="getPatientById" />
                    <button @click="getPatientById" :class="[theme.components.button.base, 'bg-secondary text-neutral-lightest']">Search</button>
                </div>
                <div v-if="foundPatient" class="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
                   <div><p :class="theme.colors.neutral.light">Name</p><p class="text-lg font-semibold">{{ foundPatient.name[0].given.join(' ') }} {{ foundPatient.name[0].family }}</p></div>
                   <div><p :class="theme.colors.neutral.light">Gender</p><p class="text-lg font-semibold">{{ foundPatient.gender }}</p></div>
                   <div><p :class="theme.colors.neutral.light">Date of Birth</p><p class="text-lg font-semibold">{{ foundPatient.birthDate }}</p></div>
                   <div><p :class="theme.colors.neutral.light">Patient ID</p><p class="text-lg font-semibold">{{ foundPatient.id }}</p></div>
                </div>
              </div>

              <div v-if="section.id === 'all'" class="overflow-x-auto">
                 <table class="w-full text-left">
                    <thead><tr :class="['border-b', { 'border-neutral-700': true }]"><th class="px-1">ID</th><th class="px-1">Name</th><th class="px-1">Gender</th><th class="px-1">Birth Date</th></tr></thead>
                    <tbody>
                        <tr v-if="allPatients.length === 0 && !isLoading"><td colspan="4" class="text-center p-1">No patients found.</td></tr>
                        <tr v-for="p in allPatients" :key="p.id" :class="['border-b', { 'border-neutral-800': true }, 'hover:bg-neutral-800']">
                            <td class="p-1 font-mono">{{ p.id }}</td>
                            <td class="p-1">{{ p.name[0].given.join(' ') }} {{ p.name[0].family }}</td>
                            <td class="p-1">{{ p.gender }}</td>
                            <td class="p-1">{{ p.birthDate }}</td>
                        </tr>
                    </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>