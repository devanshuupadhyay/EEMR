<template>
  <div :class="[theme.components.card.compact, 'w-full min-h-[350px]']">
    <p class="text-sm" :style="{ color: theme.colors.primary }">Create New Patient</p>
    <p :class="[theme.colors.neutral.light, 'text-xs mt-1']">Add a new patient to the EMR.</p>

    <div v-if="isLoading || successMessage || error" class="my-1 p-1 rounded-lg text-xs"
          :class="{'bg-neutral-dark animate-pulse': isLoading, 'bg-green-900/50 text-green-300': successMessage, 'bg-red-900/50 text-red-300': error}">
        <p v-if="isLoading">Loading...</p>
        <p v-if="successMessage">{{ successMessage }}</p>
        <p v-if="error"><strong>Error:</strong> {{ error }}</p>
    </div>

    <div class="mt-3 border-t border-neutral-700 pt-3">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="space-y-3">
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Patient ID</label>
                    <input v-model="newPatient.id" :class="theme.components.input.compact" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Given Name</label>
                    <input v-model="newPatient.name[0].given[0]" :class="theme.components.input.compact" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Family Name</label>
                    <input v-model="newPatient.name[0].family" :class="theme.components.input.compact" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Date of Birth</label>
                    <input v-model="newPatient.birthDate" type="date" :class="theme.components.input.datepicker" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Gender</label>
                    <select v-model="newPatient.gender" :class="theme.components.input.compact">
                        <option value="female">Female</option>
                        <option value="male">Male</option>
                        <option value="other">Other</option>
                        <option value="unknown">Unknown</option>
                    </select>
                </div>
            </div>
            <div class="space-y-3">
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Medical Record Number</label>
                    <input v-model="newPatient.identifier[0].value" :class="theme.components.input.compact" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Phone Number</label>
                    <input v-model="newPatient.telecom[0].value" :class="theme.components.input.compact" />
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Address</label>
                    <input v-model="newPatient.address[0].line[0]" :class="theme.components.input.compact" />
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                        <label :class="theme.typography.small" class="text-neutral-light block mb-1">City</label>
                        <input v-model="newPatient.address[0].city" :class="theme.components.input.compact" />
                    </div>
                    <div>
                        <label :class="theme.typography.small" class="text-neutral-light block mb-1">State</label>
                        <input v-model="newPatient.address[0].state" :class="theme.components.input.compact" />
                    </div>
                </div>
                <div>
                    <label :class="theme.typography.small" class="text-neutral-light block mb-1">Postal Code</label>
                    <input v-model="newPatient.address[0].postalCode" :class="theme.components.input.compact" />
                </div>
            </div>
            <div class="md:col-span-2">
                <button @click="createPatient" :class="[theme.components.button.base, theme.components.button.primary, 'w-full text-neutral-darkest']">Create Patient</button>
            </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const theme = useTheme();

const newPatient = ref({
  id: '',
  name: [{ given: [''], family: '' }],
  gender: 'female',
  birthDate: '',
  identifier: [{ system: 'medical-record-number', value: '' }],
  address: [{ line: [''], city: '', state: '', postalCode: '', country: '' }],
  telecom: [{ system: 'phone', value: '' }],
  maritalStatus: { text: 'Unknown' },
});

const isLoading = ref(false);
const error = ref(null);
const successMessage = ref('');

const createPatient = async () => {
    if (!newPatient.value.id || !newPatient.value.name[0].given[0] || !newPatient.value.name[0].family || !newPatient.value.birthDate) {
        error.value = 'Please fill out all required fields to create a patient.';
        return;
    }
    isLoading.value = true;
    error.value = null;
    successMessage.value = '';
    try {
        const fhirPayload = {
            resourceType: "Patient",
            ...newPatient.value,
            name: [{
                use: "official",
                family: newPatient.value.name[0].family,
                given: [newPatient.value.name[0].given[0]]
            }]
        };
        const response = await axios.post('http://localhost:8000/api/v1/Patient', fhirPayload);
        successMessage.value = `Successfully created patient ${response.data.id}.`;
        
        // Reset form fields
        newPatient.value = {
            id: '',
            name: [{ given: [''], family: '' }],
            gender: 'female',
            birthDate: '',
            identifier: [{ system: 'medical-record-number', value: '' }],
            address: [{ line: [''], city: '', state: '', postalCode: '', country: '' }],
            telecom: [{ system: 'phone', value: '' }],
            maritalStatus: { text: 'Unknown' },
        };
    } catch (err) {
        error.value = err.response?.data?.detail || 'An unexpected error occurred.';
    } finally {
        isLoading.value = false;
    }
};
</script>