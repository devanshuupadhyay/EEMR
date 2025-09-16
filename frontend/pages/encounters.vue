<script setup>
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Encounters</h2>
    <p :class="theme.colors.muted">Manage patient encounters & clinical visits.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: Encounters view
    </div>
  </div>
</template>
