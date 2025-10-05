<script setup>
definePageMeta({ layout: "default" });
const theme = useTheme();
</script>

<template>
  <div>
    <h2 :class="[theme.typography.h2, theme.typography.headings]">Encounters</h2>
    <p :class="[theme.colors.neutral.light, 'mt-1', 'text-sm']">Manage clinical notes and patient visit history.</p>
    <div :class="[theme.components.card.base, 'mt-4', 'text-center']">
      🚧 Content for Encounters and SOAP notes coming soon.
    </div>
  </div>
</template>