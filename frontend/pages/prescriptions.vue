<script setup>
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Prescriptions</h2>
    <p :class="theme.colors.muted">Manage patient prescriptions & medications.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: Prescriptions view
    </div>
  </div>
</template>
