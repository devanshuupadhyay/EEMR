<template>
  <div>
    <h3 :class="[theme.typography.h3, theme.typography.headings]">Patient Management</h3>
    <MultiPanelNavigation :sections="sections" />
    <div class="mt-4">
      <NuxtPage />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import MultiPanelNavigation from '~/components/MultiPanelNavigation.vue';

definePageMeta({ layout: "default" });

const theme = useTheme();
const router = useRouter();

const sections = [
  { id: 'all', title: 'View All Patients', description: 'Display a list of all patient records.', link: '/patients' },
  { id: 'find', title: 'Find Patient by ID', description: 'Search for an individual patient record.', link: '/patients/find' },
  { id: 'create', title: 'Create New Patient', description: 'Add a new patient to the EMR.', link: '/patients/create' },
];

</script>