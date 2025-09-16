<script setup>
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Labs</h2>
    <p :class="theme.colors.muted">Manage lab tests & results.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: Labs view
    </div>
  </div>
</template>
