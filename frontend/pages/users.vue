<script setup>
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Users</h2>
    <p :class="theme.colors.muted">Manage user accounts & permissions.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: User list & profile view
    </div>
  </div>
</template>
