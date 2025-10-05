<script setup>
definePageMeta({ layout: "default" });
const theme = useTheme();
</script>

<template>
  <div>
    <h2 :class="[theme.typography.h2, theme.typography.headings]">Labs</h2>
    <p :class="[theme.colors.neutral.light, 'mt-1', 'text-sm']">Manage lab orders and view results.</p>
    <div :class="[theme.components.card.base, 'mt-4', 'text-center']">
      🚧 Content for Lab Management coming soon.
    </div>
  </div>
</template>