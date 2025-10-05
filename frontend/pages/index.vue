<script setup>
definePageMeta({
  layout: "default",
});

const theme = useTheme();

const modules = [
  { name: "Users", description: "Manage roles, accounts & access", link: "/users" },
  { name: "Patients", description: "Demographics & insurance", link: "/patients" },
  { name: "Appointments", description: "Scheduling & calendar", link: "/appointments" },
  { name: "Encounters", description: "SOAP notes & clinical history", link: "/encounters" },
  { name: "Prescriptions", description: "eRx management", link: "/prescriptions" },
  { name: "Labs", description: "Orders & results", link: "/labs" },
  { name: "Billing", description: "Claims & payments", link: "/billing" },
  { name: "Audit Logs", description: "Track all user activity", link: "/audit" },
];
</script>

<template>
  <div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <NuxtLink v-for="mod in modules" :key="mod.name" :to="mod.link" :class="theme.components.card.base">
        <span class="text-xl font-bold" :style="{ color: theme.colors.primary }">
          {{ mod.name }}
        </span>
        <p :class="[theme.colors.neutral.light, 'text-sm']">
          {{ mod.description }}
        </p>
      </NuxtLink>
    </div>
  </div>
</template>