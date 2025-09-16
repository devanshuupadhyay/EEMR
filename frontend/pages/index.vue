<script setup>
definePageMeta({
  layout: "default",
})

const theme = useTheme()

// Module metadata for cleaner markup
const modules = [
  {
    name: "Users",
    description: "Manage roles, accounts & access",
    link: "/users",
    accent: theme.colors.secondary,
  },
  {
    name: "Patients",
    description: "Demographics & insurance",
    link: "/patients",
    accent: theme.colors.secondary,
  },
  {
    name: "Appointments",
    description: "Scheduling & calendar",
    link: "/appointments",
    accent: theme.colors.secondary,
  },
  {
    name: "Encounters",
    description: "SOAP notes & clinical history",
    link: "/encounters",
    accent: theme.colors.secondary,
  },
  {
    name: "Prescriptions",
    description: "eRx management",
    link: "/prescriptions",
    accent: theme.colors.secondary,
  },
  {
    name: "Labs",
    description: "Orders & results",
    link: "/labs",
    accent: theme.colors.secondary,
  },
  {
    name: "Billing",
    description: "Claims & payments",
    link: "/billing",
    accent: theme.colors.secondary,
  },
  {
    name: "Audit Logs",
    description: "Track all user activity",
    link: "/audit",
    accent: theme.colors.secondary,
  },
]
</script>

<template>
  <div>
    <!-- Application Modules -->
    <h2 :class="[theme.typography.sizes.h2, theme.typography.headings, 'mb-6']">
      Application Modules
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <a
        v-for="mod in modules"
        :key="mod.name"
        :href="mod.link"
        :class="[theme.components.card.base, 'group']"
      >
        <span
          class="text-xl font-bold transition-colors"
          :style="{ color: mod.accent }"
        >
          {{ mod.name }}
        </span>
        <p
          :class="[theme.typography.sizes.small, 'transition-colors']"
          :style="{ color: theme.colors.neutral.light }"
        >
          {{ mod.description }}
        </p>
      </a>
    </div>
  </div>
</template>
