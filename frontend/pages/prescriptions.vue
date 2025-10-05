<script setup>
definePageMeta({ layout: "default" });
const theme = useTheme();
</script>

<template>
  <div>
    <h2 :class="[theme.typography.h2, theme.typography.headings]">Prescriptions</h2>
    <p :class="[theme.colors.neutral.light, 'mt-1', 'text-sm']">Manage e-prescribing and medication history.</p>
    <div :class="[theme.components.card.base, 'mt-4', 'text-center']">
      🚧 Content for Prescription Management coming soon.
    </div>
  </div>
</template>