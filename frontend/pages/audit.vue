<script setup>
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Audit</h2>
    <p :class="theme.colors.muted">Manage audit logs & activities.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: Audit log view
    </div>
  </div>
</template>
